

from dataclasses import InitVar, dataclass, field
from typing import ClassVar
from flask_app.models.default_model import default_model


@dataclass(init=False)
class Users(default_model):
    table_name: ClassVar[str] = 'users'

    firstname: str
    lastname: str
    email: str
    username: str
    password: str
    address: str

    referral_id: int

    # RELACIONES
    # Cuantos referidos tiene un usuario
    referred_users: InitVar[list["Users"]]
    # Quién es el usuario que refirió a este usuario
    referrer: InitVar["Users"]

    # METODOS DE RELACIONES
    # Método para obtener los usuarios referidos por un usuario
    def get_referred_users(self):
        query = f'SELECT * FROM {self.table_name} WHERE referral_id = %(id)s;'
        data= self.__dict__()
        results = self.run_query(query, data)
        self.referred_users = []
        for result in results:
            self.referred_users.append(Users(result))
        return self
    
    # Método para obtener el usuario que refirió a este usuario
    def get_referrer(self):
        query = f'SELECT * FROM {self.table_name} WHERE id = %(referral_id)s;'
        data = self.__dict__()
        result = self.run_query(query, data)
        self.referrer = None
        if len(result) > 0:
            self.referrer = Users(result[0])
        return self


# PRUEBAS DE LA CLASE
if __name__ == '__main__':
    pass
