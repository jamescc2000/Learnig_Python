################################# DICCIOANRIO ###################################
# Creando un diccionario con la funcion dict()
diccionario = dict(nombre = "James", apeliido = "Contreras", edad = 23)

print(diccionario)

# Las listas ni los set (a menos que se use frozenset()) no pueden ser claves porque son mutables
# La tuplas si pueden ser claves
diccionario_tupla = {("James", "Rancio"): "jajas"}
diccionario_set = {frozenset(["James", "Rancio"]): "jajas"}

print(diccionario_tupla)
print(diccionario_set)

# Creando diccionario con fromkeys()
diccionario1 = dict.fromkeys(["nombre", "apellidos"]) # Setea todos los valore en None
diccionario2 = dict.fromkeys("ABCDEF", 0) # Itera el primer elemento y le da el valor del segundo
diccionario3 = dict.fromkeys(['a', 'b', 'c'], 100) # Itera el primer elemento y le da el valor del segundo

print(diccionario1)
print(diccionario2)
print(diccionario3)