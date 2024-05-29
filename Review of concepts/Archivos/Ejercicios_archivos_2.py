# Cambiar el tipo de dato de una columna
import pandas as pd
df = pd.read_csv("Archivos\\datos.csv")

# Con esto se convierte a string todos los datos de una columna
df['edad'] = df['edad'].astype(str)
print('----------------------------------------------------')
print(type(df['edad'][0]))

# Reemplzada los apellidos Contreras por Crack
print('----------------------------------------------------')
df['apellido'].replace('Contreras', 'Crack', inplace=True)
print(df)

# Elimina las filas con datos faltantes
df = df.dropna()
print('----------------------------------------------------')
print(df)

# Elimina las filas repetidas
df = df.drop_duplicates()
print('----------------------------------------------------')
print(df)

# Exportando los datos del dataframe a un archivo csv
df.to_csv('Archivos\\datos_limpios.csv')