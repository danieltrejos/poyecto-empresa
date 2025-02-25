import os
from flask_sqlalchemy import SQLAlchemy

from dotenv import load_dotenv

load_dotenv()

# basedir = os.path.abspath(os.path.dirname(__file__))

class Config:

    SECRET_KEY = os.getenv('SECRET_KEY') or 'clavenotansecreta'
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL') 
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    #SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key'
    #SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://user:password@localhost/db_lenderV3'  # Ajustar credenciales
    #SQLALCHEMY_TRACK_MODIFICATIONS = False

