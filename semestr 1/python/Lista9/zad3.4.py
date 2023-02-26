from collections import Counter
from collections import defaultdict as dd
from itertools import product

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

    anadl = dd(list)
    for i in anagramy:
        anadl[len(i)].append(i)

    dlugosc = len(slowo)

    T = set()
    for i in range(dlugosc-2,0,-1):
        for j in range(i,0,-1):
            if i+j >= dlugosc: continue
            for k in range(j,0,-1):
                if i+j+k == dlugosc: T.add((i,j,k))

    cos = 0

    for i in T:
        if i[0] == i[1]:
            for a in range(len(anadl[i[0]])-1):
                temp = licznik.copy()
                temp.subtract(Counter(anadl[i[0]][a]))
                for b in range(a+1,len(anadl[i[0]])):
                    temp1 = temp.copy()
                    temp1.subtract(Counter(anadl[i[0]][b]))
                    if min(temp1.items(), key=lambda x: x[1])[1] < 0: continue
                    for c in anadl[i[2]]:
                        temp2 = temp1.copy()
                        temp2.subtract(Counter(c))


        elif i[1] == i[2]:
            for b in range(len(anadl[i[1]])-1):
                temp = licznik.copy()
                temp.subtract(Counter(anadl[i[1]][b]))
                for c in range(b+1,len(anadl[i[1]])):
                    temp1 = temp.copy()
                    temp1.subtract(Counter(anadl[i[1]][c]))
                    if min(temp1.items(), key=lambda x: x[1])[1] < 0: continue
                    for a in anadl[i[0]]:
                        temp2 = temp1.copy()
                        temp2.subtract(Counter(a))

        elif i[0] == i[2]:
            for a in range(len(anadl[i[0]])-1):
                temp = licznik.copy()
                temp.subtract(Counter(anadl[i[0]][a]))
                for c in range(a+1,len(anadl[i[0]])):
                    temp1 = temp.copy()
                    temp1.subtract(Counter(anadl[i[0]][c]))
                    if min(temp1.items(), key=lambda x: x[1])[1] < 0: continue
                    for b in anadl[i[1]]:
                        temp2 = temp1.copy()
                        temp2.subtract(Counter(b))


        elif i[0] == i[1] == i[2]:
            for a in range(len(anadl[i[0]])-2):
                temp = licznik.copy()
                temp.subtract(Counter(anadl[i[0]][a]))
                for b in range(a+1,len(anadl[i[0]])-1):
                    temp1 = temp.copy()
                    temp1.subtract(Counter(anadl[i[0]][b]))
                    if min(temp1.items(), key=lambda x: x[1])[1] < 0: continue
                    for c in range(b+1,len(anadl[i[0]])):
                        temp2 = temp1.copy()
                        temp2.subtract(Counter(anadl[i[0]][c]))

        else:
            for a in anadl[i[0]]:
                temp = licznik.copy()
                temp.subtract(Counter(a))
                for b in anadl[i[1]]:
                    temp1 = temp.copy()
                    temp1.subtract(Counter(b))
                    if min(temp1.items(), key=lambda x: x[1])[1] < 0: continue
                    for c in anadl[i[2]]:
                        temp2 = temp1.copy()
                        temp2.subtract(Counter(c))

    print(cos)
    print("Done")

szukanieanagramow('Olga Tiekało')
print("--- %s seconds ---" % (time.time() - start_time))
print()

