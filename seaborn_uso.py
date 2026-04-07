import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('clientes-v3-preparado.csv')

# Dispersão
sns.jointplot(x='idade', y='salario', data=df, kind='scatter') 
plt.show()

# Densidade
plt.figure(figsize=(10,6))
sns.kdeplot(df['salario'], fill=True, color='#863e9c')
plt.title('Densidade de Salários')
plt.xlabel('Salário')
plt.show()

# Gráfico Pairplot - Densidade e Histograma
sns.pairplot(df[['idade','salario','anos_experiencia','nivel_educacao']])
plt.show()

