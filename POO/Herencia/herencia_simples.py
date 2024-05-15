################################## Herencia Simple #################################3
class Persona:
    def __init__(self, nombre, edad,nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
        
    def hablar(self):
        print('Hola estoy hablando un poco')
        
class Empleado(Persona):
    def __init__(self, nombre, edad, nacionalidad, trabajo, salario): # Se pueden agregar nuevas propiedades
        super().__init__(nombre, edad, nacionalidad)
        self.trabajo = trabajo
        self.salario = salario
     
    def hablar(self):  # Se pueden sobreescribir los metodos  
        print('No')
        
class Estudiante(Persona):
    def __init__(self, nombre, edad, nacionalidad, notas, universidad):
        super().__init__(nombre, edad, nacionalidad)
        self.notas = notas
        self.universidad = universidad

            

roberto = Empleado('Roberto', 43, 'argentino', 'Programador', 100000)

print(roberto.nacionalidad)

roberto.hablar()