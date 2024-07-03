from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

# Generar el hash de la contraseña
password_hash = bcrypt.generate_password_hash('usuario123').decode('utf-8')
print(password_hash)
