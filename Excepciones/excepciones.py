################################### Excepciones ########################################

def sumar_dos():

    while True:
        a = input('Numero 1: ')
        b = input('Numero 2: ')
        
        # Intentando convertir el numero a entero
        try:
            resultado = int(a) + int(b)
        
        # Si no se ingreso un valor numerico, le volvemos a pedir al usaurio que ingrese una numero
        except ValueError as e:
            print('Que fue mano? te pedí un numero, no te hagas el gracioso')
            print(f'ERROR: {e}')
    
        # Si todo salio bien se termina el bucle
        else:
            break
        finally:
            print('Esto se ejecuta siempre')
        
    return resultado

print(sumar_dos())


