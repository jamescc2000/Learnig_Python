################### CONDICIONAL IF #####################
# Como python es un lenguaje identado, poner siempre las tabulaciones
# Estructura :
# if condicion_1 :
#     accion_1
# elif condicion_2 :
#     accion_2
# .
# .
# .
# elif condicion_n :
#     accion_n
# else:
#     accion_por_defecto

edad = 20
dinero = 100

if edad >= 21:
    if dinero < 1500:
        print('No te alcanza')
    else:
          print('Podes pasar')   
elif edad >= 18 & edad < 21:
    if dinero < 500:
        print('No te alcanza')
    else:
          print('Muestrame tu DNI')
else:
    print('No podes pasar')









