

from dataclasses import InitVar, dataclass
from typing import ClassVar
from flask_app.models.default_model import default_model

from flask_app.models import species

@dataclass(init=False)
class breeds(default_model):
    # Nombre de la tabla como atributo de la clase
    table_name: ClassVar[str] = 'breeds'

    # Atributos de la clase
    name: str
    specie_id: int

    # RELACIONES
    specie: InitVar["species.species"]


# Pruebas de la clase
if __name__ == '__main__':

    print(breeds.data_fields())

