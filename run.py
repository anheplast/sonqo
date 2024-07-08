from sonqo import app, db
from flask_cors import CORS
from sonqo.routes import bp as api_bp


CORS(app)
app.register_blueprint(api_bp)

if __name__ == '__main__':
    CORS(app)
    with app.app_context():
        db.create_all()
<<<<<<< HEAD
    app.run(debug=True, host='192.168.1.13', port=5000)
=======
    app.run(debug=True, host='192.168.1.15', port=5000)
>>>>>>> 5de1d6d499c197fb28feda73be2c5563686803e9
    print("Script ejecutado correctamente")