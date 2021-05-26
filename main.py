import LU
import numpy as np
A = [[60, 30, 20],
    [30, 20, 15],
    [20, 15, 12]]

b = [3, -1, 1]


L, U = LU.Doolittle(A)
print(L)
print(U)

n = len(A)
Y = np.zeros((n, 1))
X = np.zeros((n, 1))

