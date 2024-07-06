import os
from flask import Flask, render_template, redirect, url_for, request, flash, make_response, session, jsonify
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired
from flask_bcrypt import Bcrypt
import matplotlib.pyplot as plt
from werkzeug.utils import secure_filename
from sonqo.config import Config

import io
import base64



from sonqo import app, db
# Modelos
from sonqo.models import User, Consejo, Actividad
from sonqo.models import Cancion

bcrypt = Bcrypt(app)


# Playlist -------------------------------------------
Carpeta_SUBIDAS = app.config['Carpeta_SUBIDAS']
Extensiones_PERMITIDAS = {'webm', 'mp3', 'wav'}

def archivo_permitido(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in Extensiones_PERMITIDAS

@app.route('/subir_audio', methods=['GET', 'POST'])
def subir_audio():
    if request.method == 'POST':
        if 'audio_file' not in request.files:
            flash('No se ha enviado ningún archivo')
            return redirect(request.url)
        
        file = request.files['audio_file']

        if file.filename == '':
            flash('No se ha seleccionado ningún archivo')
            return redirect(request.url)
        
        if file and archivo_permitido(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(Carpeta_SUBIDAS, filename))

            # Guardar información en la base de datos
            nueva_cancion = Cancion(
                titulo=request.form['titulo'],
                artista=request.form['artista'],
                archivo=file.read(),
                nombre_archivo=filename
            )
            db.session.add(nueva_cancion)
            db.session.commit()

            flash('Archivo subido exitosamente')
            return redirect(url_for('playlist'))

    return render_template('subir_audio.html')
#-------------------------------------------------------




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

# Vista Usuario y Profesional-----------------------
@app.route('/usuarios')
def usuario():
    render_template('common/navbar_usuarios.html')
    return render_template('usuarios.html')

@app.route('/profesional')
def profesional():
    return render_template('profesional.html')

#----------------------------------------------------

@app.route('/paginas/pulso')
def pulso():
    return render_template('paginas/pulso.html')



# Rutas a las paginas de Usuario

@app.route('/consejos')
def mostrar_consejos():
    consejos = Consejo.query.all()  # Asegúrate de que esta consulta devuelve datos
    return render_template('paginas/consejos.html', consejos=consejos)

@app.route('/actividades')
def mostrar_actividades():
    actividades = Actividad.query.all()
    return render_template('paginas/actividades.html', actividades=actividades)


@app.route('/playlist')
def playlist():
    # Obtener todas las canciones de la base de datos
    songs = Song.query.all()
    return render_template('paginas/playlist.html', songs=songs)



#----------------------------

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

# Ruta para mostrar la página de administración
@app.route('/administrar/consejos', methods=['GET'])
def administrar_consejos():
    return render_template('admin.html')

# Ruta y función para insertar un nuevo consejo
@app.route('/insertar_consejo', methods=['POST'])
def insertar_consejo():
    titulo = request.form['titulo']
    descripcion = request.form['descripcion']
    detalles = request.form['detalles']
    imagen_url = request.form['imagen_url']

    nuevo_consejo = Consejo(titulo=titulo, descripcion=descripcion, detalles=detalles, imagen_url=imagen_url)
    db.session.add(nuevo_consejo)
    db.session.commit()

    return redirect(url_for('administrar_consejos'))

# Ruta y función para eliminar un consejo existente
@app.route('/eliminar_consejo', methods=['POST'])
def eliminar_consejo():
    id_consejo = request.form['id_consejo']

    consejo_a_eliminar = Consejo.query.get(id_consejo)
    if consejo_a_eliminar:
        db.session.delete(consejo_a_eliminar)
        db.session.commit()

    return redirect(url_for('administrar_consejos'))



