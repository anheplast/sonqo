from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from sonqo.config import Config

# Crear la aplicación Flask
app = Flask(__name__, static_url_path='/static')

# Configurar la aplicación Flask usando la clase Config de config.py
app.config.from_object(Config)

# Inicializar las extensiones SQLAlchemy y Bcrypt
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

# Importar las rutas después de inicializar las extensiones
from sonqo import routes

