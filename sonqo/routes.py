import os
import json
from flask import render_template, redirect, url_for, request, flash, session, send_from_directory, send_file, jsonify, Blueprint
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
from werkzeug.utils import secure_filename
from sonqo import app, db, bcrypt
from sonqo.models import User, Consejo, Actividad, Cancion, PulseData, Paciente
from sonqo.forms import UploadForm
from flask_cors import CORS

from sonqo.models import PulseData
from sonqo import db

#ESP32
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask_sqlalchemy import SQLAlchemy

app.config['UPLOAD_FOLDER'] = 'sonqo/static/uploads'

if not os.path.exists(app.config['UPLOAD_FOLDER']):
   os.makedirs(app.config['UPLOAD_FOLDER'])


# salir-----------------------------------------------------------------------------------
@app.route('/salir')
def salir():
    print("Sesión antes de salir:", session.get('user_id'))
    session.pop('user_id', None)
    print("Sesión después de salir:", session.get('user_id'))
    return redirect(url_for('login'))
#-----------------------------------------------------------------------------------------

# registro--------------------------------------------------------------------------------
@app.route('/registro', methods=["GET", "POST"])
def crear_registro():
    if request.method == "POST":
        usuario = request.form['username']
        password = request.form['password']
        rol = request.form['rol']

        # Verificar si el nombre de usuario ya existe
        usuario_existente = User.query.filter_by(username=usuario).first()
        if usuario_existente:
            return render_template("auth/registro.html", registro_correcto="El nombre de usuario ya existe. Por favor elige otro.")

        # Encriptar la contraseña antes de almacenarla
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        # Crear un nuevo usuario
        nuevo_usuario = User(username=usuario, password=hashed_password, rol=rol)

        # Añadir el nuevo usuario a la sesión de la base de datos
        db.session.add(nuevo_usuario)
        db.session.commit()

        return render_template("auth/registro.html", registro_correcto="Usuario Registrado Exitosamente")

    return render_template('auth/registro.html')
#------------------------------------------------------------------------------------------

# login------------------------------------------------------------------------------------
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
#-----------------------------------------------------------------------------------------


#-----------------------------------------------------------------------------------------
# Vista Usuario y Profesional
@app.route('/usuarios')
def usuario():
    return render_template('usuarios.html')


@app.route('/paginas/pulso')
def pulso():
    pulso_data = PulseData.query.order_by(PulseData.timestamp.desc()).all()  # Obtener todos los datos, ordenados por timestamp descendente
    return render_template('paginas/pulso.html', pulso_data=pulso_data)



# Rutas a las paginas de Usuario

@app.route('/homeusuario')
def mostrar_homeusuario():
    return render_template('paginas/homeusuario.html')

@app.route('/homeprofesional')
def mostrar_homeprofesional():
    return render_template('paginas/homeprofesional.html')

@app.route('/homeadmin')
def mostrar_homeadmin():
    return render_template('admin/homeadmin.html')

@app.route('/consejos')
def mostrar_consejos():
    consejos = Consejo.query.all()
    return render_template('paginas/consejos.html', consejos=consejos)

@app.route('/actividades')
def mostrar_actividades():
    actividades = Actividad.query.all()
    return render_template('paginas/actividades.html', actividades=actividades)
#-------------------------------------------------------------------------------------------


# Rutas para listar Consejos y Actividades -------------------------------------------------
@app.route('/profesional/listactividades')
def listar_actividades():
    actividades = Actividad.query.all()
    return render_template('list_actividades.html', actividades=actividades)

@app.route('/profesional/listconsejos')
def listar_consejos():
    consejos = Consejo.query.all()
    return render_template('list_consejos.html', consejos=consejos)
#------------------------------------------------------------------------------------------



# Admin Actividades -----------------------------------------------------------------------

# Ruta y función para insertar una nueva actividad

#-----------------------------------------------------------------------------------------



#Playlist---------------------------------------------------------------------------------
# Ruta a Playlist
@app.route('/playlist')
def playlist():
    songs = Cancion.query.all()
    return render_template('paginas/playlist.html', songs=songs)

@app.route('/admin/playlist')
def subir_cancion():
    form = UploadForm()
    return render_template('admin/admin_playlist.html', form=form)


@app.route('/admin', methods=['GET', 'POST'])
def admin_panel():
    form = UploadForm()
    if form.validate_on_submit():
        titulo = form.titulo.data
        artista = form.artista.data
        archivo = form.archivo.data
        nombre_archivo = secure_filename(archivo.filename)

        # Guardar archivo en la carpeta de uploads
        archivo.save(os.path.join(app.config['UPLOAD_FOLDER'], nombre_archivo))

        # Crear instancia de Cancion con archivo guardado
        nueva_cancion = Cancion(
            titulo=titulo,
            artista=artista,
            nombre_archivo=nombre_archivo
        )

        # Guardar en la base de datos
        db.session.add(nueva_cancion)
        db.session.commit()

        flash('Archivo subido correctamente.', 'success')
        return redirect(url_for('admin_panel'))  # Redirige a la página de administración

    return render_template('admin/admin.html', form=form)




# Ruta admin actividades-------------------------------------------------------------------
@app.route('/manejar_actividades', methods=['GET'])
def admin_actividades():
    actividades = Actividad.query.all()
    return render_template('admin/admin_actividades.html', actividades=actividades)

# Insertar actividad
@app.route('/insertar_actividad', methods=['POST'])
def insertar_actividad():
    titulo = request.form['titulo']
    descripcion = request.form['descripcion']
    imagen_url = request.form['imagen_url']
    video_url = request.form['video_url']

    nueva_actividad = Actividad(titulo=titulo, descripcion=descripcion, imagen_url=imagen_url, video_url=video_url)
    db.session.add(nueva_actividad)
    db.session.commit()

    flash('Actividad insertada exitosamente', 'success')
    return jsonify({'status': 'success', 'message': 'Actividad insertada exitosamente'})

