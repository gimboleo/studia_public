from wdi import *

def zapis(n):
    T = Array(10)
    while n>0:
        T[n%10] = T[n%10] + 1
        n = n//10
    return T

def podobne(a,b):
    A = zapis(a)
    B = zapis(b)
    for i in range(10):
        if A[i] != B[i]: return False
    return True

print(podobne(55573,73555))