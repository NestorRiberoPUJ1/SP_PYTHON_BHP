
from datetime import date
from modulos.humano import Humano
from modulos.mascota import Mascota

nestor = Humano("96741852", "Nestor", "Ribero", date(1997, 6, 20), True, [])
print(nestor)

gandolfo = Mascota("Chinchilla", "Pradera", "Gandolfo",
                   ["Gris", "Blanca"], "TITI", "TIERRA", True, True, [])


nestor.mascotas.append(gandolfo)
gandolfo.dueños.append(nestor)
print(nestor.mascotas)
print(gandolfo.dueños)

