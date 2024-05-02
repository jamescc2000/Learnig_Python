################3######## DESEMPAQUETADO ############################33

datos_en_tupla = ("James", "Contreras", 23)
datos_en_lista = ["Juanito", "Alimaña", 35]
datos_en_set = {"Pancho", "Lopez", 47}
datos_en_diccionario ={
    'nombre' : 'Benito',
    'apellido' : 'Tapuja',
    'edad' : 28
}

nombre, apellido, edad = datos_en_tupla
nombre_l, apellido_l, edad_l = datos_en_lista
nombre_s, apellido_s, edad_s = datos_en_set
nombre_d, apellido_d, edad_d = datos_en_diccionario
# La cantidad de variables asignadas debe ser igual a la cantidad de datos que tiene el array, sino bota error

print(f'Hola {nombre} {apellido} de {edad} años')
print(f'Hola {nombre_l} {apellido_l} de {edad_l} años')
print(f'Hola {nombre_s} {apellido_s} de {edad_s} años')
print(f'Hola {nombre_d} {apellido_d} de {edad_d} años')
