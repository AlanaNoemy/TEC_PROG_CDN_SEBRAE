
import pandas as pd

df_pub = pd.read_csv('Publicidade.csv', sep = ';', decimal = ',')
print('Observações e variáveis : \n', df_pub.shape)
print('\n Nomes das variáveis : \n', df_pub.columns)
print('\n Tipos das variáveis : \n', df_pub.dtypes)
print('\n As cinco primeiras observações : \n', df_pub.head())

import numpy as np
from scipy import linalg

x = df_pub['TV']
y = df_pub['vendas']
soma_x2 = sum(x**2)
soma_x = sum(x)
n = len(x)
soma_xy = sum(x*y)
soma_y = sum(y)

A = np.array([[soma_x2,soma_x],[soma_x, n]])
B = np.array([[soma_xy],[soma_y]])

Xsol = linalg.solve(A,B)

a = Xsol[0][0]
b = Xsol[1][0]
x= 250
print('y = %.2fx + %.2f'% (a,b))
print(f' y = {a:.2f}*{x} + {b:.2f}')
print(f' y = {a*x + b:.2f}')
print(f' \nComo a reta A governa calculamos apenas o A para fazer a media')
print(f' y = {a:.2f}*{x:.2f}')
print(f' y = {a*x:.2f}')
import seaborn as sn
from matplotlib import pyplot as plt

sn.scatterplot( x = 'TV', y = 'vendas', data = df_pub, color = 'darkblue')
plt.title('Diagrama de dispersão')
plt.xlabel('TV (milhares de dólares)')
plt.ylabel('vendas (milhares de unidades)')
plt.show()

import seaborn as sn
from matplotlib import pyplot as plt

sn.regplot(x = df_pub['radio'], y = df_pub['vendas'], color = '#960018', 
           ci = None, marker = '*')
plt.title('Diagrama de dispersão e Reta de regressão')
plt.xlabel('Radio (milhares de dólares)')
plt.ylabel('vendas (milhares de unidades)')
plt.show()

import seaborn as sn
from matplotlib import pyplot as plt

# Cria o gráfico de dispersão e a reta de regressão
ax = sn.regplot(
    x=df_pub['radio'],
    y=df_pub['vendas'],
    color='#960018',
    ci=None,
    marker='o',
    scatter=False  # não desenha as bolinhas padrão
)

# Coloca corações no lugar das bolinhas
plt.scatter(
    df_pub['radio'],
    df_pub['vendas'],
    color='#960018',
    marker='$♥$',
    s=180
)

plt.title('Diagrama de dispersão e Reta de regressão')
plt.xlabel('Radio (milhares de dólares)')
plt.ylabel('vendas (milhares de unidades)')

plt.show()
