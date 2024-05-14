################################## Metodos ######################################
# Los metodos son las funciones que estan dentro de las clases

class Celular:
    def __init__(self, marca, modelo, camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara
        
    def llamar(self):
        print(f'Estas haciendo una llamada desde un: {self.modelo}')
        
    def cortar(self):
        print(f'Cortaste la llamada desde tu: {self.modelo}')
        
celular1 = Celular('Samsung', 'S23', '48MP')
celular1.llamar()
celular1.cortar()