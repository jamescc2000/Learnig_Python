################################## Setters y Getters #################################
# Los Getters hacen referencia a una funcion que accede a un atributo privado o muy privado de una clase

class Persona():
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad
        
    def set_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre
        
    def set_edad(self, nueva_edad):
        self.__edad = nueva_edad

    def get_nombre(self):
        return self.__nombre
    
    def get_edad(self):
        return self.__edad


james = Persona('James', 23)
nombre = james.get_nombre()
edad = james.get_edad()
print(nombre)
print(edad)

james.set_nombre('Brayan')
nuevo_nombre = james.get_nombre()
print(nuevo_nombre)

james.set_edad(21)
nueva_edad = james.get_edad()
print(nueva_edad)
