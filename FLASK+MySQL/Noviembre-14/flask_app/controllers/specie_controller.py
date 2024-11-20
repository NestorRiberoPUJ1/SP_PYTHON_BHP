from flask_app import app
from flask import redirect, render_template, request
from flask_app.models.species import species


# RUTA PARA VER TODOS LOS ESPECIES
@app.route('/species')
def view_specie():
    specie_list = species.all()
    return render_template('species/view.html', species=specie_list)

# RUTA DEL FORMULARIO DE CREACIÓN DE ESPECIES


@app.route('/species/create', methods=['GET'])
def create_specie():
    return render_template('species/create.html')

# RUTA PARA CREAR UN ESPECIE QUE RECIBE LOS DATOS DEL FORMULARIO


@app.route('/species/create', methods=['POST'])
def create_post_specie():
    # request.form es un diccionario que contiene los datos del formulario
    new_specie = species(request.form)
    species.save(new_specie.__dict__())
    return redirect('/species')

# RUTA PARA VER LOS DETALLES DE UN ESPECIE


@app.route('/species/<int:id>')
def detail_specie(id):
    # Buscamos al usuario por su id
    specie = species.find_by_id(id)
    specie
    return render_template('species/detail.html', specie=specie)

# RUTA PARA EDITAR UN ESPECIE

@app.route('/species/<int:id>/edit')
def edit_specie(id):
    # Buscamos al usuario por su id
    specie = species.find_by_id(id)
    return render_template('species/edit.html', specie=specie)

# RUTA PARA ACTUALIZAR LOS DATOS DE UN ESPECIE


@app.route('/species/<int:id>/edit', methods=['POST'])
def edit_post_specie(id):
    # Creamos un objeto de la clase species con los datos del formulario
    updated_specie = species(request.form)
    # Asignamos el id al objeto
    updated_specie.id = id
    # Actualizamos los datos del usuario
    species.update(updated_specie.__dict__())
    return redirect('/species')

# RUTA PARA ELIMINAR UN ESPECIE


@app.route('/species/<int:id>/delete')
def delete_specie(id):
    species.delete_by_id(id)
    return redirect('/species')
