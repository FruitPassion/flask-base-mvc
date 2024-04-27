import os

from utils.manage_config import read_config
from utils.manage_logs import gestion_logs

config = read_config("config.txt")

basedir = os.path.abspath(os.path.dirname(__file__))


gestion_logs()


class DevConfig:
    """
    Development configuration
    """

    SECRET_KEY = "password"
    ENVIRONMENT = "development"
    FLASK_APP = "app"
    DEBUG = True
    SESSION_PERMANENT = False
    SESSION_TYPE = "filesystem"
    WTF_CSRF_ENABLED = False
    DB_SCHEMA = f"db_{config.lower()}"
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "database.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    REMEMBER_COOKIE_SAMESITE = "strict"
    SQLALCHEMY_ENGINE_OPTIONS = {
        "pool_pre_ping": True,
    }


class ProdConfig:
    """
    Production configuration
    """

    SECRET_KEY = os.urandom(32)
    ENVIRONMENT = "production"
    FLASK_APP = "app"
    WTF_CSRF_ENABLED = True
    DEBUG = False
    SESSION_PERMANENT = False
    SESSION_TYPE = "filesystem"
    SESSION_USE_SIGNER = True
    DB_SCHEMA = f"db_{config.lower()}"
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "database.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    REMEMBER_COOKIE_SAMESITE = "strict"
    SQLALCHEMY_ENGINE_OPTIONS = {
        "pool_pre_ping": True,
    }
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = "Lax"


class TestConfig:
    """
    Test configuration
    """

    SECRET_KEY = "password"
    ENVIRONMENT = "test"
    FLASK_APP = "app"
    WTF_CSRF_ENABLED = False
    DEBUG = True
    SESSION_PERMANENT = False
    SESSION_TYPE = "filesystem"
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    REMEMBER_COOKIE_SAMESITE = "strict"
    SQLALCHEMY_ENGINE_OPTIONS = {
        "pool_pre_ping": True,
    }
