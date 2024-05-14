###################################### Clases ######################################
# Para nombrar las clases, generalmente, se utiliza el metodo pascal cases que tiene la sigueinte estructura:
# SiempreLasPrimerasLetrasDeLasPalabrasVanEnMayusculas
# La estrucura de una clases es la siguiente:
##############################
class NombreClase():
    propiedad1 = 'valor1' # Estos son atributos estaticos
    propiedad2 = 'valor2'
    propiedad3 = 'valor3'
##############################

class CelularPrueba():
    marca = 'Samsung'
    modelo = 'S3'
    camara = '48MP'
  
#################################### Objetos #########################################
  
celular1 = CelularPrueba()

print(celular1.camara)

################ Atributos #######################3
class Celular:
    def __init__(self, marca, modelo, camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara


celular2 = Celular('Samsung', 'S23', '48MP')
print(celular2.marca)

celular3 = Celular('Apple', 'iPhone 15 pro', '96MP')
print(celular3.marca)


