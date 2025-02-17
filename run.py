from flask import Flask, render_template

# from modules.auth_modulo.models import UserModel
from modules.auth_modulo.routes import auth_bp 
from modules.main.routes import main_bp

app = Flask(__name__)


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

# Registro de blueprint
# blueprint para usuarios
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(main_bp, url_prefix='/')



print(app.url_map)

if __name__ == '__main__':
    app.run(debug=True)