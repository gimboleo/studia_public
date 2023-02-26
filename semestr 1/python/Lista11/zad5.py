import csv

def importlisty():
    plik = open("wyniki_wyborow.tsv",encoding='utf-8')
    dane = list(csv.reader(plik, delimiter="\t"))
    #for i in dane: print(i)
    #print()
    return dane

def relacje(lista):
    if len(lista) == 1:
        yield [lista]
        return

    pierwszy = lista[0]
    for ogon in relacje(lista[1:]):
        for i, podzbior in enumerate(ogon): 
            yield ogon[:i] + [[pierwszy] + podzbior] + ogon[i+1:] 
        yield [[pierwszy]] + ogon

def mandaty2(dane = importlisty()):
    partie = dane[0][3:-1]
    pom = dict(zip(partie, range(3,len(partie)+2)))
    osiemgwiazd = list(relacje(partie[:-1]))
    wszystkie = list()

    for koalicje in osiemgwiazd:
        wyniki = dict()
        for komitet in koalicje: wyniki['-'.join(komitet)] = 0

        for i in range(1,len(dane)):
            okrag = dane[i]
            M = int(okrag[2])
            ilorazy = list()

            for komitet in koalicje:
                x = sum([float(dane[i][pom[partia]].replace(',','.')) for partia in komitet])
                for m in range(1,M+1): ilorazy.append(('-'.join(komitet), x / m))
        
            ilorazy.sort(key=lambda x: x[1], reverse=True)
            for m in range(M): wyniki[ilorazy[m][0]] += 1

        wszystkie.append(wyniki)
    
    print()
    print("Koalicje antypisowskie:")
    for wyniki in wszystkie:
        wygrany = max(wyniki, key=wyniki.get)
        if 'PiS' not in wygrany: print(wyniki)

    print()
    print("Większość konstytucyjna:")
    for wyniki in wszystkie:
        wygrany = max(wyniki, key=wyniki.get)
        if wyniki[wygrany] >= 307: print(wyniki)

mandaty2()