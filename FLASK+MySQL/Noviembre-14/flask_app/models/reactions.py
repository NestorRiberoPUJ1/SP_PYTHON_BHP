
from dataclasses import InitVar, dataclass
from enum import Enum, auto
from typing import ClassVar
from flask_app.models.default_model import default_model
from flask_app.models import posts
from flask_app.models import users


class ReactionOptions(Enum):
    LIKE = "Like"
    DISLIKE = "Dislike"
    FUNNY = "Funny"


@dataclass(init=False)
class reactions(default_model):

    # Nombre de la tabla
    table_name: ClassVar[str] = 'reactions'

    # Campos de la tabla
    posts_id: int
    users_id: int

    type: ReactionOptions

    # RELACIONES

    post: InitVar["posts.posts"]
    user: InitVar["users.Users"]


    # METODOS DE RELACIONES
    # Método para obtener el post al que pertenece la reacción
    def get_post(self):
        query = f'SELECT * FROM {posts.posts.table_name} WHERE id = %(posts_id)s;'
        data = self.__dict__()
        result = self.run_query(query, data)
        self.post = None
        if len(result) > 0:
            self.post = posts.posts(result[0])
        return self
    
    # Método para obtener el usuario que hizo la reacción
    def get_user(self):
        query = f'SELECT * FROM {users.Users.table_name} WHERE id = %(users_id)s;'
        data = self.__dict__()
        result = self.run_query(query, data)
        self.user = None
        if len(result) > 0:
            self.user = users.Users(result[0])
        return self
    