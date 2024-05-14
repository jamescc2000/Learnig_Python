############################### Ejercicio 1 #######################
# Crea una clase llamada estudiante que tenga los atributos: nomber, edad y grado
# Ademas, crea el metodo estudiar que imprmie lo siguiente: El estudiante(nombre) esta estudiando
# Crea un objeto Estudiante y usa el metodo estudiar()
# Para ello se debe interactuar con el usuario y este debe brindar los atributos
# Si despues ed registrar al estudiante el estudiante escribe estudiar (insdistinto de mayusculas o minusculas), utilizar el metodo estudiar


class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
    
    def estudiar(self):
        print(f'El estudiante {self.nombre} esta estudiando')
        
print('---------------------Bienvenido----------------------------------')
nombre1 = input('Ingrese su nombre: ')
edad1 = int(input('Ingrese su edad: '))
grado1 = input('Ingrese su grado: ')

estudiante1 = Estudiante(nombre1, edad1, grado1)

print(f'''
------------------------------------------------------------------
Datos del Estudiante:
      Nombre: {estudiante1.nombre} 
      Edad: {estudiante1.edad}
      Grado: {estudiante1.grado}
------------------------------------------------------------------
      ''')
while (True):
    accion = input()
    if accion.lower() == 'estudiar':
        estudiante1.estudiar()