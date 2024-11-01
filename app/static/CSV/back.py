import pandas as pd
import requests

df = pd.read_csv('CSV/communes_filtres.csv', sep=",")

# Estime un bien
def algorithme_estimation_bien(ville, surface):    
    ville_info = df[df['NOM_COM_M'].str.contains(ville, case=False, na=False)]
    
    if not ville_info.empty:
        prix_m2 = ville_info.iloc[0]['PrixMoyen_M2']
        estimation = prix_m2 * surface
        return f"L'estimation du prix pour {surface} m² à {ville} est de {estimation:.2f} euros."
    else:
        return f"Ville {ville} non trouvée dans la base de données."

# Obtient les coordonnés d'une ville selon son nom
def get_lat_lon(city_name):
    url = f"https://nominatim.openstreetmap.org/search?q={city_name}&format=json&limit=1"
    response = requests.get(url)
    if response:
        data = response.json()
        lat = data[0]['lat']
        lon = data[0]['lon']
        return lat, lon
    return None, None