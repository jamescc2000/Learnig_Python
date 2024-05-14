import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Graficos//Bigotes.csv")

# Creando la grafica de dispersion
sns.boxplot(x="categoria", y="valor",data=df)

# Mostrando el grafico
plt.show()