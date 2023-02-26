import click
from math import sqrt

def pierwsza(n):
    if n>1:
        for i in range(2,(int(sqrt(n))+1)): #pierwiastek zamiast n//2
            if (n%i == 0):
                return False
        return True
    return False

'''                             #testowanie algorytmu bez sprawdzania pierwszych, dla 10 i 7 z kombinatoryki powinno dawac 3700
def pierwsza(n): 
    return True
'''

def luckynumber(ln,svn):        #ln - ilosc cyfr; svn - ilosc siodemek; strnsvn - siodemki w stringu; x -licznik; inne - cyfry niesiodemkowe; reszta - konkretny zestaw tych cyfr
    x = 0
    L = set()                   #Zlicza je bez powtórek
    strsvn = '7' * svn
    inne = ln - svn
    for i in range(10**inne):
        reszta = '0'*(inne-len(str(i))) + str(i)
        for j in range(inne+1):
            liczba = int(reszta[0:inne-j] + strsvn + reszta[inne-j:inne]) ### XXX0 XX0X X0XX 0XXX - 4 kombinacje dla inne = 3
            if len(str(liczba)) == ln and pierwsza(liczba):               ### Jak kombinacja zaczynala sie zerami to nie sprawdza, np. inne = 037; X0XX; liczba = '0777777737'
                L.add(liczba)
                print(liczba)
                x = x+1
    print(L)
    print(x)
    print(len(L),'unikalnych')
    
luckynumber(10,7)
if click.confirm('Custom?', default=False):
    a = int(input('ln: '))
    b = int(input('svn: '))
    luckynumber(a,b)
    