# Eliminar actividad
@app.route('/eliminar_actividad', methods=['POST'])
def eliminar_actividad():
    id_actividad = request.form['id_actividad']

    actividad_a_eliminar = Actividad.query.get(id_actividad)
    if actividad_a_eliminar:
        db.session.delete(actividad_a_eliminar)
        db.session.commit()

    flash('Actividad eliminada exitosamente', 'success')
    return jsonify({'status': 'success', 'message': 'Actividad eliminada exitosamente'})
#------------------------------------------------------------------------------------------



# Ruta admin playlist----------------------------------------------------------------------

#------------------------------------------------------------------------------------------


# Admin Consejos -----------------------------------------------------------------------

@app.route('/manejar_consejos', methods=['GET'])
def admin_consejos():
    consejos = Consejo.query.all()
    return render_template('admin/admin_consejos.html', consejos=consejos)

# Insertar consejo
@app.route('/insertar_consejo', methods=['POST'])
def insertar_consejo():
    titulo = request.form['titulo']
    descripcion = request.form['descripcion']
    detalles = request.form['detalles']
    imagen_url = request.form['imagen_url']

    nuevo_consejo = Consejo(titulo=titulo, descripcion=descripcion, detalles=detalles, imagen_url=imagen_url)
    db.session.add(nuevo_consejo)
    db.session.commit()

    flash('Consejo insertado exitosamente', 'success')
    return jsonify({'status': 'success', 'message': 'Consejo insertado exitosamente'})

# Eliminar consejo
@app.route('/eliminar_consejo', methods=['POST'])
def eliminar_consejo():
    id_consejo = request.form['id_consejo']

    consejo_a_eliminar = Consejo.query.get(id_consejo)
    if consejo_a_eliminar:
        db.session.delete(consejo_a_eliminar)
        db.session.commit()

    flash('Consejo eliminado exitosamente', 'success')
    return jsonify({'status': 'success', 'message': 'Consejo eliminado exitosamente'})


#------------------------------------------------------------------------------------------



# Registro paciente------------------------------------------------------------------------
@app.route('/profesional', methods=['GET', 'POST'])
def profesional():
    if request.method == 'POST':
        cedula = request.form['cedula']
        nombres = request.form['nombres']
        apellidos = request.form['apellidos']
        tipo_sangre = request.form['tipo_sangre']
        novedades = request.form['novedades']
        descripcion = request.form['descripcion']

        nuevo_paciente = Paciente(
            cedula=cedula,
            nombres=nombres,
            apellidos=apellidos,
            tipo_sangre=tipo_sangre,
            novedades=novedades,
            descripcion=descripcion
        )
        db.session.add(nuevo_paciente)
        db.session.commit()

        flash('Paciente registrado exitosamente', 'success')
        return redirect(url_for('profesional'))  # Mantenerse en la misma página

    return render_template('profesional.html')



@app.route('/registro_paciente', methods=['GET', 'POST'])
def registro_paciente():
    return render_template('paginas/registro_paciente.html')


@app.route('/lista_pacientes', methods=['GET'])
def lista_pacientes():
    pacientes = Paciente.query.all()
    return render_template('paginas/lista_pacientes.html', pacientes=pacientes)




@app.route('/consejos_actividades', methods=['GET'])
def consejos_actividades():
    consejos = Consejo.query.all()
    actividades = Actividad.query.all()
    return render_template('paginas/admin_consejos_actividades.html', consejos=consejos, actividades=actividades)



bp = Blueprint('api', __name__, url_prefix='/api')

# Ruta para recibir datos de pulso desde ESP32 usando GET
@bp.route('/pulso', methods=['GET'])
def recibir_datos_pulso():
    heart_rate = request.args.get('heart_rate')
    spo2 = request.args.get('spo2')

    if heart_rate is not None and spo2 is not None:
        try:
            # Guardar los datos en la base de datos
            nuevo_dato = PulseData(heart_rate=float(heart_rate), spo2=float(spo2))
            db.session.add(nuevo_dato)
            db.session.commit()
            return jsonify({'message': 'Datos recibidos correctamente'}), 200
        except ValueError:
            return jsonify({'error': 'Datos inválidos, no se pueden convertir a números'}), 400
    else:
        return jsonify({'error': 'Datos inválidos'}), 400

# Ruta para obtener todos los datos de pulso almacenados
@bp.route('/datos_pulso', methods=['GET'])
def obtener_datos_pulso():
    try:
        datos = PulseData.query.all()
        datos_json = [{'heart_rate': dato.heart_rate, 'spo2': dato.spo2, 'timestamp': dato.timestamp.strftime('%Y-%m-%d %H:%M:%S')} for dato in datos]
        return jsonify(datos_json), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Ruta para obtener los últimos datos de pulso almacenados
@app.route('/ultimos_pulsos', methods=['GET'])
def get_ultimos_pulsos():
    try:
        # Obtener los últimos datos de pulso de la base de datos
        pulso_data = PulseData.query.order_by(PulseData.timestamp.desc()).limit(10).all()
        # Formatear los datos como JSON para enviar al cliente
        data = [{
            'id': pulse.id,
            'heart_rate': pulse.heart_rate,
            'spo2': pulse.spo2,
            'timestamp': pulse.timestamp.strftime('%Y-%m-%d %H:%M:%S')
        } for pulse in pulso_data]

        return jsonify(data), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500  