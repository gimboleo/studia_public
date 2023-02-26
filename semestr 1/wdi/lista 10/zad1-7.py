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

def usunOst(lista):
    temp = lista
    while temp.next != None:
        poprz = temp
        temp = temp.next
    poprz.next = None
    return lista

def polacz(lista1,lista2):
    temp = lista1
    while temp.next != None: temp = temp.next
    temp.next = lista2
    return lista1

def usun(lista,uval):
    if lista.val == uval: return usun(lista.next,uval)
    temp = lista
    while temp.next != None:
        poprz = temp
        temp = temp.next
        if temp.val == uval: poprz.next = temp.next
    return lista

def wypiszOdKon(lista):
    if lista.next != None: wypiszOdKon(lista.next)
    print(lista.val,end= ' ')

def odwroc(lista):
    poprz = None
    obec = lista
    while obec:
        nast = obec.next
        obec.next = poprz
        poprz = obec
        obec = nast
    return poprz

def doduje(lista):
    dod = ListItem(0)
    uje = ListItem(0)
    tdod = dod
    tuje = uje
    temp = lista
    while temp:
        x = temp.val
        i = ListItem(x)
        if x<0:
            tuje.next = i
            tuje = tuje.next
        else:
            tdod.next = i
            tdod = tdod.next
        temp = temp.next
    yield dod.next
    yield uje.next

def rozdziel(lista):
    dod = None
    uje = None
    tdod = dod
    tuje = uje
    temp = lista
    while temp:
        if temp.val<0:
            if not uje:
                uje = temp
                temp = temp.next
                uje.next = None
                tuje = uje
            else:
                uje.next = temp
                uje = uje.next
                nast = temp.next
                temp.next = None
                temp = nast
        else:
            if not dod:
                dod = temp
                temp = temp.next
                dod.next = None
                tdod = dod
            else:
                dod.next = temp
                dod = dod.next
                nast = temp.next
                temp.next = None
                temp = nast
    yield tdod
    yield tuje


L = ListItem(1)
wypisz(L)

print()

L = wstawKon(L,2)   #1
L = wstawKon(L,3)
wypisz(L)

print()

L = usunOst(L)      #2
wypisz(L)

print()

L2 = ListItem(1)    #3
L2 = wstawKon(L2,5)
L2 = wstawKon(L2,6)
L2 = wstawKon(L2,1)
wypisz(L2)
L = polacz (L,L2)
wypisz(L)

print()

L = usun(L,1)       #4
wypisz(L)

print()

wypiszOdKon(L)      #5
print()

print()

L = odwroc(L)       #6
wypisz(L)

print()

L = wstawKon(L,-1)  #7
L = wstawKon(L,-5)
wypisz(L)
for i in doduje(L):
    wypisz(i)

print()

for i in rozdziel(L):
    wypisz(i)