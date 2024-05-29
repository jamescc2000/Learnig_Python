############################################# DATOS COMPUESTOS ##########################################
############# LISTAS ##########
lista = ["James Contreras", 23,1.65 , True]
print(lista)
print(lista[1])


############# TUPLAS ##########
# La diferencia con las lsitas, es que las tuplas no se pueden modificar
tupla = ("James Contreras", 23,1.65 , True)  
print(tupla)
print(tupla[0])


############# SET ##########
# No tienen un orden fijo. No se puede modificar un elemento pero si se puede redefinir todo el set
# No se pueden repetir valores dentro del conjunto
# Tampoco se puede acceder a los elementos, es decir no puedes utilizar conjunto[i]
conjunto = {"James Contreras", 23,1.65 , True}  
print(conjunto) 


############# DICCIONARIO ##########
#En vez de definir los elementos por indices, se definen por claves
diccionario = {
    'nombre': 'James Conteras',
    'Edad': 23,
    'Altura': 1.65,
    'Egresado': True
}
print(diccionario['Altura'])



