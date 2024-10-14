import pandas as pd

# Charger le CSV avec le bon séparateur
df = pd.read_csv('CSV/communes_filtres.csv', sep=',')

# Afficher les noms des colonnes pour vérifier
print(df.columns)

ville_counts = df['NOM_COM_M'].value_counts()

for ville, count in ville_counts.items():
    print(f"Ville: {ville}, Nombre d'apparitions: {count}")
