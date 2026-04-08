import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('clientes-v3-preparado.csv')

df_corr = df[['salario','idade','anos_experiencia','numero_filhos','nivel_educacao_cod','area_atuacao_cod','estado_cod']].corr()
# Heatmap de correlação
plt.figure(figsize=(10,8))
sns.heatmap(df_corr, annot=True, fmt=".2f")
plt.title('Mapa de Calor da Correlação entre Variáveis')
plt.show()