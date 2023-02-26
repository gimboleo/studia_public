from collections import defaultdict as dd

import time
start_time = time.time()

def importlisty():
    #plik = open(r'C:\Users\kubak\Desktop\Python\Lista8\slowa.txt','r',encoding='utf-8')
    plik = open(r'C:\Users\kubak\Desktop\Python\Lista10\test.txt','r',encoding='utf-8')
    L = plik.read().splitlines()
    return L

def parycezarskie(slownik=importlisty()):

    dl = dd(list)
    for i in slownik:
        dl[len(i)].append(i)

    alfabet = 'aąbcćdeęfghijklłmnńoóprsśtuwyzźż'
    mapa = dict(zip(alfabet, [i for i in range(1,len(alfabet)+1)]))
    mapa2 = dict(zip([i for i in range(1,len(alfabet)+1)], alfabet))

    done = False

    for i in range(max(dl.keys()),min(dl.keys())-1,-1):
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
                        x = (mapa[dl[i][j][l]] + przesuniecie)%len(alfabet)
                        if x == 0: x = len(alfabet)
                        if mapa2[x] != dl[i][k][l]: break
                        if l == i-1: 
                            done = True
                            para = True
                    if para: print(dl[i][k],dl[i][j])
        if done: break




parycezarskie()
print("--- %s seconds ---" % (time.time() - start_time))
