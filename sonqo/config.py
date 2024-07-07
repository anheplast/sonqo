import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'una_llave_secreta'
    SQLALCHEMY_DATABASE_URI = 'postgresql://mapple:J_%40nte0L@localhost/db_sonqo'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'sonqo/static/uploads')
    MAX_CONTENT_LENGTH = 36 * 1024 * 1024  # Tamaño del archivo de 36 MB

    
