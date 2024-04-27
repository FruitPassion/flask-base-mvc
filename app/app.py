#!/.venv/bin/python3
import os
import sys

from app.utils import manage_requirements


def create_app(config=None):
    from flask import Flask
    from flask_session import Session
    from flask_wtf import CSRFProtect
    from utils import app_utils
    from utils.manage_config import check_config, read_config
    from utils.manage_error import LogOpeningError

    # Check if a configuration is requested
    # If not, the default configuration is used
    CONFIG_FILE = "config.txt"
    check_config(config)
    if not os.path.exists(CONFIG_FILE):
        file = open(CONFIG_FILE, "w")
        file.close()
    with open(CONFIG_FILE, "w") as file:
        file.write(config)

    config = read_config(CONFIG_FILE)

    # Database import
    from model.shared_model import db

    # Application creation
    app = Flask(__name__, template_folder="view", static_folder="static")

    # Reset logs files
    if open("logs/error.log", "w").close():
        raise LogOpeningError("Impossible d'ouvrir le fichier de log")
    if open("logs/access.log", "w").close():
        raise LogOpeningError("Impossible d'ouvrir le fichier de log")

    # Chargement de la configuration dev ou prod
    app.config.from_object(f"config.{config.capitalize()}Config")

    # Import controller
    # from controller.auth import auth

    # Controller registration
    # app.register_blueprint(auth)

    # CRSF protection activation
    csrf = CSRFProtect()
    csrf.init_app(app)

    # Database initialization
    db.init_app(app)

    Session(app)

    # Redefine the url_for function to add a timestamp
    app_utils.rewrite_url(app)

    # Error handler
    app_utils.error_handler(app, config)

    if config == "test":
        with app.app_context():
            db.create_all()

    # Return the application
    return app


# Appel principal pour lancer l'application
if __name__ == "__main__":
    try:
        manage_requirements.checking()
        create_app(sys.argv[1]).run(host="0.0.0.0")
    except IndexError:
        raise ValueError("Argument de lancement manquant (dev, test ou prod)")
