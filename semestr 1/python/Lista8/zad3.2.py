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
    slowo = slowo.lower()
    slowo = slowo.replace(' ','')
    for i in range(1,len(slowo)):
        s1 = ''.join(sorted(slowo[i:]))
        s2 = ''.join(sorted(slowo[:i]))
        print(s1,s2)
        if s1 in d and s2 in d:
            print(d[s1])
            print(d[s2])

szukanieanagramow('Bolesław Prus')