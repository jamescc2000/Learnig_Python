############################################ Propiedades ###############################################

class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad
        
    @property # Decorador que le indica a python que la funcion es un getter
    def nombre(self):
        return self.__nombre
    
    @nombre.setter # Decorador que le indica a python que la funcion es un setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre
        
    @nombre.deleter # Decorador que le indica a python que se puede eliminar el atributo
    def nombre(self):
        del self.__nombre

james = Persona('James', 23)
nombre = james.nombre # Esto solo es posible gracias a @property
print(nombre)


james.nombre = 'Jaime' # Esto solo es posible gracias a @nombre.setter
nombre = james.nombre
print(nombre)


del james.nombre # Estos solo es posible gracias a @nombre.deleter

