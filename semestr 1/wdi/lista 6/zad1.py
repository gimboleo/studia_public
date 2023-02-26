from wdi import *

def zad1(T,i):
    x = T[i]
    lewy = 0
    prawy = i-1
    while prawy - lewy != 1:
        k = (lewy + prawy) // 2
        if T[k] < x: lewy = k
        else: prawy = k
    k += 1
    lewy = k
    print(lewy)

T = Array(7)
T[0] = 1
T[1] = 3
T[2] = 5
T[3] = 5
T[4] = 5
T[5] = 7
T[6] = 6
i = 6

zad1(T,i)