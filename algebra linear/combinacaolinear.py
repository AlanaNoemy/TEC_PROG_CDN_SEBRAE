import numpy as np
from scipy import linalg

A = np.array([[1, -3],
              [2,  1]])

b = np.array([[7],[7]])
det_A = np.linalg.det(A)
resultado = np.linalg.solve(A, b)
print(f'determinante de A: {det_A:.2f}')
print(f'resultado: c1 = {resultado[0][0]:.2f}, c2 = {resultado[1,0]:.2f}')