from bs4 import BeautifulSoup
import re

with open("BeautifulSoup//index2.html", "r") as f:
    doc = BeautifulSoup(f, 'html.parser')
    
# Buscando un tag 
tag = doc.find('option')

# Ver que atribtos tiene el tag
print(tag.attrs)

# Cambiando el valor de los atributos del tag
tag['selected'] = 'false' 
tag['color'] = 'blue'

# Cambiamos el atributo placeholder de los inputs
tags = doc.find_all('input', type='text')
for tag in tags:
    tag['placeholder'] = 'I changed you!'

# Gaurdamos los cambios en un nuveo html
with open('BeautifulSoup//changed.html', 'w') as file:
    file.write(str(doc))

# Buscando varios tags a la vez
tags = doc.find_all(['p', 'div', 'li'])

# Buscando un tag con ciertas especificaciones
specific_tag = doc.find_all(['option'], string = 'Undergraduate', value = 'undergraduate')

# Como en python la palabra class esta reservada para crear clases, se utiliza class_
class_tag = doc.find_all(class_= 'btn-item')

# Buscando tags y atributos con regular expresions
regex_tag = doc.find_all(string = re.compile(r'\$.*'))

for tag in regex_tag:
    print(tag.strip())
    
# limitado la busqueda a una cantida especifica
limited_tags = doc.find_all('option', limit=3)
print(limited_tags)
