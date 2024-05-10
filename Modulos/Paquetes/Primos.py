
def es_primo(num):
    for j in range (2,num):
        if num%j == 0:
            return False
            break
    return True



def mostrar_numeros_primos_hasta(num):
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
    return list_prim
