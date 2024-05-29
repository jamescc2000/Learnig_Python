from bs4 import BeautifulSoup
import requests

# url de la pagina que se desea scrappear
url = 'https://www.newegg.ca/black-gigabyte-g6-series-g6-kf-h3us854kh-gaming/p/N82E16834233581?Item=N82E16834233581&SoldByNewegg=1'

# Creamos el htpp get request
result = requests.get(url)

# parseamos el get requets a html con bs
doc = BeautifulSoup(result.text, 'html.parser')

# Buscamos todos los textos que tenga $
prices = doc.find_all(string ='$')

# Obtenemos el parent del primer texto encontrado con $
parent = prices[0].parent

# Buscamos el tag strong, que es el que contiene el valor del articulo
precio = parent.find('strong').string

# Ahora buscamos el nombre del producto, en este caso se cuentrada entro de un h1
product_name = doc.find_all('h1')[0].string

# Finalmente mostramos el nombre y el precio
print(f'''
***************** Producto encontrado *****************
Nombre: {product_name[:17]}
precio: {precio}
*******************************************************
''')

