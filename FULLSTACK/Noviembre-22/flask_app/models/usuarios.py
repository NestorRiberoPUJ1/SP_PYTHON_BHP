

from dataclasses import InitVar, dataclass
import re
from typing import ClassVar

from flask import flash
from flask_app.models.default_model import default_model


EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@dataclass(init=False)
class Usuarios(default_model):

    # Nombre de la tabla
    table_name: ClassVar[str] = "usuarios"

    # Atributos de la clase
    email: str
    contraseña: str
    nombre: str
    apellido: str

    # Campos virtuales para las relaciones
    equipo: InitVar[object]
    equipos_favoritos: InitVar[list[object]]


    @staticmethod
    def validate(data):
        # Variable para determinar si los datos son válidos
        is_valid = True
        if(data.get('email') == None or not EMAIL_REGEX.match(data.get('email'))):
            flash('Ingrese un email válido','email')
            is_valid = False
        if(data.get('contraseña') == None or len(data.get('contraseña')) < 8):
            flash('contraseña debe ser mayor a 8 caracteres','contraseña')
            is_valid = False
        if(data.get('nombre') == None or len(data.get('nombre')) < 2):
            flash('nombre debe ser mayor a 2 caracteres','nombre')
            is_valid = False
        if(data.get('apellido') == None or len(data.get('apellido')) < 2):
            flash('apellido debe ser mayor a 2 caracteres','apellido')
            is_valid = False        
        return is_valid

