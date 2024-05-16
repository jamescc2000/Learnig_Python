##################### Ejercicios 2 ##############################
# Ejercicio de Herencia multiple y MRO:
# Imagina que estas modelando animales en un zoologico. Crear tres
# clases: "Animal", "Mamifero" y "Ave". La clases "Animal" debe tener
# un metodo llamado "comer". La clase "Mamifero" debe tener un metodo 
# llamado "amamantar" y la clase "Ave" un metodo llamado "volar".
# Ahora, crea una clase "Murcielago" que herede de "Mamifero" y "Ave", 
# en ese orden, y por lo tanto debe ser capaz de "amamantar" y "volar" , 
# ademas de "comer".
# Finalmente, juega con el orden de herencia de la clase "Murcielago" y
# observa como cambia el MRO y el comportamiento de los metodos al usar super()

class Animal:
    def comer(self):
        print("Estoy comiendo")

class Mamifero(Animal):
    def amamantar(self):
        print("Estoy amamantando")
        
class Ave(Animal):
    def volar(self):
        print("Estoy volando")
        
class Murcielago(Mamifero, Ave):
    pass


murci = Murcielago()

print(Murcielago.mro())
murci.amamantar()
murci.volar()
murci.comer()