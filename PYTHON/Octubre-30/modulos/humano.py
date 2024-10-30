

from dataclasses import dataclass
from datetime import date

from typing import List, TYPE_CHECKING


if TYPE_CHECKING:
    from mascota import Mascota

@dataclass
class Humano:

    dni: str
    nombres: str
    apellidos: str
    fecha_nacimiento: date
    apto_mascota: bool  # True: Si, False: No
    # RELACION CON MASCOTA
    mascotas: List['Mascota']
    
    




# PRUEBA CUANDO SE EJECUTA EL ARCHIVO
if __name__ == "__main__":

    print("HOLA")