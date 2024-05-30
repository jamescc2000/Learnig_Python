from bs4 import BeautifulSoup
import re
import requests
from itertools import permutations

# Solicitamos al usuario el producto que desea buscar
product = input('Que producto quieres buscar? ')

# cambiamos la estructura del nombre del producto para poder buscarlo en la pagina
product_link = product.replace(' ', '+')
url = f'https://www.newegg.ca/p/pl?d={product_link}&N=4131'

# Obtenemos los datos de la pagina
page = requests.get(url).text
doc = BeautifulSoup(page, 'html.parser')

# Buscamos el numero total de paginas para el resultado de la busqueda
page_text_tag = doc.find(class_ ='list-tool-pagination-text')
pages = int(page_text_tag.strong.text.split('/')[1])

items_found = {}

# Inicializamos una iteracion por cada pagina de resultado del producto
for page in range(1,pages+1):
    
    # Obtenemos los datos de la pagina
    url = f'https://www.newegg.ca/p/pl?N=4131&d={product_link}&page={page}'
    page = requests.get(url).text
    doc = BeautifulSoup(page, 'html.parser')
    
    # Buscamos el tag que contiene la informacion de cada producto enontrado
    div = doc.find(class_ = 'item-cells-wrap border-cells short-video-box items-grid-view four-cells expulsion-one-cell')
    
    # Buscamos aquellos productos que coincidan con el nomber del producto requerido por el usuario
    # Para ello se crea un patron que realice una busqueda compleja en cada nomber de producto
    
    # Primero separamos cada palabra del nombre del producto
    product_words = product.split()

    # Luego generamos todas las permutaciones posibles de las palabras del producto
    perms = permutations(product_words)

    # Creamos una lista de patrones que buscan las palabras en cualquier orden, permitiendo cualquier texto entre ellas
    patterns = []
    for perm in perms:
        pattern = r'\b' + r'\b.*?\b'.join(perm) + r'\b'
        patterns.append(pattern)

    # Unimos todos los patrones con el operador OR
    full_pattern = '|'.join(patterns)
    
    # Finalmente, buscamos todos los texto que coincidan con el patron de busqueda,
    # Ademas usamos el IGNORECASE para no preocuparnos las mayusuclas y minusculas
    items = div.find_all(string=re.compile(full_pattern, re.IGNORECASE))
    
    # Inicializamos la iteracion por cada producto encontrado
    for item in items:
        
        # Obtenemos el tag padre
        parent = item.parent
        
        # Filtramos aquellos que no sean un tag a, porque no contienen informacion necesaria y nos daria error
        if parent.name != 'a':
            continue
        
        # Ahora, como estamos seguros de que solo estamos trabajando con los tag a, utilizamos su atributo href para obtener el link del producto
        link = parent['href']
        
        # Buscamos el tag padre de los productos
        next_parent = item.find_parent(class_='item-container')
        
        # Usamos un try porque hay elementos que no van a cumplir las condiciones siguientes
        try: 
            
            # La estructura del precio en esta pagina separa la parte entera de la decimal
            # Entonces primero obtenemos la parte entera que se encuentra dentro de una etiqueta strong
            int_price = next_parent.find(class_='price-current').strong.text.replace(',','')
            
            # Luego obtenemos la parte decimal que se encuentra dentro de una etiqueta sup
            decimal_price = next_parent.find(class_='price-current').sup.text
            
            # Finalmente unimos las dos parte y lo convertimos en un float
            price = float(f'{int_price}{decimal_price}')
            
            # Agreamos todos los datos encontrados del producto a un diccionario
            items_found[item] = {"price" : price, "link" : link}
            
        except:
            pass
        
# Ordenamos el diccionario de mayor a menor precio usando una funcion lambda
sorted_items = sorted(items_found.items(), key=lambda x:x[1]['price'])

# Mostramos los resutlados encontrados al usuario
for item in sorted_items:
    print(f'\nNombre: {item[0]}')
    print(f'Precio: ${item[1]['price']}')
    print(f'Link: {item[1]['link']}')
    print('*******************************')