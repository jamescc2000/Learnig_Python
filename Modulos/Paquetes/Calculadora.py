def Calcular(operacion,num1, num2 ):
    operacion.lower()
    if operacion == 'sumar':
        return num1 + num2
    elif operacion == 'restar':
        return num1 - num2
    elif operacion == 'multipicar':
        return num1 * num2
    elif operacion == 'dividir':
        return round(num1 / num2,3)
    elif operacion == 'elevar':
        return num1 ** num2
    elif operacion == 'raiz':
        return round(num1 ** (1/num2),3)
    else:
        return 'ERROR: Operacion no valida'
    
    
def sumar(num1, num2):
    return num1 + num2

def restar(num1, num2):
    return num1 - num2

def multipicar(num1, num2):
    return num1 * num2

def dividir(num1, num2):
    return round(num1 / num2,3)

def elevar(num1, num2):
    return num1 ** num2

def raiz(num1, num2):
    return round(num1 ** (1/num2),3)