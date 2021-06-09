import numpy as np
import LU
import rozniczkowanie
import matplotlib.pyplot as plt
import nieliniowe
import calkowanie
from os import system
#import simplex

def uklady_liniowe():
    A = np.random.randint(1, 99, (3,3))
    b = np.random.randint(1, 99, (3, 1))
    
    L, U = LU.Doolittle(A)
    X, Y = LU.Rozwiazanie(L, U, A, b)
    while True:
        print('Znając macierz współczynników A oraz wektor rozwiązania b. Wyznacz macierze rozkładu L i U stosując metodę Doolittle\'a i oblicz rozwiązanie.')

        print('Macierz A: ')
        for i, v in enumerate(A):
            for j, vv in enumerate(v):
                print(f'{vv}*x{j+1}', end = ' ')
            print('\n')

        print(f'Wektor wyniku b:\n {b}\n')

        input('Naciśnij ENTER, aby kontynuować.')

        while True:
            schowek = input('Naciśnij k, aby zobaczyć kroki lub d, aby przejść do etapu sprawdzenia wyniku.')
            if schowek == 'k' or schowek == 'd':
                pass
            else:
                print('Zły klawisz! Wybierz przycisk k lub d.')
                input('Naciśnij ENTER, aby kontynuować')

        
            if schowek == 'k':
                print(f'Macierz rozkładu L: \n {L}\n')
                print(f'Macierz rozkładu U: \n {U}\n')
                print(f'Rozwiązanie układu inv(L)*b = z: \n {Y}\n')
            elif schowek == 'd':
                print('Wpisz swój wynik')
                wynik = np.zeros((3, 1))
                for i in range(3):
                    wynik[i] = input()

                if np.all(wynik == X):
                    print('Prawidłowy wynik!')
                    return 0

                else:
                    print('Podałeś zły wynik. Oblicz jeszcze raz')
                    input('Naciśnij ENTER, aby kontynuować.')
                    break


def zadania_rozniczkowanie():
    funkcje = {'sin':np.sin, 'cos':np.cos}
    klucze = [i for i in funkcje.keys()]
    index = np.random.randint(0, len(klucze))

    a = np.random.randint(1, 20)
    b = np.random.randint(a*2, a*20)
    ilosc_punktow = 1000

    y = rozniczkowanie.pochodne_punktowe(a, b, ilosc_punktow, funkcje[klucze[index]], 0.25, 2)
    x = np.linspace(a, b, ilosc_punktow)
    while True:
        print(f'Narysuje pochodna funkcji {klucze[index]}(x) na przedziale od {a} do {b}')
        while True:
            schowek = input('Nacisnij k, aby zobaczyć przykładowe punkty lub d, aby wyświetlić wynik.')
            if schowek != 'k' and schowek != 'd':
                print('Zły klawisz! Wybierz przycisk k lub d.')
                input('Naciśnij ENTER, aby kontynuować')
            elif schowek == 'k':
                print(y)
            elif schowek == 'd':
                plt.plot(x, y)
                plt.show()
                return 0

   
def uklady_nieliniowe():
    funkcje = {'sin':np.sin, 'cos':np.cos, 'tan':np.tan, }
    klucze = [i for i in funkcje.keys()]
    index = np.random.randint(0, len(klucze))
    while True:
        a = np.random.randint(1, 10)
        b = np.random.randint(a*11, a*20)
        f = funkcje[klucze[index]]
        x, steps = nieliniowe.bisekcja(f, a, b)
        if x != None:
            break
    while True:
        print(f'Znajdź rozwiązanie równania nieliniowego {klucze[index]}(x) stosując metode bisekcji.', end = ' ') 
        print(f'W przedziale od {a} do {b} z dokladnością 0.0001')
    
        while True:
            schowek = input('Nacisnij k, aby zobaczyć kroki lub d, aby sprawdzić wynik.')
            if schowek != 'k' and schowek != 'd':
                print('Zły klawisz! Wybierz przycisk k lub d.')
                input('Naciśnij ENTER, aby kontynuować')
            elif schowek == 'k':
                print(steps)
            elif schowek == 'd':
                print(x)
                wynik = float(input('Podaj uzyskany wynik'))
                if wynik == steps[-1]:
                    print('Prawidłowy wynik!')
                    return 0
                else:
                    print('Zły wynik! Spróbuj jeszcze raz.')
                    input('Naciśnij ENTER, aby kontynuować')
                    break



def zadania_calkowanie():
    funkcje = {'sin':np.sin, 'cos':np.cos}
    klucze = [i for i in funkcje.keys()]
    index = np.random.randint(0, len(klucze))
    a = np.random.randint(1, 20)
    b = np.random.randint(a*2, a*20)
    wynik, szerokosc, pole_kroki = calkowanie.metoda_prostokatow(funkcje[klucze[index]], a, b)



    while True:
        print(f'Oblicz pole pod wykresem funkcji {klucze[index]}(x) w przedziale od {a} do {b} za pomocą metody prostokątów o szerokości prostokąta {(b-a)/5}')
    

        while True:
            schowek = input('Naciśnij k, aby zobaczyć kroki lub d, aby sprawdzić wynik.')
            if schowek != 'k' and schowek != 'd':
                print('Zły klawisz! Wybierz przycisk k lub d.')
                input('Naciśnij ENTER, aby kontynuować')
            elif schowek == 'k':
                print('Pola poszczególnych prostokątów.')
                print(np.abs(pole_kroki))
            elif schowek == 'd':
                print(wynik)
                wynik_użytkownika = float(input('Podaj wynik: '))
                if wynik_użytkownika == wynik:
                    print('Prawidłowy wynik!')
                    return 0
                else:
                    print('Zły wynik! Spróbuj jeszcze raz.')
                    input('Naciśnij ENTER, aby kontynuować')
                    break


# def zadania_simplex():
#     I = np.eye(3, dtype = np.int32)
#     A = np.random.randint(1, 100, (3, 2))
#     A = np.hstack((A, I))
#     B = np.random.randint(3, 1)
#     return simplex.simplex(A, B)




uklady_liniowe()