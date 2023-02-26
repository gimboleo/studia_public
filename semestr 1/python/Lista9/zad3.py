from collections import Counter

import time
start_time = time.time()

def importlisty():
    plik = open(r'C:\Users\kubak\Desktop\Python\Lista8\slowa.txt','r',encoding='utf-8')
    L = plik.read().splitlines()
    return L

def szukanieanagramow(slowo,slownik = importlisty()):
    slowo = slowo.lower()
    slowo = slowo.replace(' ','')
    anagramy = set()
    licznik = Counter(slowo)
    for s in slownik:
        if set(s).issubset(set(slowo)):
            litery = set()
            for k,v in Counter(s).items():              #counter z s w postaci tupli
                if v <= licznik[k]: litery.add(k)
            if litery == set(s): anagramy.add(s)
    #print(anagramy)

    anadict = dict()
    for i in anagramy:
        anadict[i] = Counter(i)

    anagramy = list(anagramy)
    dlugosc = len(slowo)


    for i in range(len(anagramy)-2):
        if len(anagramy[i]) > dlugosc - 2: continue
        temp = licznik.copy()
        temp.subtract(anadict[anagramy[i]])
        for j in range(i,len(anagramy)-1):
            if len(anagramy[i]) + len(anagramy[j]) > dlugosc - 1: continue
            temp1 = temp.copy()
            temp1.subtract(anadict[anagramy[j]])
            if min(temp1.items(), key=lambda x: x[1])[1] < 0: continue
            for k in range(j,len(anagramy)):
                if len(anagramy[i]) + len(anagramy[j]) + len(anagramy[k]) != dlugosc: continue
                temp2 = temp1.copy()
                temp2.subtract(anadict[anagramy[k]])
                if min(temp2.items(), key=lambda x: x[1])[1] == 0 and max(temp2.items(), key=lambda x: x[1])[1] == 0: print(anagramy[i],anagramy[j],anagramy[k])
                
    print("Done")

szukanieanagramow('Jakub Kowalski')
print("--- %s seconds ---" % (time.time() - start_time))
print()

