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

def polaczsort(lista1,lista2):
    if lista2.val < lista1.val: 
        x = temp = lista2
        temp2 = lista1
    else: 
        x = temp = lista1
        temp2 = lista2
    while temp.next and temp2:
        while temp.next and temp2 and temp.next.val <= temp2.val: temp = temp.next
        temp3 = temp.next
        temp.next = temp2
        temp2 = temp3
    return x

L = ListItem(1)
L = wstawKon(L,2)
L = wstawKon(L,3)
L = wstawKon(L,3)
L = wstawKon(L,5)
L = wstawKon(L,11)

L2 = ListItem(1)
L2 = wstawKon(L2,6)
L2 = wstawKon(L2,6)
L2 = wstawKon(L2,9)
L2 = wstawKon(L2,11)

wypisz(L)
wypisz(L2)

print()

L = polaczsort(L,L2)
wypisz(L)
