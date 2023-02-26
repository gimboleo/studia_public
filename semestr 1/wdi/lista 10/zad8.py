class ListItem:
    def __init__(self,value):
        self.val = value
        self.prev = None
        self.next = None

def wypisz(lista):
    while lista:
        if lista.prev: print('prev:',lista.prev.val,'|',end=' ')
        else: print('        |',end=' ')
        if lista.next: print('next:',lista.next.val,'|',end=' ')
        else: print('        |',end=' ')
        print(lista.val)
        lista = lista.next
    print()

def wstawKon(lista,nval):
    nowy = ListItem(nval)
    temp = lista
    while temp.next != None: temp = temp.next
    temp.next = nowy
    nowy.prev = temp
    return lista

def usunPierw(lista):
    temp = lista.next
    temp.prev = None
    return temp

L = ListItem(1)
wypisz(L)

print()

L = wstawKon(L,2)
L = wstawKon(L,3)
L = wstawKon(L,4)
wypisz(L)

print()

L = usunPierw(L)
wypisz(L)

