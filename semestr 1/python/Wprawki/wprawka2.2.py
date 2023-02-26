def pascal(n):
    if n == 0: return [[1]]
    nowy_rzad = [1]
    wynik = pascal(n-1)
    stary_rzad = wynik[-1]
    for i in range(len(stary_rzad)-1):
        nowy_rzad.append(stary_rzad[i]+stary_rzad[i+1])
    nowy_rzad+=[1]
    wynik.append(nowy_rzad)
    return wynik

print(pascal(4))