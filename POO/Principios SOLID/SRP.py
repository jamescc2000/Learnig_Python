##################### Single Responsability Principle #####################33
# Una clase debe tener una y solo una razon para cambiar
# Esto significa que cada clase debe tener una unica responsabilidad o tarea

## Esto no se debe hacer, porque la clase auto se encarga de mas de
# class Auto():
#     def __init__(self) -> None:
#         self.posicion = 0
#         self.combustible = 100
        
#     def mover(self, distancia):
#         if self.combustible  >= distancia/2:
#             self.posicion += distancia
#             self.combustible -= distancia/2
#         else:
#             print('No hay suficiente combustible')
            
#     def agregar_combustible(self, cantidad):
#         self.combustible += cantidad
    
#     def obtener_combustible(self):
#         return self.combustible

### Esto es la forma correcta, usando SRP:
class Auto():
    def __init__(self, tanque) -> None:
        self.posicion = 0
        self.tanque = tanque
        
    def mover(self, distancia):
        if self.tanque.obtener_combustible()  >= distancia/2:
            self.posicion += distancia
            self.tanque.usar_combustible(distancia/2)
            print('Has moviso el auto exitosamente')
        else:
            print('No hay suficiente combustible')
            
    def obtener_posicion(self):
        return self.posicion

class TanqueDeCombustible():
    def __init__(self) -> None:
        self.combustible = 100
        
    def agregar_combustible(self,cantidad):
        self.combustible += cantidad
        
    def obtener_combustible(self):
        return self.combustible
    
    def usar_combustible(self, cantidad):
        self.combustible -= cantidad


tanque = TanqueDeCombustible()
autito = Auto(tanque)

print(f'Posicion: {autito.obtener_posicion()}')
print(f'Combustible: {tanque.obtener_combustible()}')
autito.mover(10)
print(f'Posicion: {autito.obtener_posicion()}')
print(f'Combustible: {tanque.obtener_combustible()}')
autito.mover(20)
print(f'Posicion: {autito.obtener_posicion()}')
print(f'Combustible: {tanque.obtener_combustible()}')
autito.mover(60)
print(f'Posicion: {autito.obtener_posicion()}')
print(f'Combustible: {tanque.obtener_combustible()}')
autito.mover(100)
print(f'Posicion: {autito.obtener_posicion()}')
print(f'Combustible: {tanque.obtener_combustible()}')
autito.mover(200)
print(f'Posicion: {autito.obtener_posicion()}')
print(f'Combustible: {tanque.obtener_combustible()}')