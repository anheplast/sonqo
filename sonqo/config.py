import os
from flask_sqlalchemy import SQLAlchemy

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'yw/CtFLiui8U9j0CKbZuBo0rgjn+vRCWaY7GZq87nA0='
    SQLALCHEMY_DATABASE_URI = 'postgresql://mapple:J_%40nte0L@localhost/db_sonqo'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

