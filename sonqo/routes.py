from flask import Flask, render_template, redirect, url_for, request, flash, make_response, session
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired
from flask_bcrypt import Bcrypt
import matplotlib.pyplot as plt
import io
import base64

from sonqo import app, db
from sonqo.models import User

bcrypt = Bcrypt(app)

# salir ---------

@app.route('/salir')
def salir():
    print("Sesión antes de salir:", session.get('user_id'))
    session.pop('user_id', None)
    print("Sesión después de salir:", session.get('user_id'))
    return redirect(url_for('login'))

# ---------------

# registro ------

@app.route('/registro', methods=["GET", "POST"])
def crear_registro():
    if request.method == "POST":
        usuario = request.form['username']
        password = request.form['password']
        rol = request.form['rol']

        # Verificar si el nombre de usuario ya existe
        usuario_existente = User.query.filter_by(username=usuario).first()
        if usuario_existente:
            return render_template("registro.html", registro_correcto="El nombre de usuario ya existe. Por favor elige otro.")

        # Encriptar la contraseña antes de almacenarla
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        # Crear un nuevo usuario
        nuevo_usuario = User(username=usuario, password=hashed_password, rol=rol)

        # Añadir el nuevo usuario a la sesión de la base de datos
        db.session.add(nuevo_usuario)
        db.session.commit()

        return render_template("registro.html", registro_correcto="Usuario Registrado Exitosamente")

    return render_template('auth/registro.html')

#-----------------


# login ----------

class LoginForm(FlaskForm):
    username = StringField('Usuario', validators=[DataRequired()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    submit = SubmitField('Iniciar Sesión')

@app.route('/usuario')
def usuario():
    return render_template('usuario.html')

@app.route('/profesional')
def profesional():
    return render_template('profesional.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = User.query.filter_by(username=username).first()

        if user and bcrypt.check_password_hash(user.password, password):
            # Redirige según el rol del usuario
            if user.rol == 'profesional':
                return redirect(url_for('profesional'))
            else:
                return redirect(url_for('usuario'))
        else:
            flash('Credenciales incorrectas. Intente de nuevo.', 'error')

    return render_template('auth/login.html', form=form)

# ----------------

@app.route('/pag1')
def pag1():
    return render_template('pag1.html')

