##################### Interface Segregation Principle ####################################
# Ningun cliente tiene que ser forzado a depender de interfaces que no utilice
# Eliminar las dependecias que no vamos a utilizar

from abc import ABC, abstractmethod

# En este caso no se estaria cumpliendo el principio de segregacion de interfaz

# class Trabajador(ABC):
    
#     @abstractmethod
#     def comer(self):
#         pass
#     @abstractmethod
#     def trabajar(self):
#         pass
    
#     @abstractmethod
#     def dormir(self):
#         pass
    
# class Humano(Trabajador):
#     def comer(self):
#         print('El humano esta comiendo')
    
#     def trabajar(self):
#         print('El humano esta trabajando')
    
#     def dormir(self):
#         print('El humano esta durmiendo')
        
        
# class Robot(Trabajador):
#     def trabajar(self):
#         print('El robot esta trabajando')
        
#     def comer(self):
#         pass
 
#     def dormir(self):
#         pass
        
# Esto seria la forma correcta:
class Trabajador(ABC):
    @abstractmethod
    def trabajar(self):
        pass
       
class Comerdor(ABC):
    @abstractmethod
    def comer(self):
        pass
    
class Durmiente(ABC):
    @abstractmethod
    def dormir(self):
        pass
    
    
class Humano(Trabajador, Durmiente, Comerdor):
    def comer(self):
        print('El humano esta comiendo')
    
    def trabajar(self):
        print('El humano esta trabajando')
    
    def dormir(self):
        print('El humano esta durmiendo')
        
  
class Robot(Trabajador):
    def trabajar(self):
        print('El robot esta trabajando')
        
        
skynet = Robot()
skynet.trabajar()

james = Humano()
james.trabajar()
james.comer()
james.dormir()