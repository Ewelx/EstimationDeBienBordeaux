from flask import Flask

def create_app():
    # Crée l'instance de l'application Flask
    app = Flask(__name__)

    # Configuration de l'application (importe les paramètres depuis le fichier config.py)
    app.config.from_object('config')

    # Importation des routes (blueprint)
    from .routes import main_bp 
    app.register_blueprint(main_bp)

    return app
