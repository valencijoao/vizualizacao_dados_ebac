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

# Pairplot - Densidade e Histograma
sns.pairplot(df[['idade','salario','anos_experiencia','nivel_educacao']])
plt.show()

# Regressão 
sns.regplot(x='idade', y='salario', data=df, color='#278f65', scatter_kws={'alpha':0.5, 'color':'#34c289'})
plt.title('Regressão de Salário por Idade')
plt.xlabel('Idade')
plt.ylabel('Salário')
plt.show()

# Countplot com hue
sns.countplot(x='estado_civil', hue='nivel_educacao', data=df, palette='pastel')
plt.xlabel('Estado Civil')
plt.ylabel('Quantidade de Clientes')
plt.legend(title='Nível de Educação')
plt.show()

