import pyodbc
import pandas as pd
import matplotlib.pyplot as pt


server = 'MSI'  
database = 'Testing'
connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'

connection = pyodbc.connect(connection_string)

# Obteneniendo los 10 productos mas rentables
query = '''
    SELECT TOP 10 MAX(CONVERT(NVARCHAR,ProductName)) ProductName, SUM(Price*Quantity) AS Revenue FROM OrderDetails od
    JOIN Products p ON p.ProductID = od.ProductID
    GROUP BY od.ProductID
    ORDER BY Revenue DESC
'''

top_product = pd.read_sql_query(query, connection)

top_product.plot(x='ProductName', y='Revenue', kind='bar', figsize=(10,5), legend=False)
pt.title('10 Productos mas rentables')
pt.xlabel('Productos')
pt.ylabel('Revenue')
pt.xticks(rotation=90)
pt.show()


# Obteneniendo los 10 empleados mas efectivos
query2 = '''
    SELECT TOP 10 MAX(CONVERT(NVARCHAR, FirstName) + ' ' + CONVERT(NVARCHAR,LastName)) Empleado, COUNT(*) AS Total FROM Orders o
    JOIN Employees e ON o.EmployeeID = e.EmployeeID
    GROUP BY o.EmployeeID
    ORDER BY Total DESC
'''

top_employees = pd.read_sql_query(query2, connection)

top_employees.plot(x='Empleado', y='Total', kind='bar', figsize=(10,5), legend=False)
pt.title('10 Empleados mas efectivos')
pt.xlabel('Empleados')
pt.ylabel('Total')
pt.xticks(rotation=45)
pt.show()

