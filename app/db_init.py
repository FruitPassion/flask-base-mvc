#!../.venv/bin/python3

from app import create_app

app = create_app("dev")
with app.app_context():
    from model.shared_model import db

    db.create_all()
