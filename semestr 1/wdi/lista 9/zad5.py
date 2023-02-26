from wdi import *

def isfree(x,y,wynik,suma,k):
    if x == n-1:
        temp = k
        for i in range(0,n-1): temp += wynik[y][i]
        if temp != suma: return False
    if y == n-1:
        temp = k
        for i in range(0,n-1): temp+= wynik[i][x]
        if temp != suma: return False
        if x == 0:
            temp = k
            for i in range(1,n): temp += wynik[y-i][x+i]
            if temp != suma: return False
        if x == n-1:
            temp = k
            for i in range(1,n): temp += wynik[y-i][x-i]
            if temp != suma: return False
    return True

def magia(wynik,mozliwe,kroki):
    if kroki == n*n: return True

    y = kroki//n
    x =  kroki - n*(kroki//n)

    for k in range(1,n*n+1):
        if mozliwe[k] and isfree(x,y,wynik,suma,k):
            wynik[y][x] = k
            mozliwe[k] = False

            if magia(wynik,mozliwe,kroki+1): return True
            wynik[y][x] = 0
            mozliwe[k] = True

    return False

def init():
    wynik = Array(n,n)
    for i in range(n):
        for j in range(n):
            wynik[i][j] = 0

    mozliwe = Array(n*n+1)
    for i in range(1,n*n+1):
        mozliwe[i] = True

    if magia(wynik,mozliwe,0):
        for i in range(n):
            for j in range(n):
                if wynik[i][j] < 10: print(wynik[i][j],end='  ')
                else: print(wynik[i][j],end=' ')
            print()
    else: print('False')

n = 4
suma = n*(n*n+1)/2
init()