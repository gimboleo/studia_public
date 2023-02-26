from collections import defaultdict as dd

def importlisty():
    plik = open(r'C:\Users\kubak\Desktop\Python\Lista8\slowa.txt','r',encoding='utf-8')
    L = plik.read().splitlines()
    return L

def parycezarskie(slownik=importlisty()):

    dl = dd(list)
    for i in slownik:
        dl[len(i)].append(i)

    alfabet = 'aąbcćdeęfghijklłmnńoóprsśtuwyzźż'
    mapa = dict(zip(alfabet, [i for i in range(1,len(alfabet)+1)]))

    done = False

    for i in range(max(dl.keys()),min(dl.keys()),-1):
        if i not in dl: continue
        dlli = len(dl[i])
        print(i,dlli)
        for j in range(dlli-1):
            for k in range(j+1,dlli):
                para = False
                if dl[i][k][0] in mapa and dl[i][j][0] in mapa:
                    przesuniecie = mapa[dl[i][k][0]] - mapa[dl[i][j][0]]
                    if przesuniecie == 0: continue
                    for l in range(1,i):
                        if dl[i][k][l] not in mapa or dl[i][j][l] not in mapa: break
                        if mapa[dl[i][k][l]] - mapa[dl[i][j][l]] != przesuniecie: break
                        if l == i-1: 
                            done = True
                            para = True
                    if para: print(dl[i][k],dl[i][j])
        if done: break




parycezarskie()