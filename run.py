from sonqo import app, db
from flask_cors import CORS
from sonqo.routes import bp as api_bp


CORS(app)
app.register_blueprint(api_bp)

if __name__ == '__main__':
    CORS(app)
    with app.app_context():
        db.create_all()
    app.run(debug=True, host='192.168.1.13', port=5000)
    print("Script ejecutado correctamente")