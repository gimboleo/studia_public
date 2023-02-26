from wdi import *


def sqrt(n):
    sqr = n/2
    temp = 0

    while sqr != temp:
        temp = sqr
        sqr = (n / temp + temp) / 2 
    
    return sqr


def zad5(n):
    T = Array(n+1)
    for i in range(2,n+1):
        T[i] = 1
    
    for i in range(2,int(sqrt(n))):
        if T[i]:
            for j in range(i*2,n+1,i):
                T[j] = 0
    
    for i in range(2,n+1):
        if T[i]: print(i)    


zad5(200)
