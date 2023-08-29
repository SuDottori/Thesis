import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df1_sem1_2021 = pd.read_csv('D:\VSCode\Campioni ChatGPT\Risultati solo id\Camp1 Sem1 2021.csv')
df2_sem1_2021 = pd.read_csv('D:\VSCode\Campioni ChatGPT\Risultati solo id\Camp2 Sem1 2021.csv')
df3_sem1_2021 = pd.read_csv('D:\VSCode\Campioni ChatGPT\Risultati solo id\Camp3 Sem1 2021.csv')
df1_sem2_2021 = pd.read_csv('D:\VSCode\Campioni ChatGPT\Risultati solo id\Camp1 Sem2 2021.csv')
df2_sem2_2021 = pd.read_csv('D:\VSCode\Campioni ChatGPT\Risultati solo id\Camp2 Sem2 2021.csv')
df3_sem2_2021 = pd.read_csv('D:\VSCode\Campioni ChatGPT\Risultati solo id\Camp3 Sem2 2021.csv')
df1_sem1_2022 = pd.read_csv('D:\VSCode\Campioni ChatGPT\Risultati solo id\Camp1 Sem1 2022.csv')
df2_sem1_2022 = pd.read_csv('D:\VSCode\Campioni ChatGPT\Risultati solo id\Camp2 Sem1 2022.csv')
df3_sem1_2022 = pd.read_csv('D:\VSCode\Campioni ChatGPT\Risultati solo id\Camp3 Sem1 2022.csv')
df1_sem2_2022 = pd.read_csv('D:\VSCode\Campioni ChatGPT\Risultati solo id\Camp1 Sem2 2022.csv')
df2_sem2_2022 = pd.read_csv('D:\VSCode\Campioni ChatGPT\Risultati solo id\Camp2 Sem2 2022.csv')
df3_sem2_2022 = pd.read_csv('D:\VSCode\Campioni ChatGPT\Risultati solo id\Camp3 Sem2 2022.csv')

import pandas as pd
import matplotlib.pyplot as plt


#df1,df2,df3 uniti e differenze mostrate per semestre

# DataFrames for each semester
df_sem1_2021 = pd.concat([df1_sem1_2021, df2_sem1_2021, df3_sem1_2021])
df_sem2_2021 = pd.concat([df1_sem2_2021, df2_sem2_2021, df3_sem2_2021])
df_sem1_2022 = pd.concat([df1_sem1_2022, df2_sem1_2022, df3_sem1_2022])
df_sem2_2022 = pd.concat([df1_sem2_2022, df2_sem2_2022, df3_sem2_2022])

# Calculating the percentage of sentiment for each semester
sentiment_sem1_2021 = df_sem1_2021['sentiment'].value_counts(normalize=True) * 100
sentiment_sem2_2021 = df_sem2_2021['sentiment'].value_counts(normalize=True) * 100
sentiment_sem1_2022 = df_sem1_2022['sentiment'].value_counts(normalize=True) * 100
sentiment_sem2_2022 = df_sem2_2022['sentiment'].value_counts(normalize=True) * 100

# Creating the data for the multibar chart
semesters = ['Sem1 2021', 'Sem2 2021', 'Sem1 2022', 'Sem2 2022']
positive_sentiment = [sentiment_sem1_2021.get('Positivo', 0), sentiment_sem2_2021.get('Positivo', 0),
                      sentiment_sem1_2022.get('Positivo', 0), sentiment_sem2_2022.get('Positivo', 0)]
negative_sentiment = [sentiment_sem1_2021.get('Negativo', 0), sentiment_sem2_2021.get('Negativo', 0),
                      sentiment_sem1_2022.get('Negativo', 0), sentiment_sem2_2022.get('Negativo', 0)]
neutral_sentiment = [sentiment_sem1_2021.get('Neutrale', 0), sentiment_sem2_2021.get('Neutrale', 0),
                     sentiment_sem1_2022.get('Neutrale', 0), sentiment_sem2_2022.get('Neutrale', 0)]

# Creating the multibar chart
bar_width = 0.2
positions = range(len(semesters))

plt.bar([p - bar_width for p in positions], positive_sentiment, bar_width, label='Positive')
plt.bar(positions, negative_sentiment, bar_width, label='Negative')
plt.bar([p + bar_width for p in positions], neutral_sentiment, bar_width, label='Neutral')

