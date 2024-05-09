############################### ENRUTAMIENTO DE MODULOS ##############################################33
##### Si el modulo se encuentra dentro de la misma carpeta
import Funciones_buenas.Saludar as m_salud  #La estructura es la siguiente: Nombre_carpte.Nombre_modulo
import Funciones_buenas.Calculadora as cal
##### Si el modulo se encuntra en otra ruta
import sys
sys.path.append("c:\\Users\\james\\OneDrive - UNIVERSIDAD NACIONAL DE INGENIERIA\\Documentos\\Python\\Funciones_buenas_2") #Ruta donde se encuentra el modulo
import Saludar # Nombre del modulo
import Primos as prim # Nombre del modulo

print(Saludar.saludar("Pancho"))
print(m_salud.saludar("James"))
print(cal.Calcular('raiz', 27,3))
print(cal.elevar(5,4))
print(prim.es_primo(23))
print(prim.mostrar_numeros_primos_hasta(50))

#print(sys.path) # Para ver las rutas de los modulos

#print(sys.builtin_module_names) # Muestra todos los modulos integrados de python