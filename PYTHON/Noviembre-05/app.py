# Importar Flask
from flask import Flask, render_template

# Crear una instancia de Flask
app = Flask(__name__)


# RUTAS

# RUTAS ESTÁTICAS
@app.route('/')
def root():
    return 'Hola Mundo!'


@app.route('/saludo')
def saludo():
    return 'Hola, ¿cómo estás?'


# RUTAS DINÁMICAS
@app.route('/saludo/<nombre>')
def saludo_nombre(nombre):
    return 'Hola, ' + nombre + '!'


@app.route('/suma/<int:num1>/<int:num2>')
def suma(num1, num2):
    return 'La suma de ' + str(num1) + ' + ' + str(num2) + ' es: ' + str(num1 + num2)


# RUTAS CON PLANTILLAS
@app.route('/plantilla')
def plantilla():

    estudiantes = [
        {'nombre': 'Diomedes Diaz', 'edad': 25},
        {'nombre': 'Rafael Orozco', 'edad': 30},
        {'nombre': 'Jorge Celedon', 'edad': 35},
        {'nombre': 'Martin Elias', 'edad': 40},
        {'nombre': 'Ivan Villazon', 'edad': 45}
    ]

    return render_template('index.html', profesor="Nestor Ribero", estudiantes=estudiantes)


# Iniciar la aplicación
if __name__ == '__main__':
    # Iniciar la aplicación en modo debug para recargar automáticamente los cambios en el código
    app.run(debug=True)
