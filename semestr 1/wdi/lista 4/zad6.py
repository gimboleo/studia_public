from wdi import *

T = Array(100)
def palindromn(a,n):
    l = 0
    while a>0:
        T[l] = a%n
        a = a//n
        l = l+1

    for i in range(l-1,-1,-1):
        print(T[i],T[l-1-i])

    for i in range(l-1,-1,-1):
        if T[i] != T[l-1-i]: return False
    return True

print(palindromn(8057,8))