from wdi import *

class ListItem:
    def __init__(self,value):
        self.val = value
        self.next = None

def wypisz(lista):
    while lista != None:
        print(lista.val,end=' ')
        lista = lista.next
    print()

def wstawKon(lista,nval):
    nowy = ListItem(nval)
    temp = lista
    while temp.next != None: temp = temp.next
    temp.next = nowy
    return lista

def usun(lista,uval):
    if lista.val == uval: return usun(lista.next,uval)
    temp = lista
    while temp.next != None:
        poprz = temp
        temp = temp.next
        if temp.val == uval: poprz.next = temp.next
    return lista

def przeszukaj(T,n,s,s2):
    L = Array(n)
    d = Array(n)
    sc = Array(n)
    for i in range(1,n): 
        L[i] = T[i]
        d[i] = -1
    sc[0] = s
    odw = Array(n)
    odw[s] = 1
    K = ListItem(s)
    d[s] = 0
    while K:
        v = K.val
        if not L[v]: K = K.next
        else:
            w = L[v].val
            L[v] = L[v].next
            if not odw[w]:
                K = wstawKon(K,w)
                odw[w] = 1
                d[w] = d[v] + 1
                sc[d[w]-1] = v
                sc[d[w]] = w
                if w == s2: return sc
    return -1

n = 7 + 1

L = Array(n)
L[1] = ListItem(1)
wstawKon(L[1],2)
wstawKon(L[1],5)
wstawKon(L[1],6)
wstawKon(L[1],7)
L[2] = ListItem(2)
wstawKon(L[2],1)
L[3] = ListItem(3)
wstawKon(L[3],4)
L[4] = ListItem(4)
wstawKon(L[4],3)
L[5] = ListItem(5)
wstawKon(L[5],1)
wstawKon(L[5],6)
L[6] = ListItem(6)
wstawKon(L[6],1)
wstawKon(L[6],5)
wstawKon(L[6],7)
L[7] = ListItem(7)
wstawKon(L[7],1)
wstawKon(L[7],6)

x = 7 + 1

X = Array(x)
X[1] = ListItem(1)
wstawKon(X[1],2)
wstawKon(X[1],3)
X[2] = ListItem(2)
wstawKon(X[2],4)
X[3] = ListItem(3)
wstawKon(X[3],2)
wstawKon(X[3],7)
X[4] = ListItem(4)
wstawKon(X[4],5)
wstawKon(X[4],6)
X[5] = ListItem(5)
wstawKon(X[5],6)
X[6] = ListItem(6)
wstawKon(X[6],4)
wstawKon(X[6],5)

wynik = przeszukaj(L,n,1,6)
if wynik != -1:
    for i in range(n): 
        if not wynik[i]: break
        print(wynik[i],end=' ')
else: print(-1)

print()

wynik = przeszukaj(X,x,1,6)
if wynik != -1:
    for i in range(x): 
        if not wynik[i]: break
        print(wynik[i],end=' ')
else: print(-1)
