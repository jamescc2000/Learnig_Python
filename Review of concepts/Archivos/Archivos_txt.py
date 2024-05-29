############################# ARCHIVOS TXT ##########################
# Leer el archivo completo
archivo_sin_leer = open("Archivos\\texto.txt", encoding="UTF-8") # Se utiliza UTF-8 porque es el que admite todos los caracteres existentes
archivo = archivo_sin_leer.read() 
archivo_sin_leer.close() # Cuando un archivo se abre se tiene que cerrar, porque sino no se puede volver a utilziar
print(archivo)

# Leer linea por linea
archivo_sin_leer = open("Archivos\\texto.txt", encoding="UTF-8")
lineas = archivo_sin_leer.readlines() 
archivo_sin_leer.close()
print(lineas)

# Leer una sola linea
archivo_sin_leer = open("Archivos\\texto.txt", encoding="UTF-8")\
# No se recomienda usar para archivos muy grandes de texto porque consumiria mucha memoria ram
linea_1 = archivo_sin_leer.readline()  # Si no se coloca un argumento, lee la primera linea, caso contrario, muestra las cantidad de caracteres especificados
archivo_sin_leer.close()
print(linea_1)



########### LEER ARCHIVOS TXT CON WITH OPEN ######################
with open("Archivos\\texto.txt", encoding="UTF-8") as archivo:
    contenido = archivo.read()
    print(contenido)
    
    
    
################# ESCRIBIR EN ARCHIVOS TXT ########################
# Con el parametro "w", se indica que se va a sobreescribir el archivo
#Nota: si el archivo no existe, lo crea

with open("Archivos\\texto.txt", "w" ,encoding="UTF-8") as archivo:
    archivo.write("Esto es una nueva linea de texto\n") # Sobreescribiendo el archivo, es decir, eliminar el contenido y lo llena con el texto introducido en la funcion
    archivo.writelines(["Hola que tal? como te llamas?\n", "No me hables por favor\n"])

    
################# AGREGAR TEXTO EN ARCHIVOS TXT ########################
# Con el parametro "a", se indica que se va a agergar texto el archivo (append)

with open("Archivos\\texto.txt", "a" ,encoding="UTF-8") as archivo:
    archivo.write("Esto es otras nueva linea de texto\n") 
    archivo.writelines(["El publico no nos merece\n", "No le debemos nada al publico\n", "HH tlv\n"])


import sys
sys.path.append("c:\\Users\\james\\OneDrive - UNIVERSIDAD NACIONAL DE INGENIERIA\\Documentos\\Python\\Funciones_buenas_2")
import Primos as prim 

num = 100
num_primos = prim.mostrar_numeros_primos_hasta(num)

with open("Archivos\\texto.txt", "a" ,encoding="UTF-8") as archivo:
    archivo.write(f"Todos los numero primos hasta el {num} son:\n")
    for primo in num_primos:
        archivo.write(f"{primo}\n") 
