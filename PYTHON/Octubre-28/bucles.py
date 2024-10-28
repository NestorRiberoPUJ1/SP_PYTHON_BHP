

""" BUCLES """

# Bucle while
# Bucle for

# Bucle while
# Es un bucle que se repite mientras una condición sea verdadera, cuantas veces sea necesario.
# Sintaxis:
# while condición:
#     bloque de código

# Ejemplo:

import random

numero_aleratorio = 0
while (numero_aleratorio <= 999):
    numero_aleratorio = random.randint(0, 1000)
    print("El número aleatorio es: ", numero_aleratorio)


# Bucle for
# Es un bucle que se repite un número determinado de veces.
# Sintaxis:
# for variable in secuencia:
#     bloque de código

# Ejemplo:
for i in range(0, 10):  # range(inicio, fin) -> [inicio, fin)
    print(i)

# Elemento iterable
# Es un objeto que se puede recorrer con un bucle for.
# Ejemplo de elementos iterables:
# - Listas
# - Tuplas
# - Diccionarios
# - Conjuntos

# Ejemplo de listas
lista_grupos_de_salsa = ["Grupo Niche","Los Hermanos Lebron","Fruko y sus Tesos","Joe Arroyo"]
for grupo in lista_grupos_de_salsa:
    print(grupo)

# Ejemplo de tuplas
tuplas_grupos_de_banda_mexicana = ("Los Tigres del Norte","Los Bukis","Los Temerarios","Los Yonic's")
for item in tuplas_grupos_de_banda_mexicana:
    print(item)

# Ejemplo de diccionarios
diccionario_informacion_vicente_fernandez = {
    "nombre": "Vicente Fernandez",
    "edad": 81,
    "canciones": ["Volver, volver", "El Rey", "Estos celos"],
    "esposa": "Cuquita Abarca",
    "hijos": ["Alejandro Fernandez", "Gerardo Fernandez", "Vicente Fernandez Jr."],
    "nietos": ["Camila Fernandez", "Emiliano Fernandez", "Valentina Fernandez"],
}
print(diccionario_informacion_vicente_fernandez.items())
for key, value in diccionario_informacion_vicente_fernandez.items():
    print(key, ":", value)

# Ejemplo de conjuntos
conjunto_colores = {"rojo", "azul", "verde", "amarillo"}
for color in conjunto_colores:
    print(color)


