################### METODOS DE CADENAS #####################
################ LIST ################
# Sirve para crear una lista pero no es tan utilizado
# No es un metodo, es una funcion
lista = list(["Hola", True, 12.4, False])

print(lista)
################ LEN ################
# Devuelve la cantidad de elementos de una lista
resultado = len(lista)

print(resultado)


################ APPEND ################
# Agrega un nuevo elemento a la lista (Solo se puede agregar un elemento)
lista.append("Nuevo_elemento 1")

print(lista)

################ INSERT ################
# Agrega un nuevo elemento a la lista en un lugar especifico
lista.insert(2,"Nuevo_elemento 2")

print(lista)

################ EXTEND ################
# Agrega varios elementos (una lista) a un lista
lista.extend([False,"Nuevo_elemento 3"])

print(lista)

################ POP ################
# Elimina un elemento de la lista en un lugar especifico
# Con -1 se elimina el ultimo elemento de la lista
# Con -2 se elimina el penultimo elemento de la lista, y asi sucesivamente
lista.pop(0)
lista.pop(-1)

print(lista)

################ REMOVE ################
# Elimina un elemento de la lista por su valor
# Si hay mas de 2 elementos con el mismo valor a eliminar, solo elimina el primero
# Si no encuentra el valor solicitado bota una excepcion
lista.remove(False)

print(lista)

################ CLEAR ################
# Elimina todos los elementos de la lista
lista.clear()

print(lista)

################ SORT ################
# Solo sirve si la lista tiene elementos numerios o Boleanos
# Ordena los elementos de una lista de manera ascendente por defecto
# Si se quiere ordenar de manera descendete se tiene que usar reverse=True
lista = [5, 0.0005, 1, 2, 7.7, 45, True, 23.44, 23,0 ,12, 59, False ]
lista.sort()
print(lista)

lista.sort(reverse=True)
print(lista)


################ REVERSE ################
# Invierte la posicion de los elementos de una lista
lista.reverse()
print(lista)


################ INDEX ################
# Verifica si un elemento esta dento de una lista, de ser el caso, bota la posicion del elemento, caso contrario bota un error
resultado = lista.index(5)
print(resultado)


