from flask_app import app
from flask import redirect, render_template, request
from flask_app.models.posts import posts
from flask_app.models.users import Users
from flask_app.models.reactions import reactions


# RUTA PARA VER TODOS LOS POSTS
@app.route('/posts')
def view_post():
    post_list = posts.all()
    return render_template('posts/view.html', posts=post_list)

# RUTA DEL FORMULARIO DE CREACIÓN DE POSTS


@app.route('/posts/create', methods=['GET'])
def create_post():
    user_list = Users.all()
    return render_template('posts/create.html', users=user_list)

# RUTA PARA CREAR UN POST QUE RECIBE LOS DATOS DEL FORMULARIO


@app.route('/posts/create', methods=['POST'])
def create_post_post():
    # request.form es un diccionario que contiene los datos del formulario
    new_post = posts(request.form)
    posts.save(new_post.__dict__())
    return redirect('/posts')

# RUTA PARA VER LOS DETALLES DE UN POST


@app.route('/posts/<int:id>')
def detail_post(id):
    # Buscamos al post por su id
    post = posts.find_by_id(id)
    post = post.get_reactions()
    print(post.reactions)
    user_list = Users.all()
    return render_template('posts/detail.html', post=post, users=user_list)

# RUTA PARA EDITAR UN POST


@app.route('/posts/<int:id>/edit')
def edit_post(id):
    # Buscamos al post por su id
    post = posts.find_by_id(id)
    user_list = Users.all()
    return render_template('posts/edit.html', post=post, users=user_list)

# RUTA PARA ACTUALIZAR LOS DATOS DE UN POST


@app.route('/posts/<int:id>/edit', methods=['POST'])
def edit_post_post(id):
    # Creamos un objeto de la clase posts con los datos del formulario
    updated_post = posts(request.form)
    # Asignamos el id al objeto
    updated_post.id = id
    # Actualizamos los datos del post
    posts.update(updated_post.__dict__())
    return redirect('/posts')

# RUTA PARA ELIMINAR UN POST


@app.route('/posts/<int:id>/delete')
def delete_post(id):
    posts.delete_by_id(id)
    return redirect('/posts')


@app.route('/posts/<int:id>/reactions', methods=['POST'])
def create_reaction(id):
    reaction = reactions(request.form)
    reaction.posts_id = id
    reactions.save(reaction.__dict__())
    return redirect(f'/posts/{id}')
