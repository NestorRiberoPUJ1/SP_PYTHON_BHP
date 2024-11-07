import os
from flask import Flask, redirect, render_template, request, session
from dotenv import load_dotenv

load_dotenv()

# Crear la aplicación
app = Flask(__name__)
app.secret_key = os.getenv('APP_SECRET_KEY')

# Ruta para el template de login y registro
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para procesar el formulario de registro
@app.route('/register', methods=['POST'])
def register():
    email = request.form.get('email')
    password = request.form.get('password')
    password_confirm = request.form.get('passwordConfirm')

    if password != password_confirm:
        return redirect('/')
    
    session['email'] = email

    return redirect('/dashboard')

# Ruta para procesar el formulario de login
@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    type = request.form.get('type')
    
    session['email'] = email
    session['type'] = type
    return redirect('/dashboard')

@app.route('/dashboard')
def dashboard():
    # Si el usuario no ha iniciado sesión, redirigir al login
    if 'email' in session:
        return render_template('dashboard.html')
    return redirect('/')

@app.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return redirect('/')


# Iniciar la aplicación
if __name__ == '__main__':
    app.run(debug=True)
