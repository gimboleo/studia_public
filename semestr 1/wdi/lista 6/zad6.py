from wdi import *


def sqrt(n):
    sqr = n/2
    temp = 0

    while sqr != temp:
        temp = sqr
        sqr = (n / temp + temp) / 2 
    
    return sqr


def prostesito(limit):
    T = Array(limit+1)
    for i in range(2,limit+1):
        T[i] = 1
    
    for i in range(2,int(sqrt(limit))):
        if T[i]:
            for j in range(i*2,limit+1,i):
                T[j] = 0
    
    for i in range(2,limit+1):
        if T[i]: print(i)

    return T


def segmentowanesito(m,n):
    limit = int(sqrt(n))
    S = prostesito(limit)

    dol = m
    gora = dol + limit

    while dol < n:
        if gora >= n: gora = n

        T = Array(limit+1)
        for i in range(limit+1):
            T[i] = 1

        for i in range(limit+1):
            if S[i]:
                for j in range(dol,gora+1):
                    if j%i == 0:
                        minim = j
                        break
                for j in range(minim,gora,i):
                    T[j-dol] = 0

        for i in range(dol,gora):
            if T[i-dol]: print(i)

        dol = dol + limit
        gora = gora + limit 


segmentowanesito(10000,15000)