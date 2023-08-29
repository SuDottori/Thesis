import openai
openai.api_key = "API KEY"
import pandas as pd
import re
import time
import os

# Creazione del DataFrame risultato
result_df = pd.DataFrame(columns=['ID', 'Negative score', 'Neutral score', 'Positive score'])
result_df_noscore = pd.DataFrame(columns=['id','sentiment'])
df1_sem1_2021 = pd.read_csv('D:\VSCode\Campioni ChatGPT\Camp1 Sem1 2021.csv')
df2_sem1_2021 = pd.read_csv('D:\VSCode\Campioni ChatGPT\Camp2 Sem1 2021.csv')
df3_sem1_2021 = pd.read_csv('D:\VSCode\Campioni ChatGPT\Camp3 Sem1 2021.csv')
df1_sem2_2021 = pd.read_csv('D:\VSCode\Campioni ChatGPT\Camp1 Sem2 2021.csv')
df2_sem2_2021 = pd.read_csv('D:\VSCode\Campioni ChatGPT\Camp2 Sem2 2021.csv')
df3_sem2_2021 = pd.read_csv('D:\VSCode\Campioni ChatGPT\Camp3 Sem2 2021.csv')
df1_sem1_2022 = pd.read_csv('D:\VSCode\Campioni ChatGPT\Camp1 Sem1 2022.csv')
df2_sem1_2022 = pd.read_csv('D:\VSCode\Campioni ChatGPT\Camp2 Sem1 2022.csv')
df3_sem1_2022 = pd.read_csv('D:\VSCode\Campioni ChatGPT\Camp3 Sem1 2022.csv')
df1_sem2_2022 = pd.read_csv('D:\VSCode\Campioni ChatGPT\Camp1 Sem2 2022.csv')
df2_sem2_2022 = pd.read_csv('D:\VSCode\Campioni ChatGPT\Camp2 Sem2 2022.csv')
df3_sem2_2022 = pd.read_csv('D:\VSCode\Campioni ChatGPT\Camp3 Sem2 2022.csv')

df= df3_sem2_2022

# Iterazione attraverso il DataFrame originale per l'analisi del sentiment
for index, row in df.iterrows():
    testo = row['text']
    id_originale = str(row['id'])

    # Invia il testo a ChatGPT e restituisce gli score Negativo,Positivo e Neutrale
    prompt = "Svolgi la sentiment analysis per questo testo '" + testo + "' restituendo solo i valori Negativi, Neutrali e Positivi con una precisione a 6 cifre decimali"
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=100  # Numero di token massimo per la risposta
    )
    
    # Esegui l'elaborazione della risposta di ChatGPT
    sentiment_result = response.choices[0].text.strip()
    print(sentiment_result)

    # Analizza il risultato del sentiment
    sentiment_values = re.findall(r'\d+\.\d+', sentiment_result)
    negative = float(sentiment_values[0].replace(',', '.'))
    neutral = float(sentiment_values[1].replace(',', '.'))
    positive = float(sentiment_values[2].replace(',', '.'))
    result_df.loc[index] = [id_originale, negative, neutral, positive]

# Stampare il DataFrame risultato
print(result_df)
result_df.to_csv("chatgpt.csv", index = False)

for index, row in df.iterrows():
    testo = row['text']
    sentiment = row['sentiment']
    id_originale = str(row['id'])

# Invia il testo a ChatGPT e restituisce solo se Positivo,Negativo o Neutral
    #Il primo prompt elabora i sentimenti del testo dato restituendo unicamente il sentimento senza alcuna punteggiatura o parole
    prompt = "Svolgi la sentiment analysis per questo testo "+ testo +" dicendo solo se Positivo,Negativo o Neutrale senza ulteriori parole diverse o punteggiatura"
    #Il secondo prompt chiede di spiegare i sentimenti del sentimento precedentemente elaborato
    prompt = "Spiega il perchè questo testo : '"+ testo +"' sia considerato" + sentiment
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=100,
        temperature=0.5,
        n=1,
        stop=None,
        timeout=10
    )
    print(index)
    sentiment_result = response.choices[0].text.strip()
    sentiment = sentiment_result.replace(',','.')
    result_df_noscore.loc[index] = [id_originale, sentiment]

# Stampare il DataFrame risultato
result_df_noscore['sentiment'] = result_df_noscore['sentiment'].apply(lambda x: re.sub('[^\w\s]', '', x))
os.chdir('DIRECTORY')
result_df_noscore.to_csv("CSV NAME", index = False)
