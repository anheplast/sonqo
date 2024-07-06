from sonqo import db
from flask import url_for
from datetime import datetime
from flask_bcrypt import generate_password_hash
from sqlalchemy import Text


class User(db.Model):
    __tablename__ = 'tb_sesiones'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(128), nullable=False)
    rol = db.Column(db.String(20), nullable=False)


class Consejo(db.Model):
    __tablename__ = 'tb_consejos'
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(255), nullable=False)
    descripcion = db.Column(Text, nullable=False)
    detalles = db.Column(Text, nullable=False)
    imagen_url = db.Column(db.String(500), nullable=False)


class Actividad(db.Model):
    __tablename__ = 'tb_actividades'
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(255), nullable=False)
    descripcion = db.Column(db.Text, nullable=True)
    imagen_url = db.Column(db.String(1024), nullable=True)
    video_url = db.Column(db.String(1024), nullable=True)


    

class Cancion(db.Model):
    __tablename__ = 'tb_canciones'
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    artista = db.Column(db.String(100), nullable=False)
    nombre_archivo = db.Column(db.String(255), nullable=False)
    fecha_creacion = db.Column(db.TIMESTAMP, default=datetime.utcnow, nullable=False)

    @property
    def song_url(self):
        return url_for('static', filename=f'uploads/{self.nombre_archivo}')



    

