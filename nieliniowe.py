import math
import numpy

#Metoda bisekcji
def bisekcja(f, a, b, tol = 0.00001, ftol=0.0001):
    """Input:
        f - funkcja której szukamy miejsca zerowego
        a - punkt początkow zakresu
        b - punkt końcowy zakresu
        tol - dokładność dla x
        ftol - dokładność dla f(x)
        
        Output:
        x - koncowy wynik
        x_steps[] - kolejne znalezione x
        """
    n = 0
    x_steps = []
    #Sprawdzenie czy przedział zawiera pierwiastek
    if (f(a)*f(b)>=0):
        x = None
        n = -1
        return x, x_steps
    
    #wyznaczenie srodka przedezialu
    x = (a+b)/2
    last_x = x - 1 #ustawiam tak bo jakies musi byc,
    #a w ten sposob na pewno nie spelni warunku dokladnosci
    while True:
        n += 1
        #sprawdzenie dokladnosci
        if((abs(f(x)) <= ftol) or abs(x-last_x) <= tol):
            return x, x_steps
        #ustawienie nopwych granic przedzialu
        if(f(a)*f(x) < 0):
            b = x
        else:
            a = x
        #wyznaczenie nowego srodka i zapisanie poprzedniego
        last_x = x
        x = (a+b)/2
    