import pandas as pd
import back

def filtrage_communes():
    df = pd.read_csv('CSV/dvf-communes-2019.csv', sep=";")
    print(df.head())
    condition = df['INSEE_DEP'] != "33"
    df_filtered = df[~condition]
    df_filtered.to_csv('CSV/communes_filtres.csv', index=False)

def filtrage_coord():
    df = pd.read_csv('CSV/communes_filtres.csv', sep=",")
    df['LATITUDE'] = None
    df['LONGITUDE'] = None
    for index, row in df.iterrows():
        ville = row['NOM_COM_M']
        lat, lon = back.get_lat_lon(ville)
        if lat is not None and lon is not None:
            df.at[index, 'LATITUDE'] = str(lat)
            df.at[index, 'LONGITUDE'] = str(lon)
        else:
            df.at[index, 'LATITUDE'] = "Null"
            df.at[index, 'LONGITUDE'] = "Null"

    df.to_csv('CSV/communes_filtres.csv', sep=",", index=False)

filtrage_coord()
