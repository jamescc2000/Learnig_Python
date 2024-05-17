###################################### Decoradores ###################################
# Agrea una funcionallidad a otra funcion antes y despues de jecutar dicha funcion

# Definiendo el decorador
def decorador(funcion):
    def funcion_modificada():
        print('Antes de llamar a la funcion')
        funcion()
        print('Despuesde llamar a la funcion')
    return funcion_modificada

# Forma no optima de llamar al decorador
def saludo():
    print('Hola mundo no optimo')
    
    
saludo_modificado = decorador(saludo)
saludo_modificado()

print('------------------------------------------------------')
# Forma optima de llamar al decorador
@decorador
def saludo():
    print('Hola mundo optimo')
    
saludo()