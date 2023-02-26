from collections import defaultdict
from collections import Counter
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

def szukanieanagramow(slowo,slownik):
    slowo = slowo.lower()
    slowo = slowo.replace(' ','')
    anagramy = set()
    licznik = Counter(slowo)
    for s in slownik:
        if set(s).issubset(set(slowo)):
            litery = set()
            for k,v in Counter(s).items():
                if v <= licznik[k]: litery.add(k)
            if litery == set(s): anagramy.add(s)
    print(anagramy)

szukanieanagramow('Bolesław Prus',importlisty())