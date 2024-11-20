

from dataclasses import InitVar, dataclass, field, fields
from datetime import datetime
from typing import ClassVar
from flask_app.models.default_model import default_model
from flask_app.models import breeds


@dataclass(init=False)
class species(default_model):
    # Nombre de la tabla como atributo de la clase
    table_name: ClassVar[str] = 'species'

    # Atributos de la clase
    name: str

    # RELACIONES
    # razas: breeds.breeds
    breed_list: InitVar[list["breeds.breeds"]]


# Pruebas de la clase
if __name__ == '__main__':

    lista_especies = species.all()
    print(lista_especies)

    buscar_especie = species.find_by_id(12)
    print(buscar_especie)

    print(species.data_fields())

    data = {
        'name': 'Crustaceo'
    }
    species.save(data)
