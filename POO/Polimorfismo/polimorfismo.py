######################### Polimorfismo #######################################3
# El mismo metodo funciona diferente para diferentes objetos
class Animal():
    pass

class Gato(Animal):
    def sonido(self):
        return 'Miua'
    
class Perro(Animal):
    def sonido(self):
        return 'Guau'
   
def hacer_sonido(animal):
    print(animal.sonido())
 
gato = Gato()
perro = Perro()

hacer_sonido(perro)
hacer_sonido(gato)

################################ Conceptos ###################################
########## Duck Typing ############
# El tipo o la clase de un objeto no es tan importante como los metodos o atributos que posee
# En lugar de verificar explícitamente el tipo de un objeto, se confía en su comportamiento
# Permite que las funciones y los metodos trabajen con cualquier objeto que tenga los metodos
# y atributos necesarios, sin importar la clase especifica del objeto
# Ejemplo:
class Duck:
    def quack(self):
        print('Quack!')

class Person:
    def quack(self):
        print('Im quacking like a duck!')
    
def make_it_quack(duck_like):
    duck_like.quack()

donald = Duck()
john = Person()

make_it_quack(donald) 
make_it_quack(john) 

################################## Tipos ##########################################
########## Tipo declarado ############
# Es el tipo de una variable según se especifica en el código fuente en tiempo de compilación

gato = Gato() # Gato vendria a ser el tipo declarado, porque es el que se se esta asignando

########## Tipo real ############
# Es el tipo del objeto al que realmente apunta una referencia en tiempo de ejecución

gato = Gato() # pero Animal vendria a ser el tipo real, porque es la clase padre de Gato

################################## Enlances ########################################
########## Enlances dinamicos ############
# las referencias a funciones y variables se resuelven cuando el programa
# se está ejecutando, y no todas las bibliotecas se incluyen en el archivo ejecutable

########## Enlances estaticos ############
# Todas las referencias a funciones y variables se resuelven cuando el
# programa es compilado y antes de que se ejecute

