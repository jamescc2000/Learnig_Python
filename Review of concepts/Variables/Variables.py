########################### VARIABLES ############################
### Definir variable
numero = 10
print(numero)

### Definir variable con camelCase
nombreCompletoDelUsuario = 'James Contreras Campos'  

### Definir variable con snake_case
nombre_comleto_del_usuario = 'James Contreras Campos' #Es la mas recomendada de usar en python

### Redfinir variable
numero = 34
print(numero)

numero += 10  #Es lo mismo que decir numero = numero + 10
print(numero)

numero *= 2  #Es lo mismo que decir numero = numero * 2
print(numero)

### Concatenar con +
nombre = 'James'
bienvenida = 'Hola ' + nombre + ' como estas?'
print(bienvenida)

### Concatenar con f-strings
nombre = 123
bienvenida = f'Hola {nombre} como estas?'  # La diferencia con el anterior es que este convierte la variable en string
print(bienvenida)

### Eliminar variable
del bienvenida

### Operadores de pertenecia (in / not in)
nombre = 'James'
bienvenida = f'Hola {nombre} como estas?'  # La diferencia con el anterior es que este convierte la variable en string
print('ola' in bienvenida)
print('ola' not in bienvenida)
