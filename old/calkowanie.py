def metoda_prostokatow(f, a, b, k=0):
    """INPUT:
        f - funkcja której całke obliczamy
        a - poczatek przedzialu
        b - koniec przedzialu
        k - krok, czyli jak szerokie są prostokąty

        Output:
        calka - koncowy wynik
        k_steps - kolejne srodki przedzialow
        c_steps - kolejne wartości całek
    """
    k_steps = c_steps = []
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

    return abs(calka), k_steps, c_steps

def func(x):
    return x

# a,b,c=metoda_prostokatow(func, -2, 2, 0.3)
# print(a)