from flask import redirect, request
from flask_app import app
from flask_app.models import publicaciones


@app.route('/publicaciones/create', methods=['POST'])
def create_publicacion():
    data = request.form.copy()  # Copiar los datos del formulario para no modificar el original
    data['owner_id'] = 1 # Cambiar por el id del usuario logueado
    if (not publicaciones.Publicacion.validate_2(data)):
        return redirect('/dashboard')

    # Crear la nueva publicación
    nueva_publicacion = publicaciones.Publicacion(data)
    publicaciones.Publicacion.save(nueva_publicacion.__dict__())
    return redirect('/dashboard')
