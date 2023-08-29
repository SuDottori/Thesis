import pandas as pd
import os

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

df1_ris_sem1_2021 = pd.read_csv('D:\VSCode\Campioni ChatGPT\Risultati solo id\Camp1 Sem1 2021.csv')
df2_ris_sem1_2021 = pd.read_csv('D:\VSCode\Campioni ChatGPT\Risultati solo id\Camp2 Sem1 2021.csv')
df3_ris_sem1_2021 = pd.read_csv('D:\VSCode\Campioni ChatGPT\Risultati solo id\Camp3 Sem1 2021.csv')
df1_ris_sem2_2021 = pd.read_csv('D:\VSCode\Campioni ChatGPT\Risultati solo id\Camp1 Sem2 2021.csv')
df2_ris_sem2_2021 = pd.read_csv('D:\VSCode\Campioni ChatGPT\Risultati solo id\Camp2 Sem2 2021.csv')
df3_ris_sem2_2021 = pd.read_csv('D:\VSCode\Campioni ChatGPT\Risultati solo id\Camp3 Sem2 2021.csv')
df1_ris_sem1_2022 = pd.read_csv('D:\VSCode\Campioni ChatGPT\Risultati solo id\Camp1 Sem1 2022.csv')
df2_ris_sem1_2022 = pd.read_csv('D:\VSCode\Campioni ChatGPT\Risultati solo id\Camp2 Sem1 2022.csv')
df3_ris_sem1_2022 = pd.read_csv('D:\VSCode\Campioni ChatGPT\Risultati solo id\Camp3 Sem1 2022.csv')
df1_ris_sem2_2022 = pd.read_csv('D:\VSCode\Campioni ChatGPT\Risultati solo id\Camp1 Sem2 2022.csv')
df2_ris_sem2_2022 = pd.read_csv('D:\VSCode\Campioni ChatGPT\Risultati solo id\Camp2 Sem2 2022.csv')
df3_ris_sem2_2022 = pd.read_csv('D:\VSCode\Campioni ChatGPT\Risultati solo id\Camp3 Sem2 2022.csv')

df1= df3_sem2_2022
df2= df3_ris_sem2_2022

merged_df = df1.merge(df2, on='id')
merged_df=merged_df[['id','sentiment','text']]
os.chdir('DIRECTORY')
merged_df.to_csv("CSV NAME", index = False)

