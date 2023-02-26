from wdi import *

def zapis(n):
    T = Array(10)
    while n>0:
        T[n%10] = T[n%10] + 1
        n = n//10
    x = 0
    for i in range(10):
        if T[i] != 0: x = x+1
    print(x)

zapis(1232123)
