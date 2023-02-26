def pascal(n):
    if n == 1: return [[1]]
    nowy_rzad = [1]
    stary_rzad = pascal(n-1)
    for i in range(len(stary_rzad)-1):
        nowy_rzad.append(stary_rzad[i]+stary_rzad[i+1])
    nowy_rzad+=[1]
    return nowy_rzad

print(pascal(6))