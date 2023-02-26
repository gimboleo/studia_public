from losowanie_fragmentow import losuj_fragment

def losuj_haslo(n):
    dlugosc = n
    haslo = ""
    while True:
        if dlugosc == 0:
            break
        modul = losuj_fragment()
        if dlugosc >= len(modul) and dlugosc - len(modul) != 1:
            haslo = haslo + modul
            dlugosc = dlugosc - len(modul)
    print(haslo)
    
m = int(input("Dlugosc hasla: "))
losuj_haslo(m)
print()

for i in range(10):
    losuj_haslo(8)
print()

for i in range(10):
    losuj_haslo(12)
    