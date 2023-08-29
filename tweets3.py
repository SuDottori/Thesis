import pandas as pd

df = pd.read_csv('CSV NAME')
df = df.drop_duplicates(subset=["Id"])
df.to_csv('CSV NAME',encoding='utf-8', index=False)
