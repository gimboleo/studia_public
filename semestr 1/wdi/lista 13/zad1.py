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

def array_to_list(T,n):
    W = Array(n)
    for i in range(1,n):
        W[i] = ListItem(i)
        temp = W[i]
        for j in range(1,n):
            if T[i][j]:
                temp.next = ListItem(j)
                temp = temp.next
    return W

def list_to_array(T,n):
    W = Array(n,n)
    for i in range(1,n):
        temp = T[i]
        while temp.next:
            temp = temp.next
            W[i][temp.val] = 1
    return W

n = 7 + 1

T = Array(n,n)
T[1][5] = 1
T[1][6] = 1
T[1][7] = 1
T[3][4] = 1
T[4][3] = 1
T[5][1] = 1
T[5][6] = 1
T[6][1] = 1
T[6][5] = 1
T[6][7] = 1
T[7][1] = 1
T[7][6] = 1

L = Array(n)
L[1] = ListItem(1)
wstawKon(L[1],2)
wstawKon(L[1],5)
wstawKon(L[1],6)
L[2] = ListItem(2)
wstawKon(L[2],1)
L[3] = ListItem(3)
wstawKon(L[3],4)
L[4] = ListItem(4)
L[5] = ListItem(5)
L[6] = ListItem(6)
wstawKon(L[6],5)
wstawKon(L[6],7)
L[7] = ListItem(7)
wstawKon(L[7],1)


W1 = array_to_list(T,n)
for i in range(1,n):
    wypisz(W1[i])

print()
print()

W2 = list_to_array(L,n)
for i in range(1,n):
    for j in range(1,n):
        print(W2[i][j],end=' ')
    print()