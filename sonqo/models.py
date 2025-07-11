from sonqo import db
from flask import url_for
from datetime import datetime
from flask_bcrypt import generate_password_hash
from sqlalchemy import Text

# Modelo sesiones------------------------------------------------------------------------
class User(db.Model):
    __tablename__ = 'tb_sesiones'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(128), nullable=False)
    rol = db.Column(db.String(20), nullable=False)
#---------------------------------------------------------------------------------------

# Modelo Consejos-----------------------------------------------------------------------
class Consejo(db.Model):
    __tablename__ = 'tb_consejos'
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(255), nullable=False)
    descripcion = db.Column(Text, nullable=False)
    detalles = db.Column(Text, nullable=False)
    imagen_url = db.Column(db.String(500), nullable=False)
#---------------------------------------------------------------------------------------

# Modelo Actividad----------------------------------------------------------------------
class Actividad(db.Model):
    __tablename__ = 'tb_actividades'
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(255), nullable=False)
    descripcion = db.Column(db.Text, nullable=True)
    imagen_url = db.Column(db.String(1024), nullable=True)
    video_url = db.Column(db.String(1024), nullable=True)
#--------------------------------------------------------------------------------------

    
# Modelo Cancion-----------------------------------------------------------------------
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
#--------------------------------------------------------------------------------------


# Modelo de datos para los registros de ritmo cardiaco y SpO2--------------------------

class PulseData(db.Model):
    __tablename__ = 'pulse_data'
    id = db.Column(db.Integer, primary_key=True)
    heart_rate = db.Column(db.Float, nullable=False)
    spo2 = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

#--------------------------------------------------------------------------------------


# Modelo Paciente----------------------------------------------------------------------
class Paciente(db.Model):
    __tablename__ = 'tb_pacientes'
    id = db.Column(db.Integer, primary_key=True)
    cedula = db.Column(db.String(20), nullable=False)
    nombres = db.Column(db.String(100), nullable=False)
    apellidos = db.Column(db.String(100), nullable=False)
    tipo_sangre = db.Column(db.String(5), nullable=False)
    novedades = db.Column(db.Text)
    descripcion = db.Column(db.Text, nullable=False)
    fecha_registro = db.Column(db.DateTime, default=db.func.current_timestamp())
#---------------------------------------------------------------------------------------
    

