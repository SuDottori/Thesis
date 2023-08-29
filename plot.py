from sqlalchemy import create_engine
from sqlalchemy.engine import URL
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


#Connessione al database
url = URL.create(
    drivername="postgresql",
    username="postgres",
    host="/tmp/postgresql/socket",
    database="Tirocinio"
)

engine = create_engine("postgresql://postgres:PASSWORD@localhost:5432/TIROCINIO")

connection = engine.connect()

df_vader = pd.read_sql_query("SELECT ID, vader_pos as positive, vader_neg as negative, vader_neu as neutral, vader_compound as compound from tirocinio.db_vader_roberta", con=engine)
df_roberta = pd.read_sql_query("SELECT ID, roberta_pos as positive, roberta_neg as negative, roberta_neu as neutral from tirocinio.db_vader_roberta", con=engine)
df_distilbert = pd.read_sql_query("""SELECT 
   ID,
   CASE GREATEST(admiration,
		amusement,
        anger,
        annoyance,
        approval,
        caring,
        confusion,
        curiosity,
        desire,
        disappointment,
        disapproval,
        disgust,
        embarrassment,
        excitement,
        fear,
        gratitude,
        grief,
        joy,
        love,
        nervousness,
        optimism,
        pride,
        realization,
        relief,
        remorse,
        sadness,
        surprise,
        neutral)
         WHEN admiration THEN 'admiration'
         WHEN amusement THEN 'amusement'
         WHEN anger THEN 'anger'
		 WHEN annoyance THEN 'annoyance'
		 WHEN approval THEN 'approval'
		 WHEN caring THEN 'caring'
		 WHEN confusion THEN 'confusion'
		 WHEN curiosity THEN 'curiosity'
		 WHEN desire THEN 'desire'
		 WHEN disappointment THEN 'disappointment'
		 WHEN disapproval THEN 'disapproval'
		 WHEN disgust THEN 'disgust'
		 WHEN embarrassment THEN 'embarrassment'
		 WHEN excitement THEN 'excitement'
		 WHEN fear THEN 'fear'
		 WHEN gratitude THEN 'gratitude'
		 WHEN grief THEN 'grief'
		 WHEN joy THEN 'joy'
		 WHEN love THEN 'love'
		 WHEN nervousness THEN 'nervousness'
		 WHEN optimism THEN 'optimism'
		 WHEN pride THEN 'pride'
		 WHEN realization THEN 'realization'
		 WHEN relief THEN 'relief'
		 WHEN remorse THEN 'remorse'
		 WHEN sadness THEN 'sadness'
		 WHEN surprise THEN 'surprise'
		 WHEN neutral THEN 'neutral'
		END first_emotion,	
   (SELECT MAX(scores)
      FROM (VALUES (admiration),
		(amusement),
        (anger),
        (annoyance),
        (approval),
        (caring),
        (confusion),
        (curiosity),
        (desire),
        (disappointment),
        (disapproval),
        (disgust),
        (embarrassment),
        (excitement),
        (fear),
        (gratitude),
        (grief),
        (joy),
        (love),
        (nervousness),
        (optimism),
        (pride),
        (realization),
        (relief),
        (remorse),
        (sadness),
        (surprise),
        (neutral)) AS score(scores)) 
   AS scores
FROM tirocinio.db_distilbert""", con=engine)

#Distilbert plot
"""
emotion_counts = df_distilbert['first_emotion'].value_counts()

fig, ax = plt.subplots()
ax.bar(emotion_counts.index, emotion_counts.values)

ax.set_xlabel('Emotion')
ax.set_ylabel('Number of occurrences')
ax.set_title('Distribution of Emotions')

plt.xticks(rotation=90)

plt.show()
"""
#Vader plot

df_vader['sentiment'] = pd.cut(df_vader['compound'], bins=[-1.0, -0.5, 0.5, 1.0], labels=['negative', 'neutral', 'positive'])

sentiment_counts = df_vader['sentiment'].value_counts()
sentiment_percentages = (sentiment_counts / sentiment_counts.sum()) * 100  # Calcola le percentuali

ax = sentiment_percentages.plot(kind='bar', rot=0)
plt.title('Sentiment Distribution Vader')
plt.xlabel('Sentiment')
plt.ylabel('Percentage')

plt.xticks(rotation=0)
plt.yticks(range(0, int(sentiment_percentages.max()) + 10, 10))
for p in ax.patches:
    ax.annotate(f'{p.get_height():.1f}%', (p.get_x() + p.get_width() / 2, p.get_height()), ha='center', va='bottom')
plt.show()

#Roberta plot
"""
df_roberta['compound'] = (df_roberta['positive'] - df_roberta['negative']) / (df_roberta['positive'] + df_roberta['negative'] + df_roberta['neutral'])

df_roberta['sentiment'] = pd.cut(df_roberta['compound'], bins=[-1.0, -0.5, 0.5, 1.0], labels=['negative', 'neutral', 'positive'])

sentiment_counts = df_roberta['sentiment'].value_counts()
sentiment_counts.plot(kind='bar', rot=0)
plt.title('Sentiment Distribution Roberta')
plt.xlabel('Sentiment')
plt.ylabel('Count')
plt.show()
"""
