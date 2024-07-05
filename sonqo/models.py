from sonqo import db
from flask_bcrypt import generate_password_hash


class User(db.Model):
    __tablename__ = 'tb_sesiones'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(128), nullable=False)
    rol = db.Column(db.String(20), nullable=False)