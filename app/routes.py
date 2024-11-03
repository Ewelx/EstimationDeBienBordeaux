from flask import Blueprint, render_template, jsonify, request
import csv
import os

# Création du blueprint
main_bp = Blueprint('main', __name__)

# Fonction pour charger les villes et prix/m² du CSV
def charger_villes():
    villes = []
    with open('app/static/CSV/communes_filtres.csv', mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            villes.append(row['NOM_COM_M'])
            villes.sort()
    return villes

def algorithme_estimation_bien(ville, type_bien, annee_construction, superficie, nombre_pieces, nombre_etages, etat_general, jardin_terrasse, garage_parking, ascenseur, type_chauffage, proximite, renovations):
    prix_base = None
    with open('app/static/CSV/communes_filtres.csv', mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["NOM_COM_M"] == ville:
                prix_base = float(row["PrixMoyen_M2"])  # Assigner la valeur trouvée
                break

    if type_bien == "maison":
        prix_base *= 1.1  # Exemple d'ajustement pour maison
    elif type_bien == "appartement":
        prix_base *= 0.9

    if annee_construction == "avant_1949":
        prix_base *= 0.8  
    elif annee_construction == "1949_1974":
        prix_base *= 0.9 
    elif annee_construction == "1975_1999":
        prix_base *= 1.0  
    elif annee_construction == "2000_2005":
        prix_base *= 1.1  
    elif annee_construction == "2006_2012":
        prix_base *= 1.15  
    elif annee_construction == "2013_2018":
        prix_base *= 1.2  
    elif annee_construction == "apres_2018":
        prix_base *= 1.25

    nombre_pieces = int(nombre_pieces)

    if nombre_pieces > 1:
        prix_base *= 1 + 0.005 * (nombre_pieces - 1) 

    nombre_etages = int(nombre_etages)

    if nombre_etages > 1:
        prix_base *= 1 + 0.003 * (nombre_etages - 1)

    if etat_general == "neuf":
        prix_base *= 1.2  
    elif etat_general == "bon":
        prix_base *= 1.1  
    elif etat_general == "a_renover":
        prix_base *= 0.85 

    if jardin_terrasse == "oui":
        prix_base *= 1.1 

    if garage_parking == "oui":
        prix_base *= 1.1

    if ascenseur == "oui":
        prix_base *= 1.1  # Augmenter le prix de 10% si ascenseur présent

    # Ajustement pour le type de chauffage
    if type_chauffage == "gaz":
        prix_base *= 1.05  # Augmenter le prix de 5% pour chauffage au gaz
    elif type_chauffage == "electrique":
        prix_base *= 1.02  # Augmenter le prix de 2% pour chauffage électrique
    elif type_chauffage == "fioul":
        prix_base *= 1.03  # Augmenter le prix de 3% pour chauffage au fioul
    elif type_chauffage == "bois":
        prix_base *= 1.04  # Augmenter le prix de 4% pour chauffage au bois

    # Ajustement pour la proximité des commodités
    if proximite == "commerces":
        prix_base *= 1.05  # Augmenter le prix de 5% pour proximité des commerces
    elif proximite == "transports":
        prix_base *= 1.07  # Augmenter le prix de 7% pour proximité des transports
    elif proximite == "ecoles":
        prix_base *= 1.06  # Augmenter le prix de 6% pour proximité des écoles
    elif proximite == "parcs":
        prix_base *= 1.04  # Augmenter le prix de 4% pour proximité des parcs

    # Ajustement pour les rénovations récentes
    if renovations == "oui":
        prix_base *= 1.1
    
    prix_estime = int(superficie) * prix_base
    return prix_estime

# Définir une route pour la page d'accueil
@main_bp.route('/')
def home():
    return render_template('index.html')


# Définir une route pour la page estimerbien
@main_bp.route('/estimerbien', methods=['POST', 'GET'])
def estimerbien():
    villes = charger_villes()
    if request.method == 'POST':
        data = request.form  
        ville = data.get('ville')
        type_bien = data.get('type_bien')
        annee_construction = data.get('annee_construction')
        superficie = data.get('superficie')
        nombre_pieces = data.get('nombre_pieces')
        nombre_etages = data.get('nombre_etages')
        etat_general = data.get('etat_general')
        jardin_terrasse = data.get('jardin_terrasse')
        garage_parking = data.get('garage_parking')
        ascenseur = data.get('ascenseur')
        type_chauffage = data.get('type_chauffage')
        proximite = data.get('proximite')
        renovations = data.get('renovations')

        # Appeler l'algorithme d'estimation
        prix_estime = algorithme_estimation_bien(
            ville, type_bien, annee_construction, superficie, nombre_pieces,
            nombre_etages, etat_general, jardin_terrasse, garage_parking,
            ascenseur, type_chauffage, proximite, renovations
        )

        return render_template('estimerbien.html', villes=villes, prix_estime=int(prix_estime))
    return render_template('estimerbien.html', villes=villes, prix_estime=None)

# Définir une route pour la page map
@main_bp.route('/map')
def map():
    return render_template('map.html')


