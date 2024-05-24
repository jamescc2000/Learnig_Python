# Creando mi propia excepcion
class MiExcepcion(Exception):
    def __init__(self, err) :
        print(f'Impresionante, cometiste el siguiente error: {err}')
      
# Lanzando mi propia excepcion        
#raise MiExcepcion('Jajaja persona poco culta')    

# Manejando mi propia excepcion        
try:
    raise MiExcepcion('Jajaja persona poco culta')
except:
    print('Como vas a cometer ese error')
    
    
