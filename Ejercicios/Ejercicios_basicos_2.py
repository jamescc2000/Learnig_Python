###################### EJERCICIOS BASICOS 2 ######################3
# Suponiendo que cada persona en promedio habla:
word_per_seg_prom = 2 # 2 palabras por segundo

# a) Pedirle al usuario que diga cualquier texto real y:
#   - Calcular cuanto tardaria en decir esa frase
#   - Cuantas palabras fueron las que dijo

texto = input("Escribe el texto que deseas hablar: ")
lista_palabra = texto.split(' ')
tiempo = (len(lista_palabra))/word_per_seg_prom
print(f'Tardarias {tiempo} segundos en decir esa frase')
print(f'En total dijiste {len(lista_palabra)} palabras')

# b) Si tarda mas de 1 minuto decirle : Para flaco tampoco te pedí un testamento
if tiempo > 60:
    print("Para flaco tampoco te pedí un testamento")

# c) Dalto habla un 30% mas rapido, Cuanto tardaria en decirlo?

word_per_seg_dalton = word_per_seg_prom*1.3
tiempo_dalto = (len(lista_palabra))/word_per_seg_dalton
print(f"Dalto tardaria en decirlo solo {tiempo_dalto} segundos")









