from collections import defaultdict as dd
import itertools

import time
start_time = time.time()

def importlisty():
    plik = open(r'C:\Users\kubak\Desktop\Python\Lista8\slowa.txt','r',encoding='utf-8')
    #plik = open(r'C:\Users\kubak\Desktop\Python\Lista10\test.txt','r',encoding='utf-8')
    L = plik.read().splitlines()
    return L

def caesar(s,k):
    s = s.lower()
    alfabet = 'aąbcćdeęfghijklłmnńoóprsśtuwyzźż'
    mapa = dict(zip(alfabet, ''.join((alfabet[k:],alfabet[:k]))))
    wynik = ''.join([mapa[l] for l in s])
    return wynik

def parycezarskie(slownik=importlisty()):

    dl = dd(list)
    for i in slownik:
        dl[len(i)].append(i)

    alfabet = 'aąbcćdeęfghijklłmnńoóprsśtuwyzźż'

    for i in range(max(dl.keys()),min(dl.keys())-1,-1):
        if i not in dl: continue
        dlli = len(dl[i])
        print(i,dlli)
        temp = list()
        for e in dl[i]:
            if all(c in alfabet for c in e): temp.append(e)
        slownik = dict()
        zbior = set(temp)
        while zbior:
            x = zbior.pop()
            slownik[x] = [x]
            for i in range(1,32):
                y = caesar(x,i)
                if y in zbior:
                    zbior.remove(y)
                    slownik[x].append(y)
        test = sorted([(len(v), k) for k, v in slownik.items()], reverse=True)
        if test and test[0][0] > 1:
            for k in range(len(test)):
                if test[k][0] <= 1: break
                print(slownik[test[k][1]])
            break

parycezarskie()
print("--- %s seconds ---" % (time.time() - start_time))
