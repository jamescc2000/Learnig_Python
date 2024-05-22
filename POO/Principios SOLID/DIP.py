##################### Dependency Inversion Principle ####################################
# Los modulos de alto nivel no deben depender de los modulos de bajo nivel, sino que ambos deben depender de las abstracciones
# Las abstracciones no deben depender de los detalles, sino que los detalles deben depender de las abstraccioens

# En este caso no se estaria cumpliendo el principio de inversion de dependencias

# class Diccionario:
#     def verificar_palabras(self, palabra):
#         #Logica para verificar palabras
#         pass
    
# class CorrectorOrtografico:
#     def __init__(self) -> None:
#         self.diccionario = Diccionario()
        
#     def corregir_texto(self, texto):
#         #Usamos el diccionario para corregir el texto
#         pass

       
# Esto seria la forma correcta:
from abc import ABC, abstractmethod

class VerificadorOrtografico(ABC):
    @abstractmethod
    def verificar_palabra(self, palabra):
        #Logica para verificar palabras
        pass
    
class Diccionario(VerificadorOrtografico):
    def verificar_palabra(self, palabra):
        #Logica para verificar palabras si esta en el diccionario
        pass
    
class ServicioOnline(VerificadorOrtografico):
    def verificar_palabra(self, palabra):
        #Logica para verificar palabras desede el servicio web
        pass
    
class CorrectorOrtografico:
    def __init__(self, verificador) -> None:
        self.verificador = verificador
        
    def corregir_texto(self, texto):
        #Usamos el verificador para corregir texto
        pass
        
        
corrector = CorrectorOrtografico(Diccionario())
corrector = CorrectorOrtografico(ServicioOnline())