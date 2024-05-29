################### METODOS DE DICCIONARIOS #####################
diccionario = {
    "nombre" : "James",
    "apellidos" : "Contreras",
    "Edad" : 23,
    "nombre" : "Mikey"
}

################ KEY ################
# Devuelve las claves del diccionario
# Tambien sirve para iterar los keys
resultado = diccionario.keys()

print(resultado)

################ GET ################
# Devuelve el valor de la clave introducida
# En caso haya claves repetidas, devuelve el ultimo valor de la clave
# Si no encuentra la claves solicitada, devuelve Nonce
resultado = diccionario.get("nombre")

print(resultado)

################ POP ################
# Elimina elementos del diccionario, dada una clave
# En caso una clave se repita mas de una vez, elimna todos las repeticiones tambien
diccionario.pop("nombre")

print(diccionario)

################ ITEMS ################
# Devuelve el diccionario pero lo convierte en iterable
resultado = diccionario.items()

print(resultado)

################ CLEAR ################
# Elimina todos los elementos del diccionario
diccionario.clear()

print(diccionario)



















