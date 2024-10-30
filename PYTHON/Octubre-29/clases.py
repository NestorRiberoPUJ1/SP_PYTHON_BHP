

""" POO: Programación Orientada a Objetos """

# Clase: Es un molde para crear objetos
# Objetos: Instancias de una clase


import random


class Automovil:

    # Atributos de clase
    autos_creados = 0
    lista_autos = []
    colores_disponibles = ['Blanco', 'Rojo',
                           'Amarillo', 'Azul', 'Plata', 'Negro']

    # Constructor

    def __init__(self, carroceria: str, marca: str, modelo: str, ruedas: int, puertas: int, motor: float, año: int):
        # Atributos
        self.carroceria = carroceria
        self.marca = marca
        self.modelo = modelo
        self.ruedas = ruedas
        self.puertas = puertas
        self.motor = motor
        self.año = año
        self.velocidad = 0
        # Asignar un color aleatorio de la lista de colores de la clase
        self.color = random.choice(Automovil.colores_disponibles)
        # Incrementamos los autos credos
        Automovil.autos_creados += 1
        Automovil.lista_autos.append(self)

    # Métodos de instancia

    def acelerar(self, cantidad: int = 1) -> int:
        self.velocidad += cantidad
        print(f'{self.modelo} acelerando a {self.velocidad} km/h')
        return self

    def frenar(self, cantidad: int = 1) -> int:
        self.velocidad -= cantidad
        print(f'{self.modelo} frenando a {self.velocidad} km/h')
        return self


    # Métodos de clase

    @classmethod
    def agregar_color(cls, color: str):
        cls.colores_disponibles.append(color)


    # Métodos estáticos
    @staticmethod
    def km_a_millas(km: float) -> float:
        return km * 0.621371


# Ejecución si es el archivo principal
if __name__ == '__main__':

    # Crear una instancia de la clase Automovil

    volkswagen_amarok = Automovil(
        'Pick-up', 'Volkswagen', 'Amarok', 4, 4, 2.0, 2021)
    audi_q7 = Automovil('SUV', 'Audi', 'Q7', 4, 4, 3.0, 2024)
    tuktuk = Automovil('Motocarro', 'Bajaj', 'Tuktuk', 3, 1, 0.2, 2020)
    Automovil('Sedán', 'Toyota', 'Corolla', 4, 4, 1.8, 2022)

    print(volkswagen_amarok.marca)
    print(audi_q7.modelo)
    print(tuktuk.puertas)
    volkswagen_amarok.motor = 2.5
    print(volkswagen_amarok.motor)

    # Acelerar
    print(audi_q7.velocidad)
    audi_q7.acelerar(100)
    print(audi_q7.velocidad)
    print(volkswagen_amarok.velocidad)

    # Vamos a realizar una carrera

    tuktuk.acelerar(15).acelerar(25).acelerar(30).acelerar(35).frenar(105)


    print(Automovil.autos_creados)
    print(Automovil.lista_autos[3].marca)

    Automovil.agregar_color('Verde')
    print(Automovil.colores_disponibles)


    print(Automovil.km_a_millas(audi_q7.velocidad))