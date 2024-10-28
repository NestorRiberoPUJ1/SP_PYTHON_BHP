

""" METODOS DE LISTAS """

# append() - Agrega un elemento al final de la lista
# clear() - Elimina todos los elementos de la lista
# copy() - Devuelve una copia de la lista
# count() - Devuelve el número de elementos con el valor especificado
# extend() - Agrega los elementos de una lista (o cualquier iterable), al final de la lista actual
# index() - Devuelve el índice del primer elemento con el valor especificado
# insert() - Agrega un elemento en la posición especificada
# pop() - Elimina el elemento en la posición especificada
# remove() - Elimina el primer elemento con el valor especificado
# reverse() - Invierte el orden de la lista
# sort() - Ordena la lista

meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
         "Julio", "Septiembre", "Octubre", "Noviembre"]

# append()
meses.append("Diciembre")
print(meses)

# clear()
#meses.clear()
#print(meses)

# copy()
copia_meses = meses.copy()
print(copia_meses)

# count()
print(meses.count("Enero"))

# extend()
meses.extend(["Finaliciembre, Iniciomarzo"])
print(meses)

# index()
print(meses.index("Marzo"))

# insert()
meses.insert(7, "Agosto")
print(meses)

# pop()
meses.pop(7)
print(meses)

# remove()
meses.remove("Finaliciembre, Iniciomarzo")
print(meses)

# reverse()
meses.reverse()
print(meses)

# sort()
meses.sort()
print(meses)


print(len(meses))  # len() - Devuelve el número de elementos de la lista