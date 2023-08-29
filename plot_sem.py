from sqlalchemy import create_engine
from sqlalchemy.engine import URL
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
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

#Creazione df per semestre
df_distilbert_sem1_2021 = pd.read_sql_query("""SELECT 
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
FROM tirocinio.db_distilbert
WHERE "created_at" BETWEEN '2021-01-01 00:00:00+00:00' AND '2021-06-30 23:59:59+00:00'""", con=engine)

df_distilbert_sem2_2021 = pd.read_sql_query("""SELECT 
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
FROM tirocinio.db_distilbert
WHERE "created_at" BETWEEN '2021-07-07 00:00:00+00:00' AND '2021-12-31 23:59:59+00:00'""", con=engine)

df_distilbert_sem1_2022 = pd.read_sql_query("""SELECT 
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
FROM tirocinio.db_distilbert
WHERE "created_at" BETWEEN '2022-01-01 00:00:00+00:00' AND '2022-06-30 23:59:59+00:00'""", con=engine)

df_distilbert_sem2_2022 = pd.read_sql_query("""SELECT 
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
FROM tirocinio.db_distilbert
WHERE "created_at" BETWEEN '2022-07-01 00:00:00+00:00' AND '2022-12-31 23:59:59+00:00'""", con=engine)

df_vader_sem1_2021 = pd.read_sql_query("""SELECT ID, vader_pos as positive, vader_neg as negative, vader_neu as neutral, vader_compound as compound from tirocinio.db_vader_roberta WHERE "created_at" BETWEEN '2021-01-01 00:00:00+00:00' AND '2021-06-30 23:59:59+00:00'""", con=engine)
df_vader_sem2_2021 = pd.read_sql_query("""SELECT ID, vader_pos as positive, vader_neg as negative, vader_neu as neutral, vader_compound as compound from tirocinio.db_vader_roberta WHERE "created_at" BETWEEN '2021-07-01 00:00:00+00:00' AND '2021-12-31 23:59:59+00:00'""", con=engine)
df_vader_sem1_2022 = pd.read_sql_query("""SELECT ID, vader_pos as positive, vader_neg as negative, vader_neu as neutral, vader_compound as compound from tirocinio.db_vader_roberta WHERE "created_at" BETWEEN '2022-01-01 00:00:00+00:00' AND '2022-06-30 23:59:59+00:00'""", con=engine)
df_vader_sem2_2022 = pd.read_sql_query("""SELECT ID, vader_pos as positive, vader_neg as negative, vader_neu as neutral, vader_compound as compound from tirocinio.db_vader_roberta WHERE "created_at" BETWEEN '2022-07-01 00:00:00+00:00' AND '2022-12-31 23:59:59+00:00'""", con=engine)

df_roberta_sem1_2021 = pd.read_sql_query("""SELECT ID, roberta_pos as positive, roberta_neg as negative, roberta_neu as neutral from tirocinio.db_vader_roberta WHERE "created_at" BETWEEN '2021-01-01 00:00:00+00:00' AND '2021-06-30 23:59:59+00:00'""", con=engine)
df_roberta_sem2_2021 = pd.read_sql_query("""SELECT ID, roberta_pos as positive, roberta_neg as negative, roberta_neu as neutral from tirocinio.db_vader_roberta WHERE "created_at" BETWEEN '2021-07-01 00:00:00+00:00' AND '2021-12-31 23:59:59+00:00'""", con=engine)
df_roberta_sem1_2022 = pd.read_sql_query("""SELECT ID, roberta_pos as positive, roberta_neg as negative, roberta_neu as neutral from tirocinio.db_vader_roberta WHERE "created_at" BETWEEN '2022-01-01 00:00:00+00:00' AND '2022-06-30 23:59:59+00:00'""", con=engine)
df_roberta_sem2_2022 = pd.read_sql_query("""SELECT ID, roberta_pos as positive, roberta_neg as negative, roberta_neu as neutral from tirocinio.db_vader_roberta WHERE "created_at" BETWEEN '2022-07-01 00:00:00+00:00' AND '2022-12-31 23:59:59+00:00'""", con=engine)


dataframes_distilbert = [df_distilbert_sem1_2021, df_distilbert_sem2_2021, df_distilbert_sem1_2022, df_distilbert_sem2_2022]
dataframes_vader = [df_vader_sem1_2021, df_vader_sem2_2021, df_vader_sem1_2022, df_vader_sem2_2022]
dataframes_roberta = [df_roberta_sem1_2021, df_roberta_sem2_2021, df_roberta_sem1_2022, df_roberta_sem2_2022]

semesters = ['Semester 1 2021', 'Semester 2 2021', 'Semester 1 2022', 'Semester 2 2022']

#Distilbert

for i, df in enumerate(dataframes_distilbert):
    emotion_counts = df['first_emotion'].value_counts()

    fig, ax = plt.subplots()
    ax.bar(emotion_counts.index, emotion_counts.values)

    ax.set_xlabel(semesters[i])

    ax.set_title('Distribution of Emotions - {}'.format(semesters[i]))
    ax.set_ylabel('Number of occurrences')

    plt.xticks(rotation=45)

    plt.show()

