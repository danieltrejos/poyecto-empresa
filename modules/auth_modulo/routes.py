from flask import Blueprint,render_template 

auth_bp = Blueprint('auth_bp', __name__, template_folder="templates")


@auth_bp.route('/')
def index():
    return render_template('index.html')

@auth_bp.route('/login')
def Login():
    return render_template('Login.html')


@auth_bp.route('/recuperacion')
def Recuperacion():
    return render_template('Recuperacion.html')

@auth_bp.route('/registro')
def Registro():
    return render_template('Registro.html')