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
    if isinstance(lista,int): return 0
    if lista.val == uval: return usun(lista.next,uval)
    temp = lista
    while temp.next != None:
        poprz = temp
        temp = temp.next
        if temp.val == uval: poprz.next = temp.next
    return lista

def przeszukaj(T,n,s,odw):
    L = Array(n)
    for i in range(1,n): L[i] = T[i]
    odw[s] = s
    B = set()
    B.add(s)
    while B:
        v = B.pop()
        if L[v]:
            B.add(v)
            w = L[v].val
            L[v] = L[v].next
            if not odw[w]:
                B.add(w)
                odw[w] = s
    return odw

def skladowe(T,n):
    odw = Array(n)
    for i in range(1,n):
        if odw[i] == 0: odw = przeszukaj(T,n,i,odw)
    return odw

def artykulacja(T,n,s):
    x = skladowe(T,n)
    L = Array(n)
    for i in range(1,s): L[i] = T[i]
    for i in range(s+1,n): L[i] = T[i]
    for i in range(1,n): L[i] = usun(L[i],s)
    x2 = skladowe(L,n)
    z = set()
    z2 = set()
    for i in range(1,n): 
        print(x[i],end=' ')
        z.add(x[i])
    print()
    for i in range(1,s): 
        print(x2[i],end=' ')
        z2.add(x2[i])
    print(' ',end=' ')
    for i in range(s+1,n): 
        print(x2[i],end=' ')
        z2.add(x2[i])
    print()
    if len(z) != len(z2): print(True)
    else: print(False)
       
x = 6 + 1

X = Array(x)
X[1] = ListItem(1)
wstawKon(X[1],2)
wstawKon(X[1],3)
X[2] = ListItem(2)
wstawKon(X[2],3)
X[3] = ListItem(3)
wstawKon(X[3],4)
X[4] = ListItem(4)
wstawKon(X[4],5)
wstawKon(X[4],6)
X[5] = ListItem(5)
wstawKon(X[5],6)
X[6] = ListItem(6)
wstawKon(X[6],4)
wstawKon(X[6],5)

artykulacja(X,x,1)
print()
artykulacja(X,x,3)