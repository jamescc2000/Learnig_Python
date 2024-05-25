############################## User Difiened Functions ##########################################
import pyodbc
import pandas as pd

square = lambda n: n*n
print(square(10))


# Definir la cadena de conexión
server = 'MSI'  
database = 'Testing'

# Crear la cadena de conexión
connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'

try:
    # Conectarse a la base de datos
    connection = pyodbc.connect(connection_string)
    print("Conexión exitosa a SQL Server")

    # Crear un cursor desde la conexión
    cursor = connection.cursor()
    
    # Ejecutar una consulta
    cursor.execute("SELECT TOP 5 CCL, CCR, NID, NCL FROM BDC01")
    results = cursor.fetchall()
    df_results = pd.DataFrame(results)
    print(df_results)
    #connection.commit()
    
    cursor.close()

except pyodbc.Error as e:
    print("Error al conectarse a SQL Server:", e)

finally:
    # Cerrar la conexión
    if 'connection' in locals():
        connection.close()
        
