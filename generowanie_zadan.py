import numpy as np
import LU
import rozniczkowanie
import matplotlib.pyplot as plt
import nieliniowe
import calkowanie
import simplex
def uklady_liniowe():
    A = np.random.randint(1, 99, (3,3))
    b = np.random.randint(1, 99, (3, 1))
    print(A)
    print(b)
    L, U = LU.Doolittle(A)
    return LU.Rozwiazanie(L, U, A, b)

def zadania_rozniczkowanie():
    funkcje = {'sin':np.sin, 'cos':np.cos, 'tan':np.tan, 'arcsin':np.arcsin, 'arccos':np.arccos, 'arctan':np.arctan}
    wsp = np.random.randint(1, 100, (1, 2))
    klucze = [i for i in funkcje.keys()]
    index = np.random.randint(0, len(klucze))

    a = np.random.randint(1, 20)
    b = np.random.randint(a*2, a*20)
    ilosc_punktow = 1000
    y = rozniczkowanie.pochodne_punktowe(a, b, ilosc_punktow, funkcje[klucze[index]], 0.25, 2)
    x = np.linspace(a, b, ilosc_punktow)
    plt.plot(x, y)
    plt.show()
    
def uklady_nieliniowe():
    funkcje = {'sin':np.sin, 'cos':np.cos, 'tan':np.tan, 'arcsin':np.arcsin, 'arccos':np.arccos, 'arctan':np.arctan}
    wsp = np.random.randint(1, 100, (1, 2))
    klucze = [i for i in funkcje.keys()]
    index = np.random.randint(0, len(klucze))

    a = np.random.randint(1, 20)
    b = np.random.randint(a*2, a*20)

    return nieliniowe.bisekcja(funkcje[klucze[index]], a, b)


def zadania_calkowanie():
    funkcje = {'sin':np.sin, 'cos':np.cos, 'tan':np.tan, 'arcsin':np.arcsin, 'arccos':np.arccos, 'arctan':np.arctan}
    wsp = np.random.randint(1, 100, (1, 2))
    klucze = [i for i in funkcje.keys()]
    index = np.random.randint(0, len(klucze))

    a = np.random.randint(1, 20)
    b = np.random.randint(a*2, a*20)
    
    return calkowanie.metoda_prostokatow(funkcje[klucze[index]], a, b)



def zadania_simplex():
    I = np.eye(3, dtype = np.int32)
    A = np.random.randint(1, 100, (3, 2))
    A = np.hstack((A, I))
    B = np.random.randint(3, 1)
    return simplex.simplex(A, B)

