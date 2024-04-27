from flask_sqlalchemy import SQLAlchemy
from utils.manage_config import read_config

db = SQLAlchemy()

config = read_config("config.txt")

DB_SCHEMA = "main"
