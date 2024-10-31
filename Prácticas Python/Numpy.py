#COMO USAR NUMPY

import numpy as np

# Usando las listas de Python.
M1 = [[1,2,3], [4,5,6], [7,8,9]]
suma = 0
for i in range(0,3): # El intervalo es [0,3)
    for j in range(0,3):
        suma += M1[i][j]

# Usando operaciones de numpy.
M2 = np.array([[1,2,3],[4,5,6],[7,8,9]])
suma = M2.sum()

M = np.array([[1,2,3],[4,5,6],[7,8,9]])
N = np.array([[1,2,3],[4,5,6],[7,8,9]])
# M == N devuelve una matriz del mismo tamaño,
# indicando posición por posición cuales son iguales.
(M == N).all() # Devuelve True si todas las posiciones lo son, False en caso contrario

operadores = {"8": "ARRIBA", "2": "ABAJO", "4": "IZQUIERDA", "6": "DERECHA"}

for op in operadores.values():
    print(op)

