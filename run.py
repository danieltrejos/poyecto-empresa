from flask import Flask, render_template


app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(debug=True)