
from flask import redirect, render_template, request, session
from flask_app import app
from flask_app.config.security import session_required

from flask_app.models import usuarios
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)


@app.route('/home')
@session_required
def index():
    return render_template('/home/home.html')


@app.route('/')
def root():
    return render_template('/home/login.html')


@app.route('/login', methods=['POST'])
def login():
    # Buscar el usuario en la base de datos
    email = request.form.get('email')
    user = usuarios.Usuarios.find_by_email(email)
    if user:
        # Si el usuario existe vamos a verificar la contraseña
        if bcrypt.check_password_hash(user.contraseña, request.form.get('contraseña')):
            # Si la contraseña es correcta, guardar el usuario en la session
            session['usuario'] = user
            return redirect('/home')
    # Si el usuario no existe o la contraseña es incorrecta, mostrar un mensaje de error
    return redirect('/')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')
