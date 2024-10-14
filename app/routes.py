from flask import Blueprint, render_template

# Création du blueprint
main_bp = Blueprint('main', __name__)

# Définir une route pour la page d'accueil
@main_bp.route('/')
def home():
    return render_template('index.html')


# Définir une route pour la page estimerbien
@main_bp.route('/estimerbien')
def estimerbien():
    return render_template('estimerbien.html')

# Définir une route pour la page map
@main_bp.route('/map')
def map():
    return render_template('map.html')


