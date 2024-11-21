from dataclasses import dataclass
from flask import redirect, render_template, request
from flask_app.controllers import default_controller as DC
from flask_app import app
from flask_app.models import posts
from flask_app.models import users
from flask_app.models import reactions

# POLIMORFISMO CON DATA CLASSES


@dataclass(init=False)
class PostCreate(DC.ModelCreate):

    def get(self):
        user_list = users.Users.all()
        return render_template(f"{self.template_folder}/create.html", users=user_list)


@dataclass(init=False)
class PostDetail(DC.ModelDetail):

    def get(self, id):
        item = self.model.find_by_id(id)
        item = item.get_reactions()
        user_list = users.Users.all()
        return render_template(f"{self.template_folder}/detail.html", item=item, users=user_list)


@dataclass(init=False)
class PostEdit(DC.ModelEdit):

    def get(self, id):
        item = self.model.find_by_id(id)
        user_list = users.Users.all()
        return render_template(f"{self.template_folder}/edit.html", item=item, users=user_list)


# RUTA PARA CREAR UNA REACCION
@app.route('/posts/<int:id>/reactions', methods=['POST'])
def create_reaction(id):
    reaction = reactions(request.form)
    reaction.posts_id = id
    reactions.save(reaction.__dict__())
    return redirect(f'/posts/{id}')


# RUTAS PARA ESPECIES

# RUTA PARA VER TODOS LOS POSTS
app.add_url_rule('/posts', view_func=DC.ModelList.as_view('posts',
                 model=posts.posts, template_folder='posts'))

# RUTA PARA CREAR UN POST
app.add_url_rule('/posts/create', view_func=PostCreate.as_view('posts_create',
                 model=posts.posts, template_folder='posts', on_create_redirect='posts'))

# RUTA PARA VER LOS DETALLES DE UN POST
app.add_url_rule('/posts/<int:id>', view_func=PostDetail.as_view(
    'posts_detail', model=posts.posts, template_folder='posts'))

# RUTA PARA EDITAR UN POST
app.add_url_rule('/posts/<int:id>/edit', view_func=DC.ModelEdit.as_view('posts_edit',
                 model=posts.posts, template_folder='posts', on_update_redirect='posts'))

# RUTA PARA ELIMINAR UN POST
app.add_url_rule('/posts/<int:id>/delete', view_func=DC.ModelDelete.as_view(
    'posts_delete', model=posts.posts, on_delete_redirect='posts'))





