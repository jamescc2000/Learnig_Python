############################# FUNCIONES LAMBDA ########################
# La estructura es la siguiente:
# nombre_funcion = lambda parametro : expresion
# Lamdda crea funciones anonimas que despues podemos almacenar en variables
# Se utiliza principalmente cuando queieres crear un funcion sencilla y rapida
multiplicar = lambda x : x*2
print(multiplicar(7))


numeros = [11,5,71,2,65,64,78]
numeros_pares = list(filter(lambda num : num%2 == 0, numeros))

print(numeros_pares)