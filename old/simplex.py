import numpy as np
def simplex(A,B):
    """ INPUT:
    A - współczynniki ograniczen
    B - wspolczynniki z funkcji celu
    """
    #Cj - dorobic
    #Cb-dorobic
    n = 0 #licznik iteracji
    while(any(ww)>0):
        n+=1
        #znajdz kolumne kluczową (indeks maksymalnego el. w ierszu wskaznikow)
        kk = ww.index(max(ww))
        ki = B/A[:,kk] #ki-kolumna ilorazow

        #znalezienie WK(indeks najmniejszego nieujemnego ilorazu)
        wk_val = min(ki)
        wk = ki.index(wk)
        while wk_val < 0:
            ki[wk] = None
            wk_val = min(ki)
            wk = ki.index(wk)

        ab(wk) = kk
        cb(wk) = Cj[kk]

        #wyznaaczenie ER = A(WK,KK) - ER element rozwiazujacy
        ER = A[wk,kk]
        #podzielenie wiersza kluczowego przez ER
        A[wk, :] = A[wk, :] / ER
        B(wk) = B(wk)/ER

        #wyeliminowanie elementow w KK nad i pod WK
        for i in range(3):
            if  i == wk:
                continue
            #mnoznik = ;
            B[i] = B[i] - A[:,kk]*B[wk]
            A[i, :] = A[i,:] - A[i,kk]*A[wk,:]
        #wyznaczenie wiersza wskaznikow
        F=np.transpose(Cb)*B
        ww = Cj-np.transpose(Cb)*A

