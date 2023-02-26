import re
import string
class dlugosc(Exception):
    pass
class malelitery(Exception):
    pass
class duzelitery(Exception):
    pass
class znakispecjalne(Exception):
    pass
class cyfra(Exception):
    pass
class baza(Exception):
    pass

def register(haslo):
    try:
        if len(haslo) < 9: raise dlugosc

        d = set()
        D = set()
        specjalne = 0
        cyfry = 0
        for litera in haslo:
            if litera.islower():
                d.add(litera)
            if litera.isupper():
                D.add(litera)
            if litera in string.punctuation:
                specjalne = specjalne + 1
            if litera.isdigit():
                cyfry = cyfry + 1
        if len(d) < 2: raise malelitery
        if len(D) < 2: raise duzelitery
        if specjalne < 2: raise znakispecjalne
        if cyfry < 2: raise cyfra

        with open(r'C:\Users\kubak\Desktop\Python\Wprawki\users.db',encoding='utf-8') as plik:
                tmp = re.findall(r'\:.*? ',plik.read())
        for i in range(len(tmp)):
            tmp[i] = tmp[i][1:]
            tmp[i] = tmp[i][:-1]
        if haslo in tmp: raise baza

    except dlugosc:
        print('hasło za krótkie')
    except malelitery:
        print('za mało unikalnych małych liter')
    except duzelitery:
        print('za mało unikalnych dużych liter')
    except znakispecjalne:
        print('za mało znaków specjalnych')
    except cyfra:
        print('za mało cyfr')
    except baza:
        print('hasło znalezione w bazie')
    else:
        print('rejestracja przebiegła pomyślnie')

register('abc')
register('aaaaaaaaaaaaaa')
register('abcdefghijkkGG')
register('abcdefghijkkGHG')
register('azsxdcfvgaBVaa!!')
register('FLORENci@@18')
register('azsxdcfvgaBVa00a!!')