# Add percentage labels above each bar
for i, pos in enumerate(positions):
    plt.text(pos - bar_width, positive_sentiment[i], f'{positive_sentiment[i]:.2f}%', ha='center', va='bottom')
    plt.text(pos, negative_sentiment[i], f'{negative_sentiment[i]:.2f}%', ha='center', va='bottom')
    plt.text(pos + bar_width, neutral_sentiment[i], f'{neutral_sentiment[i]:.2f}%', ha='center', va='bottom')

plt.xlabel('Semester')
plt.ylabel('Percentage')
plt.title('Sentiment Analysis by Semester')
plt.xticks(positions, semesters)
plt.legend()
plt.show()



#Sem1 2021 differenze tra i campioni

# Calculation of sentiment percentages for each dataframe in the first semester
df1_sem1_sentiment = df1_sem1_2021['sentiment'].value_counts(normalize=True) * 100
df2_sem1_sentiment = df2_sem1_2021['sentiment'].value_counts(normalize=True) * 100
df3_sem1_sentiment = df3_sem1_2021['sentiment'].value_counts(normalize=True) * 100

# Creating the data for the multibar chart
labels = ['Positive', 'Negative', 'Neutral']
df1_percentages = [df1_sem1_sentiment['Positivo'], df1_sem1_sentiment['Negativo'], df1_sem1_sentiment['Neutrale']]
df2_percentages = [df2_sem1_sentiment['Positivo'], df2_sem1_sentiment['Negativo'], df2_sem1_sentiment['Neutrale']]
df3_percentages = [df3_sem1_sentiment['Positivo'], df3_sem1_sentiment['Negativo'], df3_sem1_sentiment['Neutrale']]

# Creating the multibar chart
x = range(len(labels))
width = 0.2

plt.bar(x, df1_percentages, width, label='df1')
plt.bar([i + width for i in x], df2_percentages, width, label='df2')
plt.bar([i + 2 * width for i in x], df3_percentages, width, label='df3')

# Adding percentage labels above the bars
for i in x:
    plt.text(i, df1_percentages[i], f'{df1_percentages[i]:.2f}%', ha='center', va='bottom')
    plt.text(i + width, df2_percentages[i], f'{df2_percentages[i]:.2f}%', ha='center', va='bottom')
    plt.text(i + 2 * width, df3_percentages[i], f'{df3_percentages[i]:.2f}%', ha='center', va='bottom')

plt.xlabel('Sentiment')
plt.ylabel('Percentage')
plt.title('Sentiment Analysis - Sem1 2021')
plt.xticks([i + width for i in x], labels)
plt.legend()
plt.show()

#Sem2 2021 differenze tra i campioni

# Calculation of sentiment percentages for each dataframe in the first semester
df1_sem2_sentiment = df1_sem2_2021['sentiment'].value_counts(normalize=True) * 100
df2_sem2_sentiment = df2_sem2_2021['sentiment'].value_counts(normalize=True) * 100
df3_sem2_sentiment = df3_sem2_2021['sentiment'].value_counts(normalize=True) * 100

# Creating the data for the multibar chart
labels = ['Positive', 'Negative', 'Neutral']
df1_percentages = [df1_sem2_sentiment['Positivo'], df1_sem2_sentiment['Negativo'], df1_sem2_sentiment['Neutrale']]
df2_percentages = [df2_sem2_sentiment['Positivo'], df2_sem2_sentiment['Negativo'], df2_sem2_sentiment['Neutrale']]
df3_percentages = [df3_sem2_sentiment['Positivo'], df3_sem2_sentiment['Negativo'], df3_sem2_sentiment['Neutrale']]

# Creating the multibar chart
x = range(len(labels))
width = 0.2

plt.bar(x, df1_percentages, width, label='df1')
plt.bar([i + width for i in x], df2_percentages, width, label='df2')
plt.bar([i + 2 * width for i in x], df3_percentages, width, label='df3')

# Adding percentage labels above the bars
for i in x:
    plt.text(i, df1_percentages[i], f'{df1_percentages[i]:.2f}%', ha='center', va='bottom')
    plt.text(i + width, df2_percentages[i], f'{df2_percentages[i]:.2f}%', ha='center', va='bottom')
    plt.text(i + 2 * width, df3_percentages[i], f'{df3_percentages[i]:.2f}%', ha='center', va='bottom')

