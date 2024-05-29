###################### EJERCICIOS INTERMEDIOS ######################
# Hoy faltó el profesor de clases y los chicos se organizaron para armar la suya propia
# Uno de los alumnos va a ser el profesor y el otro de asistente
# a) Pedir la edad de los compañeros que vinieron hoy a clase y ordenar los datos de menor a mayor

val = True
alumnos = []

while val:
    nombre = input("Introduzca su nombre: ")
    edad = int(input("Introduzaca su edad: "))
    alumnos.append((nombre, edad))
    rpt = input("Vas a agregar otro alumno (Y/N)?: ")
    rpt = rpt.upper()
    if rpt == 'N':
        val = False
     
alumnos.sort(key=lambda x: x[1])

# b) El mayor es el profesor y el menor es el asistente: Quien es quien?

print(f'El profesor es {alumnos[-1][0]}')
print(f'El asistente es {alumnos[0][0]}')