#Vader

fig, axs = plt.subplots(2, 2, figsize=(12, 8))  # Creazione della griglia di subplot 2x2

for i, df_vader in enumerate(dataframes_vader):
    df_vader['sentiment'] = pd.cut(df_vader['compound'], bins=[-1.0, -0.5, 0.5, 1.0], labels=['negative', 'neutral', 'positive'])

    sentiment_counts = df_vader['sentiment'].value_counts()
    sentiment_percentages = (sentiment_counts / sentiment_counts.sum()) * 100

    ax = axs[i // 2, i % 2]  # Ottieni l'asse corrispondente alla posizione del subplot
    sentiment_percentages.plot(kind='bar', rot=0, ax=ax)
    ax.set_title(f'Sentiment Distribution Vader - {semesters[i]}')
    ax.set_xlabel('Sentiment')
    ax.set_ylabel('Percentages')

    ax.set_xticklabels(ax.get_xticklabels(), rotation=0)
    ax.set_yticks(range(0, int(sentiment_percentages.max()) + 10, 10))
    for p in ax.patches:
        ax.annotate(f'{p.get_height():.1f}%', (p.get_x() + p.get_width() / 2, p.get_height()), ha='center', va='bottom')

plt.tight_layout()  # Opzionale: migliora la disposizione dei subplot
plt.show()

#Roberta

for i, df_roberta in enumerate(dataframes_roberta):
    df_roberta['compound'] = (df_roberta['positive'] - df_roberta['negative']) / (df_roberta['positive'] + df_roberta['negative'] + df_roberta['neutral'])

    df_roberta['sentiment'] = pd.cut(df_roberta['compound'], bins=[-1.0, -0.5, 0.5, 1.0], labels=['negative', 'neutral', 'positive'])

    sentiment_counts = df_roberta['sentiment'].value_counts()
    sentiment_percentages = (sentiment_counts / sentiment_counts.sum()) * 100  # Calcola le percentuali
    ax = sentiment_percentages.plot(kind='bar', rot=0)
    plt.title(f"Sentiment Distribution Roberta - {semesters[i]}")
    plt.xlabel('Sentiment')
    plt.ylabel('Percentages')

    plt.xticks(rotation=0)
    plt.yticks(range(0, int(sentiment_percentages.max()) + 10, 10))
    for p in ax.patches:
        ax.annotate(f'{p.get_height():.1f}%', (p.get_x() + p.get_width() / 2, p.get_height()), ha='center', va='bottom')

    plt.show()


#Differenziale Vader

valori_positivi = []
valori_negativi = []
valori_neutri = []

for df in dataframes_vader:
    df['sentiment'] = pd.cut(df['compound'], bins=[-1.0, -0.5, 0.5, 1.0], labels=['negative', 'neutral', 'positive'])
    positivi = df[df['sentiment'] == 'positive']['positive'].sum()
    negativi = df[df['sentiment'] == 'negative']['negative'].sum()
    neutri = df[df['sentiment'] == 'neutral']['neutral'].sum()

    valori_positivi.append(positivi)
    valori_negativi.append(negativi)
    valori_neutri.append(neutri)

semestri = ['S1 2021', 'S2 2021', 'S1 2022', 'S2 2022']
plt.plot(semestri, valori_positivi, label='positivi')
plt.plot(semestri, valori_negativi, label='negativi')
plt.plot(semestri, valori_neutri, label='neutri')
plt.xticks(semestri)
plt.legend()
plt.show()

#Differenziale Roberta

valori_positivi = []
valori_negativi = []
valori_neutri = []

for df in dataframes_roberta:
    df['compound'] = (df['positive'] - df['negative']) / (df['positive'] + df['negative'] + df['neutral'])
    df['sentiment'] = pd.cut(df['compound'], bins=[-1.0, -0.5, 0.5, 1.0], labels=['negative', 'neutral', 'positive'])
    positivi = df[df['sentiment'] == 'positive']['positive'].sum()
    negativi = df[df['sentiment'] == 'negative']['negative'].sum()
    neutri = df[df['sentiment'] == 'neutral']['neutral'].sum()

    valori_positivi.append(positivi)
    valori_negativi.append(negativi)
    valori_neutri.append(neutri)

semestri = ['S1 2021', 'S2 2021', 'S1 2022', 'S2 2022']
plt.plot(semestri, valori_positivi, label='positivi')
plt.plot(semestri, valori_negativi, label='negativi')
plt.plot(semestri, valori_neutri, label='neutri')
plt.xticks(semestri)
plt.legend()
plt.show()

#Test distilbert

colori_emozioni = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple', 'tab:brown', 'tab:pink', 'tab:gray', 'tab:olive', 'tab:cyan', 'black', 'blue', 'red', 'green', 'orange', 'yellow', 'purple', 'brown', 'pink', 'gray', 'olive', 'cyan', 'magenta', 'gold', 'indigo', 'lime', 'maroon', 'navy']
andamento_emozioni = {}
emozioni = df_distilbert_sem1_2021['first_emotion'].unique()
for emo in emozioni:
    andamento_emozioni[emo] = [0, 0, 0, 0]

for idx, df in enumerate(dataframes_distilbert):
    for _, row in df.iterrows():
        emo = row['first_emotion']
        score = row['scores']
        andamento_emozioni[emo][idx] = score

semestri = ['S1 2021', 'S2 2021', 'S1 2022', 'S2 2022']
for idx, (emo, scores) in enumerate(andamento_emozioni.items()):
    plt.plot(semestri, scores, label=emo, color=colori_emozioni[idx])
    
plt.xticks(semestri)
plt.legend(loc='upper right', bbox_to_anchor=(1.1, 1.0))
plt.show()


#Distilbert con selezione
andamento_emozioni = {}
emozioni_interessanti1 = ['joy', 'sadness', 'surprise', 'love', 'fear', 'anger']
emozioni_interessanti2 = ['disgust', 'excitement', 'nervousness', 'optimism', 'gratitude', 'confusion']
for emo in emozioni_interessanti2:
    andamento_emozioni[emo] = [0, 0, 0, 0]

for idx, df in enumerate(dataframes_distilbert):
    for _, row in df.iterrows():
        emo = row['first_emotion']
        score = row['scores']
        if emo in emozioni_interessanti2:
            andamento_emozioni[emo][idx] = score

semestri = ['S1 2021', 'S2 2021', 'S1 2022', 'S2 2022']
for idx, (emo, scores) in enumerate(andamento_emozioni.items()):
    plt.plot(semestri, scores, label=emo)

plt.title("Temporal Variation of Primary Emotions (DistilBERT)")
plt.xlabel("Semesters")
plt.ylabel("Percentages")    
plt.xticks(semestri)
plt.legend(loc='upper right', bbox_to_anchor=(1.1, 1.0))
plt.show()


#Vader Multibar

semesters = ['Semester 1', 'Semester 2', 'Semester 3', 'Semester 4']
emotions = ['Negative', 'Neutral', 'Positive']
fig, ax = plt.subplots()

width = 0.2  # Larghezza delle barre
x = range(len(emotions))

for i, df_vader in enumerate(dataframes_vader):
    df_vader['sentiment'] = pd.cut(df_vader['compound'], bins=[-1.0, -0.5, 0.5, 1.0], labels=['negative', 'neutral', 'positive'])
    sentiment_counts = df_vader['sentiment'].value_counts()
    sentiment_percentages = (sentiment_counts / sentiment_counts.sum()) * 100

    bars = ax.bar([val + i * width for val in x], sentiment_percentages, width, label=semesters[i])

    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height:.1f}%', xy=(bar.get_x() + bar.get_width() / 2, height), xytext=(0, 3),
                    textcoords="offset points", ha='center', va='bottom')

