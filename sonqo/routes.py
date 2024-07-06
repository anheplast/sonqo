import os
from flask import render_template, redirect, url_for, request, flash, session, send_from_directory, send_file
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
from werkzeug.utils import secure_filename
from sonqo import app, db, bcrypt
from sonqo.models import User, Consejo, Actividad, Cancion
from sonqo.forms import UploadForm

app.config['UPLOAD_FOLDER'] = 'sonqo/static/uploads'


#if not os.path.exists(app.config['UPLOAD_FOLDER']):
#   os.makedirs(app.config['UPLOAD_FOLDER'])

# salir
@app.route('/salir')
def salir():
    print("Sesión antes de salir:", session.get('user_id'))
    session.pop('user_id', None)
    print("Sesión después de salir:", session.get('user_id'))
    return redirect(url_for('login'))

# registro
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

# login
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
            # Redirige según el rol del usuario
            if user.rol == 'profesional':
                return redirect(url_for('profesional'))
            else:
                return redirect(url_for('usuario'))
        else:
            flash('Credenciales incorrectas. Intente de nuevo.', 'error')

    return render_template('auth/login.html', form=form)

# Vista Usuario y Profesional
@app.route('/usuarios')
def usuario():
    return render_template('usuarios.html')

@app.route('/profesional')
def profesional():
    return render_template('profesional.html')

@app.route('/paginas/pulso')
def pulso():
    return render_template('paginas/pulso.html')

# Rutas a las paginas de Usuario
@app.route('/consejos')
def mostrar_consejos():
    consejos = Consejo.query.all()
    return render_template('paginas/consejos.html', consejos=consejos)

@app.route('/actividades')
def mostrar_actividades():
    actividades = Actividad.query.all()
    return render_template('paginas/actividades.html', actividades=actividades)


# Ruta y función para mostrar la página de administración de actividades
@app.route('/administrar/actividades', methods=['GET'])
def administrar_actividades():
    actividades = Actividad.query.all()
    return render_template('admin/admin.html', actividades=actividades)

# Ruta y función para insertar una nueva actividad
@app.route('/insertar_actividad', methods=['POST'])
def insertar_actividad():
    titulo = request.form['titulo']
    descripcion = request.form['descripcion']
    imagen_url = request.form['imagen_url']
    video_url = request.form['video_url']

    nueva_actividad = Actividad(titulo=titulo, descripcion=descripcion, imagen_url=imagen_url, video_url=video_url)
    db.session.add(nueva_actividad)
    db.session.commit()

    return redirect(url_for('administrar_actividades'))

# Ruta y función para eliminar una actividad existente
@app.route('/eliminar_actividad', methods=['POST'])
def eliminar_actividad():
    id_actividad = request.form['id_actividad']

    actividad_a_eliminar = Actividad.query.get(id_actividad)
    if actividad_a_eliminar:
        db.session.delete(actividad_a_eliminar)
        db.session.commit()

    return redirect(url_for('administrar_actividades'))

# Playlist


@app.route('/admin', methods=['GET', 'POST'])
def upload():
    form = UploadForm()
    if form.validate_on_submit():
        titulo = form.titulo.data
        artista = form.artista.data
        archivo = form.archivo.data
        nombre_archivo = secure_filename(archivo.filename)

        # Guardar archivo en la carpeta de uploads
        archivo.save(os.path.join(app.config['UPLOAD_FOLDER'], nombre_archivo))

        # Crear instancia de Cancion sin archivo_binario
        nueva_cancion = Cancion(
            titulo=titulo,
            artista=artista,
            nombre_archivo=nombre_archivo
        )

        # Guardar en la base de datos
        db.session.add(nueva_cancion)
        db.session.commit()

        flash('Archivo subido correctamente.', 'success')
        return redirect(url_for('playlist'))

    return render_template('admin/admin.html', form=form)



@app.route('/playlist')
def playlist():
    songs = Cancion.query.all()
    return render_template('paginas/playlist.html', songs=songs)



# Ruta para mostrar la página de administración
@app.route('/admin', methods=['GET'])
def administrar_consejos():
    return render_template('admin/admin.html')

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
