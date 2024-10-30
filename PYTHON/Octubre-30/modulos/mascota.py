

from dataclasses import dataclass
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from humano import Humano

@dataclass
class Mascota:

    # Atributos de instancia
    especie: str    # Especie de la mascota (Perro, Gato, etc.)
    raza: str       # Raza de la mascota (Pastor Aleman, Labrador, etc.)
    nombre: str     # Nombre de la mascota (Firulais, Michi, etc.)
    color: list[str]      # Color de la mascota (Negro, café, etc.)
    sonido: str     #
    medio: str      #
    esterilizado: bool
    vacunado: bool
    # RELACION CON HUMANOS
    dueños: List['Humano']


# PROBAR LA CLASE SI EL ARCHIVO ES EL PRINCIPAL

if __name__ == "__main__":
    firulais = Mascota("Perro", "Galgo", "Firulais",
                       ["Café"], "WOW", "TIERRA", False, True)
    gandolfo = Mascota("Chinchilla", "Pradera", "Gandolfo",
                       ["Gris", "Blanca"], "TITI", "TIERRA", True, True)
