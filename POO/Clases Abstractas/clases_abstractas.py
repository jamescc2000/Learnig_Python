###################################### Clases Abstractas ###############################

from abc import ABC, abstractmethod

class Persona(ABC):
    @abstractmethod
    def __init__(self, nombre, edad, sexo, actividad):
        self.nombre = nombre
        self.edad = edad
        self.sexo =sexo
        self.actividad = actividad
        
    @abstractmethod
    def hacer_actividad(self):
        pass
    
    def presentarse(self):
        print(f'Hola, me llamo {self.nombre} y tengo {self.edad} años')


class Estudiante(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)
        
    def hacer_actividad(self):
        print(f'Estoy estudiando {self.actividad}')


class Trabajador(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)
        
    def hacer_actividad(self):
        print(f'Actualmente estoy trabajando de {self.actividad}')



james = Estudiante('James', 23, 'Masculino', 'programacion')
james.presentarse()
james.hacer_actividad()

scarllet = Trabajador('Scarllet', 29, 'Femenino', 'Arquitecta')
scarllet.presentarse()
scarllet.hacer_actividad()