plt.xlabel('Sentiment')
plt.ylabel('Percentage')
plt.title('Sentiment Analysis - Sem2 2021')
plt.xticks([i + width for i in x], labels)
plt.legend()
plt.show()

#Sem1 2022 differenze tra i campioni

# Calculation of sentiment percentages for each dataframe in the first semester
df1_sem1_sentiment = df1_sem1_2022['sentiment'].value_counts(normalize=True) * 100
df2_sem1_sentiment = df2_sem1_2022['sentiment'].value_counts(normalize=True) * 100
df3_sem1_sentiment = df3_sem1_2022['sentiment'].value_counts(normalize=True) * 100

# Creating the data for the multibar chart
labels = ['Positive', 'Negative', 'Neutral']
df1_percentages = [df1_sem1_sentiment['Positivo'], df1_sem1_sentiment['Negativo'], df1_sem1_sentiment['Neutrale']]
df2_percentages = [df2_sem1_sentiment['Positivo'], df2_sem1_sentiment['Negativo'], df2_sem1_sentiment['Neutrale']]
df3_percentages = [df3_sem1_sentiment['Positivo'], df3_sem1_sentiment['Negativo'], df3_sem1_sentiment['Neutrale']]

# Creating the multibar chart
x = range(len(labels))
width = 0.2

plt.bar(x, df1_percentages, width, label='df1')
plt.bar([i + width for i in x], df2_percentages, width, label='df2')
plt.bar([i + 2 * width for i in x], df3_percentages, width, label='df3')

# Adding percentage labels above the bars
for i in x:
    plt.text(i, df1_percentages[i], f'{df1_percentages[i]:.2f}%', ha='center', va='bottom')
    plt.text(i + width, df2_percentages[i], f'{df2_percentages[i]:.2f}%', ha='center', va='bottom')
    plt.text(i + 2 * width, df3_percentages[i], f'{df3_percentages[i]:.2f}%', ha='center', va='bottom')

plt.xlabel('Sentiment')
plt.ylabel('Percentage')
plt.title('Sentiment Analysis - Sem1 2022')
plt.xticks([i + width for i in x], labels)
plt.legend()
plt.show()


#Sem2 2022 differenze tra i campioni

# Calculation of sentiment percentages for each dataframe in the first semester
df1_sem2_sentiment = df1_sem2_2022['sentiment'].value_counts(normalize=True) * 100
df2_sem2_sentiment = df2_sem2_2022['sentiment'].value_counts(normalize=True) * 100
df3_sem2_sentiment = df3_sem2_2022['sentiment'].value_counts(normalize=True) * 100

# Creating the data for the multibar chart
labels = ['Positive', 'Negative', 'Neutral']
df1_percentages = [df1_sem2_sentiment['Positivo'], df1_sem2_sentiment['Negativo'], df1_sem2_sentiment['Neutrale']]
df2_percentages = [df2_sem2_sentiment['Positivo'], df2_sem2_sentiment['Negativo'], df2_sem2_sentiment['Neutrale']]
df3_percentages = [df3_sem2_sentiment['Positivo'], df3_sem2_sentiment['Negativo'], df3_sem2_sentiment['Neutrale']]

# Creating the multibar chart
x = range(len(labels))
width = 0.2

plt.bar(x, df1_percentages, width, label='df1')
plt.bar([i + width for i in x], df2_percentages, width, label='df2')
plt.bar([i + 2 * width for i in x], df3_percentages, width, label='df3')

# Adding percentage labels above the bars
for i in x:
    plt.text(i, df1_percentages[i], f'{df1_percentages[i]:.2f}%', ha='center', va='bottom')
    plt.text(i + width, df2_percentages[i], f'{df2_percentages[i]:.2f}%', ha='center', va='bottom')
    plt.text(i + 2 * width, df3_percentages[i], f'{df3_percentages[i]:.2f}%', ha='center', va='bottom')

plt.xlabel('Sentiment')
plt.ylabel('Percentage')
plt.title('Sentiment Analysis - Sem2 2022')
plt.xticks([i + width for i in x], labels)
plt.legend()
plt.show()
