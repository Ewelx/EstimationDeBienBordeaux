import pandas as pd

df = pd.read_csv('CSV/dvf-communes-2019.csv', sep=";")
print(df.head())
condition = df['INSEE_DEP'] != "33"
df_filtered = df[~condition]
df_filtered.to_csv('CSV/communes_filtres.csv', index=False)

print("Lignes supprimées selon la condition.")
