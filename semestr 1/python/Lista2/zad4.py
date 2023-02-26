from duze_cyfry import daj_cyfre
    
liczba = input("Podaj liczbę: ")
dlugosc = len(liczba)
for i in range(5):
    for j in range(dlugosc):
        print(daj_cyfre(int(liczba[j]))[i],end=" ")
    print()