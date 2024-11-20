

from dataclasses import InitVar, dataclass
from typing import ClassVar
from flask_app.models.default_model import default_model
from flask_app.models import users
from flask_app.models import reactions


@dataclass(init=False)
class posts(default_model):
    # Nombre de la tabla
    table_name: ClassVar[str] = 'posts'

    # Campos de la tabla
    content: str
    owner_id: int

    # RELACIONES
    owner: InitVar["users.Users"]
    reactions: InitVar[list["reactions.reactions"]]
    users_reacted: InitVar[list["users.Users"]]

    # METODOS DE RELACIONES
    # Método para obtener el usuario dueño del post

    def get_owner(self):
        pass

    # Método para obtener las reacciones de un post
    def get_reactions(self):
        # Crear el query
        query = f'SELECT * FROM reactions WHERE posts_id = %(id)s;'
        data = self.__dict__()
        results = self.run_query(query, data)
        self.reactions = []
        if results:
            for result in results:
                new_reaction= reactions.reactions(result)
                new_reaction= new_reaction.get_user()
                self.reactions.append(new_reaction)
        return self
