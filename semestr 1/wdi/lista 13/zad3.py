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

def przeszukaj(T,n,s):
    L = Array(n)
    for i in range(1,n): L[i] = T[i]
    odw = Array(n)
    odw[s] = 1
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
                odw[w] = 1
    return odw

def most(T,n,s1,s2):
    W1 = przeszukaj(T,n,s1)
    T[s1] = usun(T[s1],s2)
    T[s2] = usun(T[s2],s1)
    W2 = przeszukaj(T,n,s1)
    T[s1] = wstawKon(T[s1],s2)
    T[s2] = wstawKon(T[s2],s1)
    for i in range(1,n):
        if W1[i] != W2[i]: return True
    return False

def czymost(T,n):
    for i in range(1,n-1):
        for j in range(i+1,n):
            if most(T,n,i,j): return True
    return False

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

x = 5 + 1

L2 = Array(x)
L2[1] = ListItem(1)
wstawKon(L2[1],2)
wstawKon(L2[1],5)
L2[2] = ListItem(2)
wstawKon(L2[2],1)
wstawKon(L2[2],3)
L2[3] = ListItem(3)
wstawKon(L2[3],2)
wstawKon(L2[3],4)
L2[4] = ListItem(4)
wstawKon(L2[4],3)
wstawKon(L2[4],5)
L2[5] = ListItem(5)
wstawKon(L2[5],4)
wstawKon(L2[5],1)

print(czymost(L,n))
print(czymost(L2,x))