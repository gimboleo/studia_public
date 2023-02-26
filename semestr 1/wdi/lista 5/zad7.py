def pot(a, b):
    rez = 1
    while b>0:
        if b%2:
            rez = rez * a
        b = b // 2
        a = a * a
    return rez

def potega(a,b):
    n = a
    m = b
    i = 0
    while n<m:
        n = n*n
        i = i+1
    
    M = pot(2,i)
    m = M//2
    while True:
        srodek = (m+M) // 2
        mc = pot(a,srodek)
        ml = pot(a,srodek-1) 
        if mc >= b and ml < b: return srodek
        elif mc >= b and ml > b: M = srodek
        else: m = srodek


print(potega(2,1000))