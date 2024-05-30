from bs4 import BeautifulSoup
import requests
import pandas as pd

# Obtenemos los datos html de la pagina
url = 'https://coinmarketcap.com/'
result = requests.get(url).text
doc = BeautifulSoup(result, 'html.parser')

# Buscamos la tabla, que es la que contiene los datos de las criptos
table = doc.tbody

# Obtenemos las filas de la tabla
t_rows = table.contents

# Como las filas estan en el mismo nivel, esta son 'siblings' por ende se puede usar los siguiente comandos:
primera_fila = t_rows[0]
primera_fila = t_rows[1].previous_sibling
segunda_fila = t_rows[0].next_sibling
todas_menos_la_primera = list(t_rows[0].next_siblings)

# En este caso el padre de las filas seria la tabla
parent = t_rows[0].parent.name


################## Obteniendo los datos de las criptos #####################
criptos = []

for i, row in enumerate(t_rows):
    
    # De las filas, solo obtenemos la informacion del nomber y el precio
    cripto_name, cripto_price = row.contents[2:4]
    
    # El top 10 tiene una estrucutura diferente a las demas criptos
    if i < 10 :
        
        # El nombre estan en los tag p
        cripto_name = cripto_name.p.string
        
        # Los precios estan en los tag span
        cripto_price = cripto_price.span.string
    
    # Estructura de las demas criptos 
    else:
        
        # Los nombres estan en el segundo span
        cripto_name = cripto_name.find_all('span')[1].string
        
        # Los precios estan directo en el td 
        # pero como son 3 valores que tiene, solo elejimos el 1 ($) y el 3 (monto/precio)
        cripto_price = ''.join(cripto_price.contents[::2])
        
    # Guardamos los datos en una lista (rank, nombre y precio)
    criptos.append([i+1,cripto_name, cripto_price])

# Convertimos la lista en un dataframe
df = pd.DataFrame(criptos,  columns=['Rank', 'Nombre', 'Precio'])
print(df)