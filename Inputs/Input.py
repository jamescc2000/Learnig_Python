################### INPUT #####################
# Sirve para solicitarle un dato al usuario
# El dato de vuelve input siempre es un string
nombre = input("Dame tu nombre: ")

print(f'El nombre es: {nombre}')

# Para trbajar con numero, primero se tiene que convertir al tipo numerico que se desea
numero = int(input("Dame un numero: "))

# Nota: Si el usuario ingresa un numero flotante en vez de uno entero el programa bota error
numero *= 2

print(numero)

flotante = float(input("Dame un numero decimal: "))

flotante *= 2
print(flotante)








