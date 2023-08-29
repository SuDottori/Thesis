import pandas as pd
import openai
# Set up the ChatGPT API credentials
openai.api_key = 'CHIAVE API'

# Load the CSV files containing the tweets
df1_sem1_2021 = pd.read_csv('D:\VSCode\Campioni ChatGPT\Risultati con testo\Camp1 Sem1 2021.csv')
df2_sem1_2021 = pd.read_csv('D:\VSCode\Campioni ChatGPT\Risultati con testo\Camp2 Sem1 2021.csv')
df3_sem1_2021 = pd.read_csv('D:\VSCode\Campioni ChatGPT\Risultati con testo\Camp3 Sem1 2021.csv')
df1_sem2_2021 = pd.read_csv('D:\VSCode\Campioni ChatGPT\Risultati con testo\Camp1 Sem2 2021.csv')
df2_sem2_2021 = pd.read_csv('D:\VSCode\Campioni ChatGPT\Risultati con testo\Camp2 Sem2 2021.csv')
df3_sem2_2021 = pd.read_csv('D:\VSCode\Campioni ChatGPT\Risultati con testo\Camp3 Sem2 2021.csv')
df1_sem1_2022 = pd.read_csv('D:\VSCode\Campioni ChatGPT\Risultati con testo\Camp1 Sem1 2022.csv')
df2_sem1_2022 = pd.read_csv('D:\VSCode\Campioni ChatGPT\Risultati con testo\Camp2 Sem1 2022.csv')
df3_sem1_2022 = pd.read_csv('D:\VSCode\Campioni ChatGPT\Risultati con testo\Camp3 Sem1 2022.csv')
df1_sem2_2022 = pd.read_csv('D:\VSCode\Campioni ChatGPT\Risultati con testo\Camp1 Sem2 2022.csv')
df2_sem2_2022 = pd.read_csv('D:\VSCode\Campioni ChatGPT\Risultati con testo\Camp2 Sem2 2022.csv')
df3_sem2_2022 = pd.read_csv('D:\VSCode\Campioni ChatGPT\Risultati con testo\Camp3 Sem2 2022.csv')

#Positive Tweet explanation
#Concatenate the positive tweets into a single string
positive_tweets = pd.concat([df1_sem1_2021,df2_sem1_2021,df3_sem1_2021,df1_sem2_2021,df2_sem2_2021,df3_sem2_2021,
                             df1_sem2_2021,df2_sem2_2021,df3_sem2_2021,df1_sem1_2022,df2_sem1_2022,df3_sem1_2022,
                             df1_sem2_2022,df1_sem2_2022,df3_sem2_2022])
positive_tweets = positive_tweets[positive_tweets['sentiment'] == 'Positivo']
positive_tweets_text = ' '.join(positive_tweets['text'])
#Create the prompt
prompt = """Spiega il motivo per cui tutti questi tweet sono positivi in una sintesi complessiva basata 
sugli eventi avvenuti con il COVID-19 tra l'inizio del 2021 e la fine del 2022:\n\n"""
prompt += positive_tweets_text
#Request an explanation from ChatGPT
response = openai.Completion.create(
    engine='text-davinci-003',
    prompt=prompt,
    max_tokens=1000
)
explanation = response.choices[0].text.strip()
#Print the explanation
print(explanation)

#Negative Tweet explanation
#Concatenate the negative tweets into a single string
negative_tweets = pd.concat([df1_sem1_2021,df2_sem1_2021,df3_sem1_2021,df1_sem2_2021,df2_sem2_2021,df3_sem2_2021,
                             df1_sem2_2021,df2_sem2_2021,df3_sem2_2021,df1_sem1_2022,df2_sem1_2022,df3_sem1_2022,
                             df1_sem2_2022,df1_sem2_2022,df3_sem2_2022])
negative_tweets = negative_tweets[negative_tweets['sentiment'] == 'Negativo']
negative_tweets_text = ' '.join(negative_tweets['text'])
#Create the prompt
prompt = """Spiega il motivo per cui tutti questi tweet sono negativi in una sintesi complessiva basata 
sugli eventi avvenuti con il COVID-19 tra l'inizio del 2021 e la fine del 2022:\n\n"""
prompt += negative_tweets_text
#Request an explanation from ChatGPT
response = openai.Completion.create(
    engine='text-davinci-003',
    prompt=prompt,
    max_tokens=1000
)
explanation = response.choices[0].text.strip()
#Print the explanation
print(explanation)

#Neutral Tweet explanation
#Concatenate the negative tweets into a single string
neutral_tweets = pd.concat([df1_sem1_2021,df2_sem1_2021,df3_sem1_2021,df1_sem2_2021,df2_sem2_2021,df3_sem2_2021,
                            df1_sem2_2021,df2_sem2_2021,df3_sem2_2021,df1_sem1_2022,df2_sem1_2022,df3_sem1_2022,
                            df1_sem2_2022,df1_sem2_2022,df3_sem2_2022])
neutral_tweets = neutral_tweets[neutral_tweets['sentiment'] == 'Neutrale']
neutral_tweets_text = ' '.join(neutral_tweets['text'])
#Create the prompt
prompt = """Spiega il motivo per cui tutti questi tweet sono neutrali in una sintesi complessiva basata 
sugli eventi avvenuti con il COVID-19 tra l'inizio del 2021 e la fine del 2022:\n\n"""
prompt += neutral_tweets_text
#Request an explanation from ChatGPT
response = openai.Completion.create(
    engine='text-davinci-003',
    prompt=prompt,
    max_tokens=1000
)
explanation = response.choices[0].text.strip()
#Print the explanation
print(explanation)