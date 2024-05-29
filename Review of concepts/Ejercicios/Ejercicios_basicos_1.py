###################### EJERCICIOS BASICOS 1 ######################3
# El timming para ver los conceptos basicos de un cruso basico de payton es de (en horas):
min = 2.5 
max = 7.0
prom = 4.0
este_curso = 1.5

# a) Cuanta diferencia en porcentaje hay entre el curso actual y:
#   - El mas rapido de los otros cursos
#   - El mas lento de los otros cursos
#   - El promedio de los cursos

respuesta1 = ((min - este_curso)/min)*100
print('La diferencia entre el mas rapido de los otros cursos y este es : ' + str(respuesta1) + '%')

respuesta2 = ((max - este_curso)/max)*100
print('La diferencia entre el mas lento de los otros cursos y este es : ' + str(respuesta2) + '%')

respuesta3 = ((prom - este_curso)/prom)*100
print('La diferencia entre el promedio de los cursos y este es : ' + str(respuesta3) + '%')


# b) Teniendo en cuenta que la cantidad en crudo, en promedio, de los otros curos es de:
crudo_otros = 5.0 # Y con edicion con convierten en 4 horas

# Y el crudo de este cruso fue de:
crudo_este_curso = 3.5 # Y con edicion se redujo a 1.5 horas

# Cual es el porcentaje de material inservible que se reduce en:
#   - El promedio de los cursos
#   - El curso actual (este_curso)

respuesta4 = ((crudo_otros - prom)/crudo_otros)*100
print('El porcentaje de material inservible que se reduce en el promedio de los cursos es: ' + str(respuesta4) + '%')

respuesta5 = ((crudo_este_curso - este_curso)/crudo_este_curso)*100
print('El porcentaje de material inservible que se reduce en el curso actual es: ' + str(respuesta5) + '%')


# c) Ver 10 horas de este curso a cuantas de otros cursos equivale? y al reves?

hora_este_curso = (prom / este_curso)

print('Ver 10 horas de este curso equivale a: ' + str(10*hora_este_curso) + ' horas de otros cursos')

hora_otros_cursos = (este_curso / prom)

print('Ver 10 horas de otros curso equivale a: ' + str(10*hora_otros_cursos) + ' horas de este curso')



















