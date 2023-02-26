def nwd(a,b):
    if a<b:
        c = a
        a = b
        b = c
    while(b>0):
        a = a%b
        if a<b:
            c = a
            a = b
            b = c
    return a

def nww(a,b):
    return a * b // nwd(a,b)

def nowy_ulamek(num, denom):
    assert denom != 0, "Mianownik nie moze byc rowny zero."
    if denom < 0:
        denom = -denom
        num = - num
    
    x = nwd(abs(num), abs(denom))
    return [num / x, denom / x]

def uproszczenie(f):
    x = nwd(abs(f[0]), abs(f[1]))
    f[0] = f[0] / x
    f[1] = f[1] / x    

def dodawanie_nowy(a,b):
    if a[1] == b[1]: return [a[0] + b[0], a[1]]
    else:
        denom = nww(a[1], b[1])
        return [a[0] * denom / a[1] + b[0] * denom / b[1] , denom]

def dodawanie_drugi(a,b):
    if a[1] == b[1]: b[0] = a[0] + b[0]
    else:
        denom = nww(a[1], b[1])
        b[0] = a[0] * denom / a[1] + b[0] * denom / b[1]
        b[1] = denom

def odejmowanie_nowy(a,b):
    if a[1] == b[1]: return [a[0] - b[0], a[1]]
    else:
        denom = nww(a[1], b[1])
        return [a[0] * denom / a[1] - b[0] * denom / b[1] , denom]

def odejmowanie_drugi(a,b):
    if a[1] == b[1]: b[0] = a[0] - b[0]
    else:
        denom = nww(a[1], b[1])
        b[0] = a[0] * denom / a[1] - b[0] * denom / b[1]
        b[1] = denom

def mnozenie_nowy(a,b):
    return [a[0] * b[0], a[1] * b[1]]

def mnozenie_drugi(a,b):
    b[0] = a[0] * b[0]
    b[1] = a[1] * b[1]

def dzielenie_nowy(a,b):
    assert b[0] != 0, "Nie można dzielić przez zero."
    l = a[0] * b[1]
    m  = a[1] * b[0]
    if m < 0:
        l = -l
        m = -m
    return [l, m]

def dzielenie_drugi(a,b):
    assert b[0] != 0, "Nie można dzielić przez zero."
    b[0], b[1] = a[0] * b[1], a[1] * b[0]
    if b[1] < 0:
        b[0] = -b[0]
        b[1] = -b[1]
