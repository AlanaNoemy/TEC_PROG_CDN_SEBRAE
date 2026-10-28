import pandas as pd
import numpy as np

df_pub = pd.read_csv('Publicidade.csv', sep = ';', decimal = ',')
print('Observações e variáveis : \n', df_pub.shape)
print('\n Nomes das variáveis : \n', df_pub.columns)
print('\n Tipos das variáveis : \n', df_pub.dtypes)
print('\n As cinco primeiras observações : \n', df_pub.head())