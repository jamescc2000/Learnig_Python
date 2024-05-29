from bs4 import BeautifulSoup

# Leemos el archivo html
with open("BeautifulSoup//index.html", "r") as f:
    doc = BeautifulSoup(f, "html.parser")
 
# Buscar directamente un tag (solo devuelve el primero que encuentre)   
title_tags = doc.title

# Cambiar el contenido del tag
title_tags.string = 'Hello'

print(title_tags)

# Buscar todos los tags 
p_tags = doc.find_all('p')[0] # Seleccionamos solo el primero

print(p_tags.find_all('b'))