import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Graficos//Dispersion.csv")

# Creando la grafica de dispersion
sns.scatterplot(x="tiempo", y="dinero",data=df)

# Mostrando el grafico
plt.show()