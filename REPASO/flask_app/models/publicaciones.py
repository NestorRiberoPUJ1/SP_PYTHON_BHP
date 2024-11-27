
from dataclasses import dataclass
from datetime import date
from typing import ClassVar

from flask import flash
from flask_app.models.default_model import default_model
from flask_app.utils.validadores import error_message, esta_vacio


@dataclass(init=False)
class Publicacion(default_model):
    # Nombre de la tabla
    table_name: ClassVar[str] = "publicaciones"

    # Atributos de la clase
    nombre: str
    fecha: date
    lugar: str
    descripcion: str

    owner_id: int

    @staticmethod
    def validate(data):
        # Variable que indica si los datos son válidos
        is_valid = True
        if (esta_vacio(data.get('nombre'))):
            is_valid = False
            flash("El nombre no puede estar vacío", "nombre")
        if (esta_vacio(data.get('fecha'))):
            is_valid = False
            flash("La fecha no puede estar vacía", "fecha")
        if (esta_vacio(data.get('lugar'))):
            is_valid = False
            flash("El lugar no puede estar vacío", "lugar")
        if (esta_vacio(data.get('descripcion'))):
            is_valid = False
            flash("La descripción no puede estar vacía", "descripcion")
        if (esta_vacio(data.get('owner_id'))):
            is_valid = False
            flash("El owner_id no puede estar vacío", "owner_id")

        return is_valid

    @staticmethod
    def validate_2(data):

        error_nombre = not error_message(
            True, "El nombre no puede estar vacío", "nombre")(esta_vacio)(data.get('nombre'))
        error_fecha = not error_message(
            True, "La fecha no puede estar vacía", "fecha")(esta_vacio)(data.get('fecha'))
        error_lugar = not error_message(
            True, "El lugar no puede estar vacío", "lugar")(esta_vacio)(data.get('lugar'))
        error_descripcion = not error_message(
            True, "La descripción no puede estar vacía", "descripcion")(esta_vacio)(data.get('descripcion'))
        error_owner_id = not error_message(
            True, "El owner_id no puede estar vacío", "owner_id")(esta_vacio)(data.get('owner_id'))

        return error_nombre and error_fecha and error_lugar and error_descripcion and error_owner_id
        
