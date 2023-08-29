from sqlalchemy import create_engine
from sqlalchemy.engine import URL
import pandas as pd
from tqdm.notebook import tqdm
from nltk.sentiment import SentimentIntensityAnalyzer
from transformers import AutoTokenizer
from transformers import AutoModelForSequenceClassification
from transformers import pipeline
from scipy.special import softmax
import seaborn as sns
import text2emotion as te

#Connessione al database
url = URL.create(
    drivername="postgresql",
    username="postgres",
    host="/tmp/postgresql/socket",
    database="Tirocinio"
)


engine = create_engine("postgresql://postgres:PASSWORD@localhost:5432/TIROCINIO")

connection = engine.connect()

df1 = pd.read_sql_query('Select * from tirocinio.db_tweet2', con=engine)

#VADER

sia = SentimentIntensityAnalyzer()

res = {}
for i, row in tqdm(df1.iterrows(), total=len(df1)):
    text= row['text']
    myid = row['id']
    res[myid] = sia.polarity_scores(text)

vaders = pd.DataFrame(res).T
vaders = vaders.reset_index().rename(columns={'index' : 'id'})
vaders = vaders.merge(df1, how='left')

print(vaders)

#ROBERTA

MODEL = f"cardiffnlp/twitter-roberta-base-sentiment"
tokenizer = AutoTokenizer.from_pretrained(MODEL)
model = AutoModelForSequenceClassification.from_pretrained(MODEL)

def polarity_scores_roberta(example):
    encoded_text = tokenizer(example, return_tensors='pt')
    output = model(**encoded_text)
    scores = output[0][0].detach().numpy()
    scores = softmax(scores)
    scores_dict = {
        'roberta_neg' : scores[0],
        'roberta_neu' : scores[1],
        'roberta_pos' : scores[2]
    }
    return scores_dict

res = {}
for i, row in tqdm(df1.iterrows(), total=len(df1)):
        text = row['text']
        myid = row['id']
        res[myid] = polarity_scores_roberta(text)

roberta= pd.DataFrame(res).T
roberta = roberta.reset_index().rename(columns={'index' : 'id'})
roberta = roberta.merge(df1, how='left')

print(roberta)

#Vader + Roberta

MODEL = f"cardiffnlp/twitter-roberta-base-sentiment"
tokenizer = AutoTokenizer.from_pretrained(MODEL)
model = AutoModelForSequenceClassification.from_pretrained(MODEL)

def polarity_scores_roberta(example):
    encoded_text = tokenizer(example, return_tensors='pt')
    output = model(**encoded_text)
    scores = output[0][0].detach().numpy()
    scores = softmax(scores)
    scores_dict = {
        'roberta_neg' : scores[0],
        'roberta_neu' : scores[1],
        'roberta_pos' : scores[2]
    }
    return scores_dict

sia = SentimentIntensityAnalyzer()

res = {}
for i, row in tqdm(df1.iterrows(), total=len(df1)):
    try:
        text = row['text']
        myid = row['id']
        vader_result = sia.polarity_scores(text)
        vader_result_rename = {}
        for key, value in vader_result.items():
            vader_result_rename[f"vader_{key}"] = value
        roberta_result = polarity_scores_roberta(text)
        both = {**vader_result_rename, **roberta_result}
        res[myid] = both
    except RuntimeError:
        print(f'Broke for id {myid}')

results_df = pd.DataFrame(res).T
results_df = results_df.reset_index().rename(columns={'index': 'id'})
results_df = results_df.merge(df1, how='left')

results_df.to_sql('db_vader_roberta',con=engine ,schema='tirocinio',if_exists="replace",index=False)


#Text2Emotion

res = {}
for i, row in tqdm(df1.iterrows(), total=len(df1)):
    text= row['text']
    myid = row['id']
    res[myid] = te.get_emotion(text)

textemo = pd.DataFrame(res).T
textemo = textemo.reset_index().rename(columns={'index' : 'id'})
textemo = textemo.merge(df1, how='left')

print(textemo)


#Distilbert

tokenizer = AutoTokenizer.from_pretrained("joeddav/distilbert-base-uncased-go-emotions-student")
model = AutoModelForSequenceClassification.from_pretrained("joeddav/distilbert-base-uncased-go-emotions-student")
emotion = pipeline('sentiment-analysis', model='joeddav/distilbert-base-uncased-go-emotions-student')


def distilbert_28(example):
    encoded_text = tokenizer(example, return_tensors='pt')
    output = model(**encoded_text)
    scores = output[0][0].detach().numpy()
    scores = softmax(scores)
    scores_dict = {
       "admiration" : scores[0],
        "amusement": scores[1],
        "anger" : scores[2],
        "annoyance" : scores[3],
        "approval" : scores[4],
        "caring" : scores[5],
        "confusion" : scores[6],
        "curiosity" : scores[7],
        "desire" : scores[8],
        "disappointment" : scores[9],
        "disapproval" : scores[10],
        "disgust" : scores[11],
        "embarrassment" : scores[12],
        "excitement" : scores[13],
        "fear" : scores[14],
        "gratitude" : scores[15],
        "grief" : scores[16],
        "joy" : scores[17],
        "love" : scores[18],
        "nervousness" : scores[19],
        "optimism" : scores[20],
        "pride" : scores[21],
        "realization" : scores[22],
        "relief" : scores[23],
        "remorse" : scores[24],
        "sadness" : scores[25],
        "surprise" : scores[26],
        "neutral" : scores[27]
    }
    return scores_dict

def distilbert_first(text):
    scores_dict = {
         "emotion" : emotion(text)[0]['label'],
         "score" : emotion(text)[0]['score']
    }
    return scores_dict


res = {}
for i, row in tqdm(df1.iterrows(), total=len(df1)):
        text = row['text']
        myid = row['id']
        res[myid] = distilbert_first(text)

distilbert = pd.DataFrame(res).T
distilbert = distilbert.reset_index().rename(columns={'index' : 'id'})
distilbert = distilbert.merge(df1, how='left')

print(distilbert)
distilbert.to_sql('db_distilbert',con=engine ,schema='tirocinio',if_exists="replace",index=False)
