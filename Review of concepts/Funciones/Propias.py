###################### FUNCIONES PROPIAS ######################
# Funcion que no retorna valores

def saludar(nombre, edad, adjetivo = "tonto"): # Seteamos por defecto el valor de adjetivo y se convierte en un parametro opcional
    
    if edad < 18:
        print(f'Hola {nombre} de {edad} años, como estas? todo bien? todo correcto {adjetivo}?')
    elif edad >= 18 and edad <=30:
        print(f'Hola {nombre} de {edad} años, como estas? abduskan {adjetivo}')
    else:
        print(f'Hola {nombre} de {edad} años, como estas? que cuenta la familia {adjetivo}?')


saludar("James", 23) # Como no se especifica el adjetivo, utiliza el valor por defecto
saludar("Miguel", 12, "chibolo") # El valor por defecto de adjetivo cambia a "chibolo"
saludar(adjetivo= "viejo" ,edad= 45, nombre = "Juanito Alimaña" ) # Podemos ingresar los datos en desorden siempre y cuando especifiquemos los keywords


# Funcion que retorna valores

def crear_contra_random(numero):
    char = 'abcdefghijklmnopqrstwxyz'
    numero_ = str(numero)
    numero = int(numero_[0])
    c1 = numero + 2
    c2 = numero
    c3 = numero + 5
    contra = f'{char[c1]}{char[c2]}{char[c3]}{numero*2}'
    return contra, numero
    

nueva_contra, num = crear_contra_random(342)

print(f'Tu contraseña nueva es: {nueva_contra} y se utilizo el numero {num}')


# Forma no optima
def suma(lista):
    suma = 0
    for num in lista:
        suma += num
        
    return suma

resultado = suma([4,3,7,8])
print(resultado)


# Forma optima
def opt_suma(nombre, *numeros): # El * convierte la entrada en una tupla / siempre se usa al final
    return f'Hola {nombre}, la suma de tus numeros {numeros} es igual: {sum(numeros)}'
    

resultado = opt_suma("James",4,3,7,8)
print(resultado)
