##################################### Encapsulamiento ################################################
# En Python, no existen los atributos privados, de una u otra forma se peuden acceder a estos atributos
# El encapsulamiento mejora la legilibilidad del codigo, el mantenimiento y la escalacion

class MiClase:
    def __init__(self):
# Los atributos privados se definen con un "_" al inicio del nombre 
# (En si solo es una nomenclatura universal para los atributos privados, no afecta al codigo)       
        self._atributo_privado = "Valor privado"
# Los atributos muy privados se definen con dos "_" al inicio del nombre
# (Estos sis afectan al codigo y arroja un error si se intenta acceder a el)       
        self.__atributo_muy_privado = "Valor muy privado" 
# Lo mismo aplica para los metodos        
    def _hablar_en_privado(self):
        print('Hola, como estas?')
        
    def __hablar_muy_privado(self):
        print('Hola, como estas?')
    
    
    
objeto = MiClase()
print(objeto._atributo_privado)
#print(objeto.__atributo_muy_privado)
#objeto._hablar_en_privado()
#objeto.__hablar_muy_privado()

