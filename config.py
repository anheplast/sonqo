import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'una_llave_secreta'
    SQLALCHEMY_DATABASE_URI = 'postgresql://mapple:J_%40nte0L@localhost/db_sonqo'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

