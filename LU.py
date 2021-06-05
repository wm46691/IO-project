import numpy as np


def Doolittle(A):
    n = len(A)
    L = np.zeros((n, n))
    U = np.zeros((n, n))


    for k in range(n):#dobrze
        L[k][k] = 1
        for j in range(k, n):#dobrze
            suma = 0
            for s in range(k):#dobrze
                suma = suma + L[k][s]*U[s][j]

            U[k][j] = A[k][j] - suma

            for i in range(k+1, n):
                suma = 0
                for s in range(k):
                    suma = suma + L[i][s]*U[s][k]

                L[i][k] = (A[i][k] - suma)/U[k][k]


    return L, U


def Rozwiazanie(L, U, A, b):

    n = len(A)
    Y = np.zeros((n, 1))
    X = np.zeros((n, 1))
    Y = np.dot(np.linalg.inv(L), b)
    X = np.dot(np.linalg.inv(U), Y)

    return X


    