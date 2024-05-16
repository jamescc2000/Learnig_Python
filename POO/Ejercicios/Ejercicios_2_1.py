##################### Ejercicios 2 ##############################
# Ejercicio de Herencia y uso de Super:
# Crear un sistema para una escuela. En este sistema, vamos a tener
# dos clases principales: Persona y Estudiante. La clase Persona tendra
# los atributos de nombre y edad y un metodo que imprima el nombre y 
# la edad de la persona. La clase Estudiante heredara de la clase Persona
# y tambien tendra un atributo adicional: grado y un metodo que imprima el
# grado del estudiante.
# Deberas utilizar super en el metodo de inicializacion  (init) para reutilizar 
# el codigo de la clase padre (Persona). Luego crea una instancia de la clase
# Estudiante e inprime sus atributos y utiliza sus metodos para asegurarte de que
# todo funciona correctamente.

class Persona:
    def __init__(self,nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def mostrar_datos(self):
        print(f'Mi nombre es {self.nombre} y tengo {self.edad} años')
        
    
class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado = grado
        
    def mostrar_grado(self):
        print(f'El grado de {self.nombre} es {self.grado}')
        
james = Estudiante('James', 23, '5to')
print(james.nombre)
print(james.edad)
print(james.grado)
james.mostrar_datos()
james.mostrar_grado()