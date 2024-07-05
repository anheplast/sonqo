from flask import Flask, render_template, redirect, url_for, request, flash, make_response
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired
from sonqo import app, db
from sonqo.models import User
from flask_bcrypt import Bcrypt
# Para los gráficos
import matplotlib.pyplot as plt
import io
import base64

bcrypt = Bcrypt(app)

class RegistroForm(FlaskForm):
    username = StringField('Usuario', validators=[DataRequired()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    rol = SelectField('Rol', choices=[('usuario', 'Usuario'), ('profesional', 'Profesional')], validators=[DataRequired()])
    submit = SubmitField('Registrar')

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    form = RegistroForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        rol = form.rol.data

        # Encriptar la contraseña antes de almacenarla
        password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

        # Crear un nuevo usuario
        nuevo_usuario = User(username=username, password=password_hash, rol=rol)

        # Agregar el nuevo usuario a la sesión de la base de datos
        db.session.add(nuevo_usuario)

        # Confirmar los cambios (guardar el nuevo usuario en la base de datos)
        db.session.commit()

        flash('Usuario registrado exitosamente.', 'success')
        return redirect(url_for('login'))

    return render_template('registro.html', form=form)



class LoginForm(FlaskForm):
    username = StringField('Usuario', validators=[DataRequired()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    submit = SubmitField('Iniciar Sesión')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = User.query.filter_by(username=username).first()

        if user and bcrypt.check_password_hash(user.password, password):
            # Aquí podrías establecer la sesión o utilizar Flask-Login
            return redirect(url_for('profesional'))
        else:
            flash('Credenciales incorrectas. Intente de nuevo.', 'error')

    return render_template('login.html', form=form)

@app.route('/profesional')
def profesional():
    return render_template('profesional.html')

# Para el gráfico
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/plot.png')
def plot_png():
    fig, ax = plt.subplots()
    ax.plot([1, 2, 3, 4], [1, 4, 2, 3])
    ax.set(xlabel='x-label', ylabel='y-label', title='Sample Plot')
    ax.grid()

    output = io.BytesIO()
    plt.savefig(output, format='png')
    output.seek(0)
    return make_response(output.getvalue())
