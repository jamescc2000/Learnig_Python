import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Graficos//Ingresos_mensuales.csv")

# Creando la grafica de barras
sns.barplot(x="fuente", y="ingresos",data=df)

# Mostrando el totla de ingresos
total_ingresos = df['ingresos'].sum()
print(f'El total de ingresos es de: ${total_ingresos} USD')

# Mostrando el grafico
plt.show()