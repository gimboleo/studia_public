from collections import Counter
from collections import defaultdict as dd
from functools import reduce

import time
start_time = time.time()

def importlisty():
    plik = open(r'slowa.txt','r',encoding='utf-8')
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

    alfabet = 'abcdefghijklmnopqrstuvwxyząćęłńóśź'
    pierwsze = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149]
    mapa = dict(zip(alfabet, pierwsze))

    def iloczyn(s):
        return reduce((lambda n1, n2: n1*n2), [mapa[litera] for litera in s])

    cel = iloczyn(slowo)
    cos = 0

    for i in T:
        if i[0] == i[1]:
            for a in range(len(anadl[i[0]])-1):
                temp = iloczyn(anadl[i[0]][a])
                for b in range(a+1,len(anadl[i[0]])):
                    temp1 = temp * iloczyn(anadl[i[0]][b])
                    if cel%temp1 != 0: continue
                    for c in anadl[i[2]]:
                        temp2 = temp1 * iloczyn(c)
                        if temp2 == cel: 
                            cos = cos + 1
                            print(anadl[i[0]][a],anadl[i[0]][b],c)

        elif i[1] == i[2]:
            for b in range(len(anadl[i[1]])-1):
                temp = iloczyn(anadl[i[1]][b])
                for c in range(b+1,len(anadl[i[1]])):
                    temp1 = temp * iloczyn(anadl[i[1]][c])
                    if cel%temp1 != 0: continue
                    for a in anadl[i[0]]:
                        temp2 = temp1 * iloczyn(a)
                        if temp2 == cel: 
                            cos = cos + 1
                            print(a,anadl[i[1]][b],anadl[i[1]][c])
        elif i[0] == i[2]:
            for a in range(len(anadl[i[0]])-1):
                temp = iloczyn(anadl[i[0]][a])
                for c in range(a+1,len(anadl[i[0]])):
                    temp1 = temp * iloczyn(anadl[i[0]][c])
                    if cel%temp1 != 0: continue
                    for b in anadl[i[1]]:
                        temp2 = temp1 * iloczyn(b)
                        if temp2 == cel: 
                            cos = cos + 1
                            print(anadl[i[0]][a],b,anadl[i[0]][c])

        elif i[0] == i[1] == i[2]:
            for a in range(len(anadl[i[0]])-2):
                temp = iloczyn(anadl[i[0]][a])
                for b in range(a+1,len(anadl[i[0]])-1):
                    temp1 = temp * iloczyn(anadl[i[0]][b])
                    if cel%temp1 != 0: continue
                    for c in range(b+1,len(anadl[i[0]])):
                        temp2 = temp1 * iloczyn(anadl[i[0]][c])
                        if temp2 == cel: 
                            cos = cos + 1
                            print(anadl[i[0]][a],anadl[i[0]][b],anadl[i[0]][c])

        else:
            for a in anadl[i[0]]:
                temp = iloczyn(a)
                for b in anadl[i[1]]:
                    temp1 = temp * iloczyn(b)
                    if cel%temp1 != 0: continue
                    for c in anadl[i[2]]:
                        temp2 = temp1 * iloczyn(c)
                        if temp2 == cel: 
                            cos = cos + 1
                            print(a,b,c)
                            
    print(cos)
    print("Done")

szukanieanagramow('Krzyszof Loryś')
print("--- %s seconds ---" % (time.time() - start_time))
print()

