from itertools import product

# Supongamos que tienes siete listas de siete elementos cada una
lista1 = [1, 2, 3, 4, 5, 6, 7]
lista2 = [8, 9, 10, 11, 12, 13, 14]
lista3 = [15, 16, 17, 18, 19, 20, 21]
lista4 = [22, 23, 24, 25, 26, 27, 28]
lista5 = [29, 30, 31, 32, 33, 34, 35]
lista6 = [36, 37, 38, 39, 40, 41, 42]
lista7 = [43, 44, 45, 46, 47, 48, 49]

# Obtener todas las combinaciones posibles
combinaciones = list(product(lista1, lista2, lista3, lista4, lista5, lista6, lista7))

# Imprimir las combinaciones
for combinacion in combinaciones:
    print(combinacion)
