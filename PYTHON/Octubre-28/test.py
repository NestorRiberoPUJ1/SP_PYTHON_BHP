
# Python es un lenguage de programación interpretado, es decir, no necesita ser compilado para ser ejecutado.
# Python es un lenguaje que no es fuertemente tipado, es decir, no es necesario declarar el tipo de variable que se va a utilizar.
# Python es un lenguaje de programación orientado a objetos.
# Python no necesita de llaves para definir bloques de código, en su lugar, utiliza la indentación.


""" VARIABLES BÁSICAS """

nombre = "Nestor"  # Variable de tipo string
edad = 27  # Variable de tipo entero
estatura = 1.75  # Variable de tipo flotante
graduado = True  # Variable de tipo booleano
moticleta = None  # Variable de tipo None
grupo_sanguinedo = 'A'  # Variable de tipo caracter


""" LISTAS """
# Normalmente se utilizan para almacenar múltiples valores en una sola variable y del mismo tipo
grupos_favoritos = ['Grupo Niche', 'Ritchie Ray y Bobby Cruz',
                    'Hector Lavoe', 'Willie Colon', 'Fruko y sus Tesos']  # Lista de tipo string
lista_combinada = ['Grupo Niche', 1, 2.5, True, None]  # Lista de tipo mixto
# Para acceder a un elemento de la lista se utiliza el índice del elemento
print(grupos_favoritos[0])  # Imprime Grupo Niche
print(lista_combinada[2])  # Imprime 2.5

""" TUPLAS """
# Las tuplas son similares a las listas, pero no se pueden modificar
tupla = ('Grupo Niche', 'Ritchie Ray y Bobby Cruz', 'Hector Lavoe',
         'Willie Colon', 'Fruko y sus Tesos')  # Tupla de tipo string
# Para acceder a un elemento de la tupla se utiliza el índice del elemento
print(tupla[0])  # Imprime Grupo Niche

""" DICCIONARIOS """
# Los diccionarios son estructuras de datos que permiten almacenar múltiples valores de diferentes tipos
# Los diccionarios se componen de llaves y valores
diccionario = {
    'nombre': 'Nestor',
    'edad': 27,
    'estatura': 1.85,
    'graduado': True,
    'moticleta': None
}
# Para acceder a un valor del diccionario se utiliza la llave
print(diccionario['nombre'])  # Imprime Nestor
print(diccionario['edad'])  # Imprime 27
# A diferencia de JS en Python no se puede acceder a un valor de un diccionario utilizando la notación de punto


""" OPERADORES """

# Operadores aritméticos
# Suma
print(5 + 5)  # Imprime 10
# Resta
print(5 - 5)  # Imprime 0
# Multiplicación
print(5 * 5)  # Imprime 25
# División
print(5 / 5)  # Imprime 1.0
# Módulo
print(5 % 5)  # Imprime 0
# Exponenciación
print(5 ** 5)  # Imprime 3125
# División entera
print(5 // 5)  # Imprime 1

# Operadores de comparación
# Igual a
print(5 == 5)  # Imprime True
# Diferente de
print(5 != 5)  # Imprime False
# Mayor que
print(5 > 4)  # Imprime True
# Menor que
print(5 < 4)  # Imprime False
# Mayor o igual que
print(5 >= 5)  # Imprime True
# Menor o igual que
print(5 <= 5)  # Imprime True

# Operadores lógicos
# AND
print(1 == 1 and 4 > 3)  # Imprime True
# OR
print(1 == 1 or 4 < 3)  # Imprime True
# NOT
print(not 1 == 1)  # Imprime False

# Operadores para strings
# Concatenación
print('Hola' + ' Mundo')  # Imprime Hola Mundo
# Concatenacion con numeros
print('Hola' + str(5))  # Imprime Hola5
# Repetición
print('Hola' * 5)  # Imprime HolaHolaHolaHolaHola
# Concatenación con interpolación
nombre = 'Nestor'
print(f'Hola {nombre}')  # Imprime Hola Nestor
edad = 27
# Imprime Hola Nestor, tienes 27 años
print(f'Hola {nombre}, tienes {edad} años')


""" CONDICIONALES """

# IF
if (5 > 4):
    print('5 es mayor que 4')  # Imprime 5 es mayor que 4

# IF ELSE
if (5 < 4):
    print('5 es menor que 4')
else:
    print('5 no es menor que 4')
print('Final')

# IF ELIF ELSE
if (5 < 4):
    print('5 es menor que 4')
elif (5 == 5):
    print('5 es igual a 5')
else:
    print('5 no es menor que 4 ni igual a 5')
    



