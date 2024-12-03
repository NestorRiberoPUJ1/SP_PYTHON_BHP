import os
from flask import Flask, render_template
from dotenv import load_dotenv
from flask_bcrypt import Bcrypt

# DEFINIMO EL PATH DE DÓNDE VAMOS A GUARDAR LOS ARCHIVOS QUE SE SUBAN
UPLOAD_FOLDER = 'flask_app/uploads'
SERVE_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {
    'img': {'png', 'jpg', 'jpeg', 'svg'},
    'doc': {'pdf', 'docx', 'txt'},
    'vid': {'mp4', 'avi', 'mov'},
}


# CONFIGURACIÓN DE LA APLICACIÓN
load_dotenv()
app = Flask(__name__)
app.secret_key = os.getenv('APP_SECRET_KEY')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SERVE_FOLDER'] = SERVE_FOLDER
bcrypt = Bcrypt(app)
