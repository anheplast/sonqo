from flask import Flask, render_template, redirect, url_for, request, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
from sonqo import app, db
from sonqo.models import User
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

class LoginForm(FlaskForm):
    username = StringField('Usuario', validators=[DataRequired()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    submit = SubmitField('Iniciar Sesión')



@app.route('/registro')
def registro():
    return render_template('registro.html')


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


