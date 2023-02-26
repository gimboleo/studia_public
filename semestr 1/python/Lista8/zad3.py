from collections import defaultdict
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
    klucz = ''.join(sorted(slowo))
    if klucz in d:
        print(d[klucz],klucz)
    else:
        print("Brak")

szukanieanagramow('wsparł')