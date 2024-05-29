################### METODOS DE CADENAS #####################
# Estructura: Dato.metodo()

cadena1 = 'Hola soy James'
cadena2 = 'Bienvenido mano'

################ DIR ################
# Devuelve la lista de atributos validos del objeto
# No es un metodo, es una funcion
resultado = dir(cadena1)

#print(resultado)

################ UPPER ################
# Convierte todo el texto a mayusculas
resultado = cadena1.upper()

print(resultado)

################ LOWER ################
# Convierte todo el texto a minusculas
resultado = cadena1.lower()

print(resultado)

################ CAPITALIZE ################
# Convierte las primeras letras en mayusculas
resultado = cadena1.capitalize()

print(resultado)


################ FIND ################
# Busca un valor en la cadena y devuelve la posicion del primer caracter
# En caso el valor es encontrado varias veces en la cadena, devuelve la posicion del primer valor
# Devuelve -1 cuando no encuentra un valor
resultado = cadena1.find('a')

print(resultado)


################ INDEX ################
# La diferencia entre find y index, es que index si no encuentra nada te devuelve un error
resultado = cadena1.index('James')

print(resultado)


################ ISNUMERIC ################
# Si el valor es numerico devuelve True
resultado = cadena1.isnumeric()

print(resultado)


################ ISALPHA ################
# Si el valor es alfanumerico devuelve True
# Solo son alfanumericos los caracteres de la A a la Z
resultado = cadena1.isalpha()

print(resultado)


################ COUNT ################
# Devuelve el numero de ocurrencia de un valor especifico dentro de la cadena
resultado = cadena1.count(' ')

print(resultado)


################ LEN ################
# Devuelve la cantidad de caracteres que tiene una cadena
# No es un metodo, es una funcion
resultado = len(cadena1)

print(resultado)


################ STARTWITH ################
# Devuele True si la cadena  empiza con el valor dado
resultado =  cadena1.startswith('Ho')

print(resultado)

################ ENDAWITH ################
# Devuele True si la cadena  termina con el valor dado
resultado =  cadena1.endswith('mes')

print(resultado)


################ REPLACE ################
# Reemplaza un valor de la cadena por otro valor dado solo si encuentra la coincidencia
resultado =  cadena1.replace(' ', '_')

print(resultado)


################ SPLIT ################
# Separa la cadena con el valor dado y devuelve una lista
resultado =  cadena1.split(' ')

print(resultado)



