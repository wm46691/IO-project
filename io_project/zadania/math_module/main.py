import numpy as np
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import matplotlib.patches as ptc
import os
import imageio
from django.conf import settings as django_settings


class Zadanie():
    #def __init__(self):
     #   self.Generate()
    def Generate():
        pass
    def Visualize():
        pass
    def Calculate():
        pass
    def Compare(self, odp):
        if odp == self.wynik:
            return True
        else:
            return False
    def GetResult(self):
        return self.wynik

class Calkowanie(Zadanie):
    def Generate(self):
        """Generuje:
        f - funkcja której całke obliczamy
        a - poczatek przedzialu
        b - koniec przedzialu
        k - krok, czyli jak szerokie są prostokąty"""

        funkcje = {'f(x)=3x':(lambda x : 3*x), 'f(x)=2*x^2-4':((lambda x : 2*x**2-4)), 'f(x)=2*x^2+2x-1':((lambda x : 2*x**2+2*x-1))}
        klucze = [i for i in funkcje.keys()]
        index = np.random.randint(0, len(klucze))
        a = np.random.randint(-5, -1)
        b = np.random.randint(1, 5)

        self.n = 5

        self.f = funkcje[klucze[index]]
        self.f_str = klucze[index]
        self.k = (b-a)/self.n
        self.a = a
        self.b = b

    def Calculate(self):
        """Pobiera z obiektu:
        f - funkcja której całke obliczamy
        a - poczatek przedzialu
        b - koniec przedzialu
        k - krok, czyli jak szerokie są prostokąty

        Oblicza:
        calka - koncowy wynik
        k_steps - kolejne srodki przedzialow
        c_steps - kolejne wartości całek
        """
        k_steps = c_steps = []
        k = self.k
        b = self.b
        a = self.a
        f = self.f

        #ustawienie k jesli nie zostalo ustalone
        if k==0:
            k = (b - a)/5
        
        cur = a #obecny punkt z ktorego zaczyna sie prostokat
        calka = 0

        while(cur + k <= b):
            #obliczenie wysokosci w polowie prostokata
            srodek = cur+k/2
            wysokosc = f(srodek)
            k_steps.append(srodek)
            #obliczenie pola pod wykresem
            c = wysokosc*k
            calka += c
            c_steps.append(c)
            #przesuniecie do początku następnego prostokąta
            cur += k
            #print("calka: {} cur:{}", calka, cur)

        #ostatni (potencjalnie mniejszy prostokąt)
        szerokosc = b - cur
        #print("sz: {}".format(szerokosc))
        srodek = cur+szerokosc/2
        k_steps.append(srodek)
        wysokosc = f(srodek)
        c = wysokosc*szerokosc
        calka += c
        c_steps.append(c)

        self.wynik = calka
        self.k_steps = k_steps
        self.c_steps = c_steps

    def Polecenie(self):
        return self.f_str, self.a, self.b, self.k
    
    def Visualize(self):
        x = np.linspace(self.a,self.b,100)
        filenames = []
        start_x = self.a
        fig, ax = plt.subplots()
        for i in range(self.n):
            
            plt.plot(x, self.f(x), c='blue')
            rect = ptc.Rectangle((start_x, 0), self.k, self.f(start_x+1/2*self.k), alpha = 0.5)
            start_x +=  self.k
            ax.add_patch(rect)
            #plt.show()

            # create file name and append it to a list
            filename = f'{i}.png'
            filenames.append(filename)
            
            # save frame
            plt.savefig(filename)
            #plt.close()
        plt.close()
        with imageio.get_writer(os.path.join(django_settings.STATIC_ROOT, 'images','my-gif.gif'), mode='I', fps=1) as writer:
            for filename in filenames:
                image = imageio.imread(filename)
                writer.append_data(image)
        plt.close()
        # Remove files
        for filename in set(filenames):
            os.remove(filename)

