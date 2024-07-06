from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileAllowed

class UploadForm(FlaskForm):
    titulo = StringField('Título', validators=[DataRequired()])
    artista = StringField('Artista', validators=[DataRequired()])
    archivo = FileField('Archivo', validators=[
        DataRequired(),
        FileAllowed(['mp3'], 'Solo se permiten archivos .mp3')
    ])
    submit = SubmitField('Subir')
