from flask import Flask, render_template
from database.db import db
from config import Config
from flask_cors import CORS

# from modules.auth_modulo.models import UserModel
from modules.auth_module.routes import auth_bp 
from modules.main.routes import main_bp
from modules.usuarios_module.routes import usuarios_bp


from views.routes import dashboard_bp




# Rutas principales de login y authentication
""" 
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def Login():
    return render_template('Login.html')


@app.route('/recuperacion')
def Recuperacion():
    return render_template('Recuperacion.html')

@app.route('/registro')
def Registro():
    return render_template('Registro.html')

"""

def create_app():
    
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    

    # Registro de blueprint
    # blueprint para usuarios
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(main_bp, url_prefix='/')
    app.register_blueprint(dashboard_bp, url_prefix='/dashboard')
    app.register_blueprint(usuarios_bp)
    

    print (app.url_map)
    CORS(app)
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)