import numpy as np
import LU
import rozniczkowanie
import matplotlib.pyplot as plt
import nieliniowe
import calkowanie
#import simplex
def uklady_liniowe():
    print('Znając macierz współczynników A oraz wektor rozwiązania b. Wyznacz macierze rozkładu L i U stosując metodę Doolittle\'a i oblicz rozwiązanie.')
    
    A = np.random.randint(1, 99, (3,3))
    b = np.random.randint(1, 99, (3, 1))
    print('Macierz A: ')
    for i, v in enumerate(A):
        for j, vv in enumerate(v):
            print(f'{vv}*x{j+1}', end = ' ')
        print('\n')

    print(f'Wektor wyniku b:\n {b}\n')

    L, U = LU.Doolittle(A)
    X, Y = LU.Rozwiazanie(L, U, A, b)
    przelacznik = True
    while przelacznik:
        schowek = input('Naciśnij ''k'', aby zobaczyć kroki lub ''w'', aby zobaczyć wynik.')
        if schowek == 'k':
            print(f'Macierz rozkładu L: \n {L}\n')
            print(f'Macierz rozkładu U: \n {U}\n')
            print(f'Rozwiązanie układu inv(L)*b = z: \n {Y}\n')
        elif schowek == 'w':
            print(X)
            przelacznik = False

    return X

def zadania_rozniczkowanie():
    funkcje = {'sin':np.sin, 'cos':np.cos}
    klucze = [i for i in funkcje.keys()]
    index = np.random.randint(0, len(klucze))

    a = np.random.randint(1, 20)
    b = np.random.randint(a*2, a*20)
    ilosc_punktow = 1000
    print(f'Narysuje pochodna funkcji {klucze[index]}(x) na przedziale od {a} do {b}')
    y = rozniczkowanie.pochodne_punktowe(a, b, ilosc_punktow, funkcje[klucze[index]], 0.25, 2)
    x = np.linspace(a, b, ilosc_punktow)
    
    while True:
        schowek = input('Nacisnij ''k'', aby zobaczyć przykładowe punkty lub w, aby zobaczyć wynik.')
        if schowek == 'k':
            print(y)
        elif schowek == 'w':
            break

    plt.plot(x, y)
    plt.show()
    
def uklady_nieliniowe():
    
    funkcje = {'sin':np.sin, 'cos':np.cos, 'tan':np.tan, }
    klucze = [i for i in funkcje.keys()]
    index = np.random.randint(0, len(klucze))
    print(f'Znajdź rozwiązanie równania nieliniowego {klucze[index]}(x) stosując metode bisekcji.', end = ' ')   
    while True:
        a = np.random.randint(1, 10)
        b = np.random.randint(a*11, a*20)
        f = funkcje[klucze[index]]
        x, steps = nieliniowe.bisekcja(f, a, b)
        if x != None:
            break
    print(f'W przedziale od {a} do {b} z dokladnością 0.0001')
    
    while True:
        schowek = input('Nacisnij ''k'', aby zobaczyć kroki lub w, aby zobaczyć wynik.')
        if schowek == 'k':
            print(steps)
        elif schowek == 'w':
            print(x)
            break


def zadania_calkowanie():
    funkcje = {'sin':np.sin, 'cos':np.cos}
    klucze = [i for i in funkcje.keys()]
    index = np.random.randint(0, len(klucze))
    a = np.random.randint(1, 20)
    b = np.random.randint(a*2, a*20)
    print(klucze)
    print(funkcje[0])
    print(f'Oblicz pole pod wykresem funkcji {klucze[index]}(x) w przedziale od {a} do {b} za pomocą metody prostokątów o szerokości prostokąta {(b-a)/5}')
    wynik, szerokosc, pole_kroki = calkowanie.metoda_prostokatow(funkcje[klucze[index]], a, b)

    while True:
        schowek = input('Naciśnij ''k'', aby zobaczyć kroki lub ''w'', aby zobaczyć wynik.')
        if schowek == 'k':
            print(szerokosc)
            print(pole_kroki)
        elif schowek == 'w':
            print(wynik)
            break



# def zadania_simplex():
#     I = np.eye(3, dtype = np.int32)
#     A = np.random.randint(1, 100, (3, 2))
#     A = np.hstack((A, I))
#     B = np.random.randint(3, 1)
#     return simplex.simplex(A, B)


uklady_nieliniowe()