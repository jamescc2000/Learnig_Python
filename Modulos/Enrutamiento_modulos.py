############################### ENRUTAMIENTO DE MODULOS ##############################################33
##### Si el modulo se encuentra dentro de la misma carpeta
import Funciones_buenas.Saludar as m_salud  #La estructura es la siguiente: Nombre_carpte.Nombre_modulo

##### Si el modulo se encuntra en otra ruta
import sys
sys.path.append("c:\\Users\\james\\OneDrive - UNIVERSIDAD NACIONAL DE INGENIERIA\\Documentos\\Python\\Funciones_buenas_2") #Ruta donde se encuentra el modulo
import Saludar # Nombre del modulo

print(Saludar.saludar("Pancho"))
print(m_salud.saludar("James"))

#print(sys.path) # Para ver las rutas de los modulos

#print(sys.builtin_module_names) # Muestra todos los modulos integrados de python