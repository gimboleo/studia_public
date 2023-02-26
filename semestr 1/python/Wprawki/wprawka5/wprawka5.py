import time
start_time = time.time()

def importlisty():
    plik = open(r'C:\Users\kubak\Desktop\Python\Wprawki\wprawka5\popularne_slowa.txt','r',encoding='utf-8')
    L = plik.read().splitlines()
    return L

def wprawka5():
    L = importlisty()
    alfabet = 'abcdefghijklmnoprstuwyz'
    lal = len(alfabet)
    A = dict()
    for slowo in range(len(L)):
        s = set()
        for l in L[slowo]: s.add(l)
        string = ''.join(sorted(s))

        lst = len(string)
        T = [[0]*(lst+1) for i in range (lal+1)]
        najdluzszy = 0
        for i in range(lal):
            for j in range(lst):
                if alfabet[i] == string[j]: 
                    T[i+1][j+1] = T[i][j] + 1
                    if T[i+1][j+1] > najdluzszy:
                        najdluzszy = T[i+1][j+1]
                        wynik = alfabet[i-najdluzszy+1:i+1]
        A[L[slowo]] = (najdluzszy,wynik)
    
    sortowana = sorted(A.items(), key=lambda x: x[1], reverse = True)
    for i in range(10):
        print(sortowana[i][0],' ma PAS = ',sortowana[i][1][0],' (bo zawiera "',sortowana[i][1][1],'")',sep='')

wprawka5()
print("--- %s seconds ---" % (time.time() - start_time))