######################################## Expresiones regulares #########################################3
import re

texto = '''Hola maestro, esto es la cadena 1. como estas mi capitan?
Esta es la linea2linea22 de texto.
Y Esta es la final (linea333); definitiva mi capitan'''


# Haciendo una busqueda simple
resultado = re.findall('esta', texto)

#\d --> busca digitos numericos del 0 al 9
resultado = re.findall(r'\d', texto)

#\D --> busca todo menos digitos numericos del 0 al 9
resultado = re.findall(r'\D', texto)

#\w --> busca caracteres alfanumericos ([a-z], [A-Z], 0-9, _)
resultado = re.findall(r'\w', texto)

#\W --> busca todo menos caracteres alfanumericos ([a-z], [A-Z], 0-9, _)
resultado = re.findall(r'\W', texto)

#\s --> busca espacio en blanco (tabs, espacios, saltos de liena)
resultado = re.findall(r'\s', texto)

#\S --> busca todo menos espacio en blanco (tabs, espacios, saltos de liena)
resultado = re.findall(r'\S', texto)

#. --> busca todo menos saltos de linea
resultado = re.findall(r'.', texto)

#\n --> busca saltos de linea
resultado = re.findall(r'\n', texto)

#\ --> cancelamos caracteres especiales
resultado = re.findall(r'\.', texto) # para buscar un punto colocamos \ al inicio

# Armando una cadena que busque un numero, seguido de un punto y un espacio
resultado = re.findall(r'\d\.\s', texto)

# ^ --> busca el principio de una linea
resultado = re.findall(r'^Esta', texto, flags=re.M) # re.M activa la multilinea

# $ --> busca el final de una linea
resultado = re.findall(r'capitan$', texto, flags=re.M) # re.M activa la multilinea

# {n} --> busca n cantidad de veces el valor (caracter) de la izquierda
resultado = re.findall(r'\d{3}\s', texto) 

# {n, m} --> busca al menos n y como maximo m
resultado = re.findall(r'\d{1,3}', texto) 

# (string){n, m} --> 
resultado = re.findall(r'(linea\d){2,3}', texto) 

# | --> busca una cosa o la otra
resultado = re.findall(r'\d{1,3}|Hola', texto) 


#print(resultado)


# Ejemplo 1
text = 'The quick borwn fox jumps over the lazy dog'
x = re.search('^The.*dog$',text)

if x:
    print('Si')
else:
    print('No')


# Ejemplo 2
text = 'La fecha es 23/06/2022 y el telefono es +1 555-555-555'

pattern = r'\d{2}/\d{2}/\d{4}'
replacement = 'Fecha oculta'

new_text = re.sub(pattern, replacement, text)
print(f'Texto modificado: {new_text}')


# Ejemplo 3
text = 'reemplazando todas las vocales por asteriscos'
new_text = re.sub(r'[aeiou]', '*', text)
print(new_text)

# Ejemplo 4
email = 'example@example.com'
pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
result = re.match(pattern, email)

if result:
    print('Direccion de correo valida')
else:
    print('Direccion de correo invalida')
    
    
# Ejemplo 5
text = 'Esto es un ejemplo de una pagina we: http://www.example.com y tambien podemos visitarla'
pattern = r'http?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
result = re.findall(pattern, text)
print(result)



### Ejercicio
# detectando un numero CABA y ocultandolo
texto = 'Hola James, mi numero es: +54 555-555-555 o tambien: +51 999-999-999'

pattern = r'\+\d{1,3}\s\d{3}-\d{3}-\d{3}'

reemplazo = re.sub(pattern,'(Numero oculto)',texto)

print(reemplazo)