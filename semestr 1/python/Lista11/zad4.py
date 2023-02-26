import csv

def importlisty():
    plik = open("wyniki_wyborow.tsv",encoding='utf-8')
    dane = list(csv.reader(plik, delimiter="\t"))
    for i in dane: print(i)
    print()
    return dane

def mandaty(dane = importlisty()):
    wyniki = dict()
    for i in range(3,len(dane[0])): wyniki[dane[0][i]] = 0

    for i in range(1,len(dane)):
        okrag = dane[i]
        M = int(okrag[2])
        ilorazy = list()

        for komitet in range(3,len(dane[i])):
            if dane[i][komitet] == '–': continue
            for m in range(1,M+1): ilorazy.append((dane[0][komitet], float(dane[i][komitet].replace(',','.')) / m))
        
        ilorazy.sort(key=lambda x: x[1], reverse=True)
        for m in range(M): wyniki[ilorazy[m][0]] += 1
        print(wyniki)

mandaty()