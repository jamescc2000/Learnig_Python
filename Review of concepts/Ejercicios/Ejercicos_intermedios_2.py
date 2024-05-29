###################### EJERCICIOS INTERMEDIOS ######################
# Crea una funcion tome como parametro un numero y que devuelva todos los numeros primos menores o iguales a dicho numero

def es_primo(num):
    for j in range (2,num):
        if num%j == 0:
            return False
            break
    return True


def num_primos(num):
    list_prim = []
    if num == 1:
        return list_prim
    else :
        for i in range(2, num+1):
            if i == 2:
                list_prim.append(i)
            else:
                if i%2 != 0:
                    if es_primo(i):
                         list_prim.append(i)

    print(list_prim)
    

num_primos(120)