ax.set_title('Sentiment Analysis Vader')
ax.set_xlabel('Sentiment')
ax.set_ylabel('Percentages')
ax.set_xticks([val + width for val in x])
ax.set_xticklabels(emotions)
ax.legend()

plt.show()

#Roberta Multibar

# Lista dei semestri
semesters = ['Semester 1', 'Semester 2', 'Semester 3', 'Semester 4']

# Definizione delle emozioni
emotions = ['Negative', 'Neutral', 'Positive']

# Creazione della figura e degli assi
fig, ax = plt.subplots()

# Configurazione delle barre multiple
width = 0.2  # Larghezza delle barre
x = range(len(emotions))  # Posizioni delle barre sull'asse x

# Ciclo sui dataset
for i, df_roberta in enumerate(dataframes_roberta):
    df_roberta['compound'] = (df_roberta['positive'] - df_roberta['negative']) / (df_roberta['positive'] + df_roberta['negative'] + df_roberta['neutral'])
    df_roberta['sentiment'] = pd.cut(df_roberta['compound'], bins=[-1.0, -0.5, 0.5, 1.0], labels=['negative', 'neutral', 'positive'])
    sentiment_counts = df_roberta['sentiment'].value_counts()
    sentiment_percentages = (sentiment_counts / sentiment_counts.sum()) * 100

    # Creazione delle barre per ogni semestre
    bars = ax.bar([val + i * width for val in x], sentiment_percentages, width, label=semesters[i])

    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height:.1f}%', xy=(bar.get_x() + bar.get_width() / 2, height), xytext=(0, 3),
                    textcoords="offset points", ha='center', va='bottom')

# Impostazione dei titoli e delle etichette degli assi
ax.set_title('Sentiment Analysis Roberta')
ax.set_xlabel('Sentiment')
ax.set_ylabel('Percentages')

# Configurazione delle etichette sull'asse x
ax.set_xticks([val + width for val in x])
ax.set_xticklabels(emotions)

# Aggiunta della legenda
ax.legend()

# Visualizzazione del grafico
plt.show()
"""
