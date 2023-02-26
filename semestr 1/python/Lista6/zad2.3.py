def importlisty():
    plik = open(r'C:\Users\kubak\Desktop\Python\Lista6\slowa.txt','r',encoding='utf-8')
    L = plik.read().splitlines()
    return L

def pary(L):
    d = dict()
    for i in L:
        #print(d)
        if i[::-1] in d:
            d[i[::-1]] = 0
        d[i] = 1
        if i == i[::-1]: d[i] = 0

    x = 0
    for i in d.keys():
        if d[i] == 0:
            print(i,i[::-1])
            x = x+1
    print(x)

lista = "maja kot ajam pokaz zakop maja zima lato otal ala ala ala".split()
#pary(lista)
pary(importlisty())