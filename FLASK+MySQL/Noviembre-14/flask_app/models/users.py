

from dataclasses import dataclass
from datetime import date

if __name__ == '__main__':
    from ..config.mysqlconnection import connectToMySQL
else:
    from flask_app.config.mysqlconnection import connectToMySQL

@dataclass
class Users:

    id: int
    firstname: str
    lastname: str
    email: str
    username: str
    password: str
    address: str
    created_at: date
    updated_at: date
    referral_id: int

    # CONSTRUCTOR DE LA CLASE
    def __init__(self, data):
        self.id = data.get('id')
        self.firstname = data.get('firstname')
        self.lastname = data.get('lastname')
        self.email = data.get('email')
        self.username = data.get('username')
        self.password = data.get('password')
        self.address = data.get('address')
        self.created_at = data.get('created_at')
        self.updated_at = data.get('updated_at')
        self.referral_id = data.get('referral_id') or "N/A"
        



    # DEFINEN LAS FUNCIONALIDADES DEL CRUD

    # OBTENER TODOS LOS USUARIOS

    @classmethod
    def get_all(cls):
        # CREAR EL QUERY
        query = "SELECT * FROM users;"
        # OBTENER LOS RESULTADOS
        results = connectToMySQL('red_social').query_db(query)
        # CREAR UNA LISTA DE OBJETOS DE LA CLASE
        users = []
        for user in results:
            users.append(cls(user))
        return users


# PRUEBAS DE LA CLASE
if __name__ == '__main__':
    users = Users.get_all()
    print(users)
