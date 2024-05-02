######################### TUPLAS #######################
# La tupla generalmente se utiliza para datos que solo se van a leer (datos fijos) porque almacena el dato en memoria y es mucho mas optimo
# Convirtiendo a tuplas con tuple()
tupla_1 = tuple(["dato1", "dato2"])
tupla_2 = tuple({"dato2", "dato3"})

print(tupla_1)
print(tupla_2)

# Creando tuplas a partir de datos
tupla_1 = "dato1", # Si no pusieramos la coma seria un string
tupla_2 = "dato2", "dato3"

print(tupla_1)
print(tupla_2)