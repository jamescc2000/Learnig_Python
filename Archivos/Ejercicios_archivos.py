# Tenemos 2 listas: 1 tiene nomber y la otra tiene apellidos
# Escribe los datos, de forma optima, en un archivo de texto con un for

nombres = ['James', 'Pedro', 'Juanito', 'Michael', 'Jorge', 'Ricardo']
apellidos = ['Contreras', 'Navaja', 'Alimaña', 'Jackson', 'Luna', 'Mendoza']

with open ("Archivos\\ejercicio_archivos.txt", 'a', encoding='UTF-8') as archivo:
    archivo.writelines('Los datos son:\n\n')
    #for i in range(len(nombres)):
    #    archivo.writelines([nombres[i], ' ', apellidos[i], '\n'])
    [archivo.writelines(f'Nombre: {n}\nApellido: {a}\n------------------------\n') for n,a in zip(nombres,apellidos)]
