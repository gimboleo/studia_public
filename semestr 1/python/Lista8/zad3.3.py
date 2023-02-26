from collections import defaultdict
from itertools import permutations
def importlisty():
    plik = open(r'C:\Users\kubak\Desktop\Python\Lista8\slowa.txt','r',encoding='utf-8')
    L = plik.read().splitlines()
    return L

def anagramy(L):
    d = defaultdict(list)
    for slowo in L:
        klucz = ''.join(sorted(slowo))
        d[klucz].append(slowo)
    return d

def szukanieanagramow(slowo):
    d = anagramy(importlisty())
    slowo = slowo.lower()
    slowo = slowo.replace(' ','')
    T = [''.join(p) for p in permutations(slowo)]
    for p in T:
        for i in range(1,len(p)):
            s1 = ''.join(sorted(p[i:]))
            s2 = ''.join(sorted(p[:i]))
            if s1 in d and s2 in d:
                print(d[s1])
                print(d[s2])

szukanieanagramow('Bolesław Prus')