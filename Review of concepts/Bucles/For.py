######################### FOR #######################
# Para listas y tuplas funcionan exactamente igual, y para sets funciona casi igual salvo algunas pequeñas diferencias

animales = ["gato", "perro", "loro", "cocodrilo"]
numeros = [10,62,12,72]

for animal in animales:
    print(f'Ahora la variable animal es igual a: {animal}')

for numero in numeros:
    resultado = numero*10
    print(resultado)
    
# Recorriendo dos lista del mismo tamaño al mismo tiempo con la funcion zip()
for animal,numero in zip(animales, numeros):
    print(f'Recorriendo lista animales con valor {animal} y lista numero con valor {numero}')
    
# Forma no optima de recorer una lista (esta forma no funciona para set)
for num in range(len(numeros)):
    print(numeros[num])
    
# Forma correcta de recorre una lista con su indice
for num in enumerate(numeros): # Ahora num es una tupla (indice, valor)
    indice = num[0]
    valor = num[1]
    print(f'El numero {valor} esta en el indice {indice}')
 
# Forma correcta y elegante de recorre una lista con su indice   
for i, num in enumerate(numeros): # i toma el valor del indice y num el valor de la lista en ese indice
    print(f'El numero {num} esta en el indice {i}')
    
    
# Usando el for - else
for numero in numeros:
    print(f'Ejecutando el ultimo bucle, valor actual: {numero}')
else:
    print('El bucle termino')
    
# Usando continue
for animal in animales:
    if animal == 'cocodrilo':
        continue # Sirve para saltarse a la siguiente iteracion, evitando que se ejecute el codigo posterior
    print(f'Me gustan los {animal}s')


# Usando break
for numero in numeros:
    if numero == 12:
        print(f'Tenemos un gandor, gracias por participar, adios')
        break # Sirve para terminar el bucle / tambien evita que se ejecute el Else, si es qie existe
    print(f'El numero que salio es el {numero}')
else:
    print(f'El bucle termino de ejecutarse')
    
###################### ITERANDO DICCOINARIOS ###############################

diccionario = {
    "nombre" : "James",
    "apellido" : "Contreras",
    "edad" : 23
}

#Recorriendo el diccionario para obtener las claves
for key in diccionario:
    print(key)

# Recorreindo el diccionario con la funcion items() para obtener las claves y los valores
for key, valor in diccionario.items():
    print(f'La clave {key} tiene el valor de: {valor}')
    

######################### ITERANDO UN STRING ####################

texto = "James Conteras Campos"

for letra in texto:
    print(letra)
    
# For en una sola linea de codigo
numero_duplicados = [x*2 for x in numeros]
print(numero_duplicados)