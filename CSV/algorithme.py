import pandas as pd

def algorithme_estimation_bien(ville, surface):
    df = pd.read_csv('CSV/dvf-communes-2019.csv', sep=";")
    
    ville_info = df[df['NOM_COM_M'].str.contains(ville, case=False, na=False)]
    
    if not ville_info.empty:
        prix_m2 = ville_info.iloc[0]['PrixMoyen_M2']
        estimation = prix_m2 * surface
        return f"L'estimation du prix pour {surface} m² à {ville} est de {estimation:.2f} euros."
    else:
        return f"Ville {ville} non trouvée dans la base de données."

ville = "Bordeaux"
surface = 500
print(algorithme_estimation_bien(ville, surface))
