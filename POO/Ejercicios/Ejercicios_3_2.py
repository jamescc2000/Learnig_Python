##################### Ejercicios 3 ##############################
# Ahora crea una inferza donde el usuario pueda interactuar y pueda realiza las siguiente accioesn:
# Crea un personaje
# Fusionar personajes (Solo los personajes disponibles)
# Mostrar personajes
# Salir de la interfaz

class Personaje:
    def __init__(self, nombre, fuerza, velocidad):
        self.nombre = nombre
        self.fuerza = fuerza
        self.velocidad = velocidad
    
    def __repr__(self) -> str:
        return f'####### {self.nombre} #######\nFuerza: {self.fuerza} \nVelocidad: {self.velocidad}\n'
    
    def __add__(self, otro):
        nuevo_nombre = self.nombre + '-' + otro.nombre
        nueva_fuerza = round(((self.fuerza + otro.fuerza)/2)**1.5,2)
        nueva_velocidad = round(((self.velocidad + otro.velocidad)/2)**1.5,2)
        return Personaje(nuevo_nombre, nueva_fuerza, nueva_velocidad)

continuar = True
lista_personajes =[]

while(continuar):
    print(f'1. Crear un personaje\n2. Fusionar personajes\n3. Mostrar personajes\n4. Salir\n')
    opcion = input('Elija una opcion: ')

    try:
        opcion = int(opcion)
        
        if opcion == 1:
            print('\nIngrese los siguiente datos del personaje:')
            nombre = input('Nombre: ')
            fuerza = input('Fuerza: ')
            val_fuerza = True
            
            while(val_fuerza):
                try:
                    fuerza = int(fuerza)
                    val_fuerza = False
                    
                except ValueError:
                    print('\nDebe ingresar un numero\n')
                    fuerza = input('Fuerza: ')
            
            velocidad = input('Velocidad: ')
            val_velocidad = True
            
            while(val_velocidad):
                try:
                    velocidad = int(velocidad)
                    val_velocidad = False
                except ValueError:
                    print('\nDebe ingresar un numero\n')
                    velocidad = input('Velocidad: ')
            
                
            nuevo_pj = Personaje(nombre, fuerza, velocidad)
            
            print('\nPersonaje creado con exito!\n')
            lista_personajes.append(nuevo_pj)
        
        elif opcion == 2:
            if len(lista_personajes) > 1:
                print('\nLista de personajes disponibles:')
                for i, personaje in enumerate(lista_personajes):
                    print(f'{i+1}. {personaje.nombre}')
                    
                opcion_pj = input('\nElija los personajes a fusionar: ')
                val_opcion_pj = True
                while(val_opcion_pj):
                    try:
                        idx_pj_selecd = list(map(int, opcion_pj.split()))
                        val_opcion_pj = False
                    
                    except ValueError:
                        print('\nPor favor ingrese una opcion valida\n')
                        opcion_pj = input('\nElija los personajes a fusionar: ')
                        
                fusion = lista_personajes[idx_pj_selecd[0]-1]
                for i, idx_pj in enumerate(idx_pj_selecd):
                    if i > 0:
                        fusion = fusion + lista_personajes[idx_pj_selecd[i]-1]
                
                print(f'\nFusion realizada correctamente!\n')
                print(fusion)
                lista_personajes.append(fusion)         
                
                
            else:
                print('\nNo hay personajes suficientes para fusionar :(\n')
            
        elif opcion == 3:
            
            if len(lista_personajes) > 0:
                print('\nLista de Personajes:\n')
                for personaje in lista_personajes:
                    print(personaje)
            else:
                print('\nNo hay personajes para mostrar :(\n')
            
        else:
            continuar = False
        
    except ValueError:
        print('\nPor favor ingrese una opcion valida\n')
    
    

    