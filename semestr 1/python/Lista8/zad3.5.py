from collections import Counter
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

    anagramy = list(anagramy)
    sortowane = ''.join(sorted(slowo))

    for i in range(len(anagramy)-1):
        for j in range(i+1,len(anagramy)):
            if ''.join(sorted(anagramy[i]+anagramy[j])) == sortowane:
                print(anagramy[i],anagramy[j])

szukanieanagramow('Krzysztof Loryś')
print()

