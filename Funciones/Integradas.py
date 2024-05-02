######################## FUNCIONES INTEGRADAS ####################3
################ MAX ##############
# Se utiliza para encontrar el numero mayor de un arreglo
# Solo sirve si los valores son numericos, en caso haya algun string, bota error
numeros = [4, 52, 100, 21, 85, 104]

print(max(numeros))


################ MIN ##############
# Se utiliza para encontrar el numero menor de un arreglo
# Solo sirve si los valores son numericos, en caso haya algun string, bota error
numeros = {97,6,18,22,77}

print(min(numeros))


############### ROUND ################
# Sirve para redondear un valor numerico
numero = 12.4865812

print(round(numero,3)) # Redonde el numeor a 3 decimales


############### BOOL ################
# Devuelve False si recibe como entrada: 0 , vacio/null, False
# Caso contrario devuelve True
resultado = bool()
print(resultado)

resultado = bool(0)
print(resultado)

resultado = bool(78)
print(resultado)

resultado = bool('aa')
print(resultado)


############### ALL ################
# Devuelve True si todos los valores son True
# Caso contrario devuelve False

resultado = all([12, 87, 45, 78, 'Valor'])
print(resultado)

resultado = all([12, 0, 45, 78, 'Valor'])
print(resultado)


################### SUM #############
# Devuelve la suma de todos los valores de un iterable

suma = sum(numeros)
print(suma)


################### FILTER #############
# Evalua una funcion con los parametros de una lista y devuelve solo aquellos valores de la lista donde el resultado es True
numeros = [1,5,7,2,65,64,78]

def es_par(num):
    if num%2 == 0:
        return True
    else:
        False

numeros_pares= list(filter(es_par, numeros))

print(numeros_pares)