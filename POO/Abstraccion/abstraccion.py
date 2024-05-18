####################################### Abstraccion ################################33
# Es el concepto de ocultar la complejidad interna de un sistema.
# No es necesario que el usuario sepa todo el proceso interno que realiza el sistema, sino para que sirve

class Auto():
    def __init__(self):
        self._estado = 'apagado' 
        
    def encender(self):
        self._estado = 'encendido'
        print('El auto esta encendido')
        
    def conducir(self):
        if self._estado == 'apagado':
            self.encender()
        
        print('conduciendo el auto')


mi_auto = Auto()
mi_auto.conducir()








