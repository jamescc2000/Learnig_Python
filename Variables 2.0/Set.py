######################### SET #######################

conjunto_1 = set(['datos1', 'dato2', (19, 'anios')]) # Tener en cuenta que solo puede alamacenar datos no modificables como las tuplas, no puede alamacenar listas
conjunto_2 = set(('datos2', 'dato3', frozenset(conjunto_1))) # No se pude poner un conjunto dentor de otro conjunto, a menos que se utilice frozenset

print(conjunto_1)
print(conjunto_2)


############### TEORIA DE CONJUNTOS #####################33333

conjunto1 = {1,3,5,7,11}
conjunto2 = {1,1,3,3,7}

# Verificando si es un subconjunto utilizando la funcion issubset()
if conjunto2.issubset(conjunto1):
    print(f'El conjunto 2 SI es un subconjunto del conjunto 1')
else:
    print(f'El conjunto 2 NO es un subconjunto del conjunto 1')


# Verificando si es un subconjunto utilziando <=
if conjunto1 <= conjunto2:
    print(f'El conjunto 1 SI es un subconjunto del conjunto 2')
else:
    print(f'El conjunto 1 NO es un subconjunto del conjunto 2')


# Verificando si es un supperconjutno utilizando la funcion issuperset()
if conjunto1.issuperset(conjunto2):
    print(f'El conjunto 1 SI es un superconjunto del conjunto 2')
else:
    print(f'El conjunto 1 NO es un superconjunto del conjunto 2')


# Verificando si es un subconjunto utilziando >
if conjunto2 > conjunto1:
    print(f'El conjunto 2 SI es un superconjunto del conjunto 2')
else:
    print(f'El conjunto 2 NO es un superconjunto del conjunto 2')


#Verificar si todos los elemento son diferente

if conjunto2.isdisjoint(conjunto1):
    print(f' El conjunto 2 es completamente diferente del conjutno 1')
else:
    print(f'El conjunto 2 tiene algunos elementos en comun con el conjunto 1')


