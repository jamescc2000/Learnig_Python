##################### Ejercicios 3 ##############################
# El juego consiste en crear un personaje de un juego y que esos 
# personajes se puedan fusionar para formar personajes mas poderosos
# que tengan mas poder...
# Para ello deberemos cambiar el comportamiento del operador "+" para
# que cuando los personajes se fusionen, salga un nuevo personaje con
# habilidades mejoradas
# Una posible formula es: el promedio de las habilidades de ambos al cuadrado


class Personaje:
    def __init__(self, nombre, fuerza, velocidad):
        self.nombre = nombre
        self.fuerza = fuerza
        self.velocidad = velocidad
    
    def __repr__(self) -> str:
        return f'{self.nombre} (fuerza: {self.fuerza}, velocidad: {self.velocidad})'
    
    def __add__(self, otro):
        nuevo_nombre = self.nombre + '-' + otro.nombre
        nueva_fuerza = round(((self.fuerza + otro.fuerza)/2)**1.5,2)
        nueva_velocidad = round(((self.velocidad + otro.velocidad)/2)**1.5,2)
        return Personaje(nuevo_nombre, nueva_fuerza, nueva_velocidad)

goku = Personaje('Goku', 100, 100)
print(goku)

vegeta = Personaje('Vegeta', 99,99)
print(vegeta)

jiren = Personaje('Jiren', 130,140)
print(jiren)

gogeta = goku + vegeta 
print(gogeta)

jireta = gogeta + jiren
print(jireta)

