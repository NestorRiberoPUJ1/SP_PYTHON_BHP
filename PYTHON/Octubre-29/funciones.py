
""" FUNCIONES """
# ¿Qué es una función?
# Una función es un bloque de código que sólo se ejecuta cuando es llamado.
# Puede pasar datos, conocidos como parámetros, a una función.
# Una función puede devolver datos como resultado.
# En Python una función se define usando la palabra clave def.
# Ejemplo:

# Funcion sin parametros


def mi_funcion():
    print("Hola, soy una función")

# Funcion con parametros


def mi_funcion2(nombre):
    print("Hola, soy una función con parametros")
    print("Mi nombre es: ", nombre)

# Funcion con parametros y retorno


def mi_funcion3(nombre):
    return "Hola, soy una función con parametros y retorno, mi nombre es: ", nombre

# Las funciones existen para evitar la repetición de código, y para hacer el código más legible.


# Llamando a una función
mi_funcion()    # Funcion sin parametros
mi_funcion2("Juan")  # Funcion con parametros
saludo = mi_funcion3("Juan")    # Funcion con parametros y retorno
print(saludo)


estudiantes = [
    {
        "nombre": "Juan",
        "edad": 25
    },
    {
        "nombre": "Maria",
        "edad": 20
    },
    {
        "nombre": "Pedro",
        "edad": 30
    }
]


def extraer_edad(estudiante):
    return estudiante["edad"]   # Retorna la edad del estudiante


def ordenar_estudiantes_por_edad(lista_estudiantes=[], orden="asc"):
    if orden == "asc":
        lista_estudiantes.sort(key=extraer_edad)
    elif orden == "desc":
        lista_estudiantes.sort(key=extraer_edad, reverse=True)

    return lista_estudiantes


print(ordenar_estudiantes_por_edad())


# Funcion definiendo el tipo de dato de los parametros y del retorno

def suma(a: int, b: int) -> int:
    return a + b


print(suma(5, 10))


def promedio(lista: list[int]) -> float:
    return sum(lista) / len(lista)


""" EJEMPLOS DE FUNCIONES """

# Multiplica por 2: crea una función que reciba un número y devuelva
# una lista que contenga los números enteros multiplicados por dos,
# desde el 0 hasta el número proporcionado como entrada.


def multiplica_por_dos(limite: int) -> list[int]:
    lista = []
    for i in range(0, limite+1):
        lista.append(i*2)
    return lista


print(multiplica_por_dos(5))    # [0, 2, 4, 6, 8, 10]

# Suma y resta: crea una función que reciba una lista con dos números.
# Imprime la suma de los dos números y regresa la resta de los dos números.


def suma_y_resta(lista: list[int]) -> int:
    print("La suma de los dos numeros es: ", lista[0] + lista[1])
    return lista[0] - lista[1]


print(suma_y_resta([10, 3]))    # 7

# Sumatoria menos longitud: crea una función que reciba una lista de números
# y regresa la sumatoria de estos menos la longitud de la lista.


def sumatoria_menos_longitud(lista: list[int]) -> int:
    return sum(lista) - len(lista)


print(sumatoria_menos_longitud([1, 2, 3, 4, 5]))    # 10


# Valores multiplicados por el segundo: escribe una función que reciba una lista
# y crea una nueva lista con todos los valores multiplicados por el segundo número.
# Imprime la longitud de la lista y regresa la nueva lista.
# Si la lista tiene menos de 2 elementos, haz que la función regrese una lista vacía.

def valores_multiplicados_por_el_segundo(lista: list[int]) -> list[int]:
    # Si la lista tiene menos de 2 elementos, regresa una lista vacía
    if len(lista) < 2:
        return []
    new_lista = []
    for i in lista:
        # Multiplica cada elemento por el segundo elemento de la lista
        new_lista.append(i * lista[1])
    print("La longitud de la lista es: ", len(new_lista))
    return new_lista

print(valores_multiplicados_por_el_segundo([1, 2, 3, 4, 5]))    # [2, 4, 6, 8, 10]


# Valor multiplado y longitud: escribe una función que reciba dos números enteros: valor y longitud.
# La función debe crear y regresar una lista cuyo tamaño sea igual a la longitud recibida
# y los valores sean igual a la longitud multiplicada por el valor dado.

def valor_multiplicado_y_longitud(valor: int, longitud: int) -> list[int]:
    lista =[]
    for i in range(0, longitud):
        lista.append(valor * longitud)
    return lista
    #return [valor * longitud] * longitud

print(valor_multiplicado_y_longitud(5, 3))    # [15, 15, 15]