import pandas as pd
import matplotlib.pyplot as plt
# Tuve problemas para instalar seaborn, el siguiente codigo fue la solucion:
#import pip
#pip.main(['install','seaborn'])
import seaborn as sns

df = pd.read_csv("Graficos//P2.csv")

# Creando la grafica lineal
sns.lineplot(x="fecha", y="p2",data=df)

# Marcando un punto dentro de la grafica
plt.plot('01-08',9, 'o')

# Mostrando el grafico
plt.show()