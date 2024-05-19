#################################### Metodos Dunder ###################################33

class Persona:
    def __init__(self, nombre, edad):
        self.nombre= nombre
        self.edad = edad
     
# Este metodo devuelve una representacion del objeto en una cadena de texto   
    def __str__(self):
        return f'Persona(nombre={self.nombre}, edad= {self.edad})' # Esto se mostrara cuando se ejecute print(objeto_persona)
    
    def __repr__(self):
        return f'Persona("{self.nombre}", {self.edad})' # Es necesario coloar las comillas si es sun string
    
    def __add__(self,otro):
        nuevo_valor = self.edad + otro.edad
        return Persona(f'{self.nombre}{otro.nombre}', nuevo_valor)
        


### Usando __str__
james = Persona('James', 23)
print(james)

### Usando __repr__
representacion = repr(james)
print(representacion)
resultado = eval(representacion)
print(resultado)

### Usando __add__
pepito = Persona('Pepito', 35)
lucia = Persona('Lucia', 20)

resultado = james + pepito + lucia
print(resultado.nombre)
print(resultado.edad)
print(resultado)



