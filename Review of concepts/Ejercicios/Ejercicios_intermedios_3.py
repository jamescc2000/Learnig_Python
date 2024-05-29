###################### EJERCICIOS INTERMEDIOS ######################
# Crea una funcion que devuelva la serie de fibonacci hasta el numero especificado

def serie_fibonacci(num):
    if num == 1: return 1
    elif  num == 2: return 2
    else: return serie_fibonacci(num-1) + serie_fibonacci(num-2)
        


def fibonacci(numero):
    list_fibonacci = [0,1]
    cont = 1
    while serie_fibonacci(cont) <= numero:
        list_fibonacci.append(serie_fibonacci(cont))
        cont +=1
    print(list_fibonacci)
        

fibonacci(25)