class Bisekcja(Zadanie):
    def Generate(self):
        funkcje = {'f(x)=3x':(lambda x : 3*x), 'f(x)=2*x^2-4':((lambda x : 2*x**2-4)), 'f(x)=x+0.3':((lambda x : x+0.3))}
        klucze = [i for i in funkcje.keys()]
        index = np.random.randint(0, len(klucze))
        #print(f'Znajdź rozwiązanie równania nieliniowego {klucze[index]}(x) stosując metode bisekcji.', end = ' ')   
        while True:
            a = np.random.randint(-5, -1)
            b = np.random.randint(1, 5)
            f = funkcje[klucze[index]]
            f_str = klucze[index]

            self.a = a
            self.b = b
            self.f = f
            self.f_str = f_str
            if self.__Check():
                break

    def __Check(self):
        #Sprawdzenie czy przedział zawiera pierwiastek
        if (self.f(self.a)*self.f(self.b)>=0):
            x = None
            n = -1
            return False
        else:
            return True

    def Calculate(self):
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
        b_steps = []
        a_steps = []
        
        a = self.a
        b = self.b
        f = self.f
        tol = 0.001
        ftol = 0.001
        #wyznaczenie srodka przedezialu
        x = (a+b)/2
        last_x = x - 1 #ustawiam tak bo jakies musi byc,
        #a w ten sposob na pewno nie spelni warunku dokladnosci
        while True:
            x_steps.append(x)
            a_steps.append(a)
            b_steps.append(b)
            #n += 1
        
            #ustawienie nopwych granic przedzialu
            if(f(a)*f(x) < 0):
                b = x
            else:
                a = x
            #wyznaczenie nowego srodka i zapisanie poprzedniego
            last_x = x
            x = (a+b)/2

            #sprawdzenie dokladnosci
            if((abs(f(x)) <= ftol) or abs(x-last_x) <= tol):
                x_steps.append(x)
                a_steps.append(a)
                b_steps.append(b)
                break
        

        self.wynik = x
        self.x_steps = x_steps
        self.a_steps = a_steps
        self.b_steps = b_steps

    def Polecenie(self):
        return  self.f_str, self.a, self.b

    def Visualize(self):
        #print(len(self.x_steps))
        #print(self.a_steps)
        #print(self.b_steps)
        x = np.linspace(self.a,self.b,30)
        filenames = []
        for i in range(len(self.x_steps)):
            plt.plot(x, self.f(x))
            plt.axvline(self.a_steps[i], c='r', linewidth = 0.5)
            plt.axvline(self.b_steps[i], c='r', linewidth = 0.5)
            plt.scatter(self.x_steps[i], 0, c='orange', zorder=10)
            #plt.show()

            # create file name and append it to a list
            filename = f'{i}.png'
            filenames.append(filename)
            
            # save frame
            plt.savefig(filename)
            plt.close()
        
        with imageio.get_writer(os.path.join(django_settings.STATIC_ROOT, 'images', 'my-gif.gif'), mode='I', fps=1) as writer:
            for filename in filenames:
                image = imageio.imread(filename)
                writer.append_data(image)
        # Remove files
        for filename in set(filenames):
            os.remove(filename)

class LU(Zadanie):
    def Generate(self):
        self.A = np.random.randint(1, 99, (3,3))
        self.b = np.random.randint(1, 99, (3, 1))

    def Calculate(self):
        n = len(self.A)
        L = np.zeros((n, n))
        U = np.zeros((n, n))


        for k in range(n):
            L[k][k] = 1
            for j in range(k, n):
                suma = 0
                for s in range(k):
                    suma = suma + L[k][s]*U[s][j]

                U[k][j] = self.A[k][j] - suma

                for i in range(k+1, n):
                    suma = 0
                    for s in range(k):
                        suma = suma + L[i][s]*U[s][k]

                    L[i][k] = (self.A[i][k] - suma)/U[k][k]
        self.L = L
        self.U = U

        self.Rozwiazanie()

    def Rozwiazanie(self):

        L = self.L
        U = self.U
        A = self.A
        b = self.b
        n = len(A)
        Y = np.zeros((n, 1))
        X = np.zeros((n, 1))
        Y = np.dot(np.linalg.inv(L), b)
        X = np.dot(np.linalg.inv(U), Y)

        self.X = X
        self.Y = Y

    def Polecenie(self):
        a_str = ""
        A = self.A
        for i, v in enumerate(A):
            for j, vv in enumerate(v):
                a_str += f'{vv}*x{j+1}' + ' '
            a_str += '\n'

        b = self.b
        b_str = ""
        for i, v in enumerate(b):
            b_str += str(b[i][0]) + " "

        x = self.X
        x_str = ""
        for i, v in enumerate(x):
            x_str += str(x[i][0]) + " "

        y = self.Y
        y_str = ""
        for i, v in enumerate(y):
            y_str += str(y[i][0]) + " "

        l_str = ""
        L = self.L
        for i, v in enumerate(L):
            for j, vv in enumerate(v):
                l_str += f'{vv}*x{j+1}' + ' '
            l_str += '\n'

        u_str = ""
        U = self.U
        for i, v in enumerate(U):
            for j, vv in enumerate(v):
                u_str += f'{vv}*x{j+1}' + ' '
            u_str += '\n'

        return a_str, b_str, x_str, y_str, l_str, u_str

class Rozniczki(Zadanie):
    def Generate(self):
        funkcje = {'f(x)=sin(x)':np.sin, 'f(x)=cos(x)':np.cos, 'f(x)=3x':(lambda x : 3*x)}
        klucze = [i for i in funkcje.keys()]
        index = np.random.randint(0, len(klucze))
        self.f = funkcje[klucze[index]]
        self.f_str = klucze[index]
        self.a = np.random.randint(-5, -1)
        self.b = np.random.randint(0, 6)
        self.rodzaj = int(np.random.choice([2,3,5], 1)[0])
        self.krok = float(np.random.choice([1, 0.5, 0.25], 1)[0])

    def Calculate(self):
        a = self.a 
        b = self.b
        ilosc_punktow = 1000
        rodzaj = self.rodzaj
        krok = self.krok
        f = self.f
        wartosci = np.linspace(a, b, ilosc_punktow)
        if rodzaj == 2:
            self.y = (f(wartosci+krok)-f(wartosci))/krok
        elif rodzaj == 3:
            self.y =(f(wartosci+krok) - f(wartosci-krok))/2*krok
        elif rodzaj == 5:
            self.y = (-f(wartosci+2*krok)+8*f(wartosci+krok)-8*f(wartosci-krok)+f(wartosci-2*krok))/12*krok
        self.x = wartosci

    def Polecenie(self):
        return self.f_str, self.a, self.b, self.krok, self.rodzaj
    
    def Visualize(self):
        plt.plot(self.x, self.y)
        plt.savefig(os.path.join(django_settings.STATIC_ROOT, 'images','my-gif.png'))
        plt.close()