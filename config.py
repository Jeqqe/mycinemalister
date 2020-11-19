

class Config:

    DEBUG = True

    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://admin:pass123@localhost/cinemalister"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SECRET_KEY = "super-secret-key"
    JWT_ERROR_MESSAGE = "message"

    JWT_BLACKLIST_ENABLED = True
    JWT_BLACKLIST_TOKEN_CHECKS = ['access', 'refresh']
