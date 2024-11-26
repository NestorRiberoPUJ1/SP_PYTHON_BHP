from flask import redirect, render_template, request
from flask_app import app
from flask_app.models import usuarios
from flask_app import bcrypt



@app.route('/')
def index():
    return render_template('root/index.html')

@app.route('/register', methods=['POST'])
def register():
    if(not usuarios.Usuario.validate(request.form)):
        return redirect('/')
    # Encriptar la contraseña
    nuevo_usuario = usuarios.Usuario(request.form)
    nuevo_usuario.contraseña = bcrypt.generate_password_hash(request.form['contraseña'])
    usuarios.Usuario.save(nuevo_usuario.__dict__())
    return redirect('/dashboard')

@app.route('/login', methods=['POST'])
def login():
    if(not usuarios.Usuario.validate_login(request.form)):
        return redirect('/')
    return redirect('/dashboard')
