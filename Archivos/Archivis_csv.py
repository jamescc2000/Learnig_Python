############################# ARCHIVOS CSV ##########################

import _csv

with open("Archivos\\datos.csv", encoding='UTF-8') as archivo:
    reader = _csv.reader(archivo)
    for row in reader:
        print(row)
 
