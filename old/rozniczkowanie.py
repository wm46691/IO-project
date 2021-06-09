from math import *
import numpy as np
import matplotlib.pyplot as plt
def pochodne_punktowe(a, b, ilosc_punktow, x, krok = 0.25, rodzaj = 2):
    wartosci = np.linspace(a, b, ilosc_punktow)
    if rodzaj == 2:
        return (x(wartosci+krok)-x(wartosci))/krok
    elif rodzaj == 3:
        return (x(wartosci+krok) - x(wartosci-krok))/2*krok
    elif rodzaj == 5:
        return (-x(wartosci+2*krok)+8*x(wartosci+krok)-8*x(wartosci-krok)+x(wartosci-2*krok))/12*krok


def pochodne(a, b, ilosc_punktow, x, krok = 0.25, rodzaj = 'wprzod'):
    wartosci = np.linspace(a, b, ilosc_punktow)
    if rodzaj == 'wprzod':
        return (-3*x(wartosci)+4*x(wartosci+krok)-x(wartosci+2*krok))/2*krok
    elif rodzaj == 'centralny':
        return (x(wartosci+krok)-x(wartosci-krok))/2*krok
    elif rodzaj == 'wstecz':
        return (x(wartosci-2*krok)-4*x(wartosci-krok)+3*x(wartosci))/2*krok
    


# a = 0
# b = 6
# ilosc_punktow = 1000000
# x = np.linspace(a, b, ilosc_punktow)
# y = pochodne(a, b, ilosc_punktow, np.cos, 0.25, 'wstecz')
# plt.plot(x, y)
# plt.show()

print(pochodne_punktowe(-4, 2, 100, lambda  x: 2*x**2))