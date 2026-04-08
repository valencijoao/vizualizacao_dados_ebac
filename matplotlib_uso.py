import pandas as pd
import matplotlib.pyplot as plt


pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
df = pd.read_csv('clientes-v3-preparado.csv')

print(df.head(20).to_string())