from wdi import *

def init():
    for i in range(n):
        b[i] = -1
    
def isf(x,y):
    for i in range(x):
        if b[i]-i == y-x or b[i]+i == y+x or b[i] == y: return 0
    return 1

def queens():
    b[0] = 0
    k = 1
    x = 0
    while k<n and k>=0:
        b[k] += 1
        if k == n-1:
            while b[k] < n:
                if isf(k,b[k]): x += 1
                b[k] += 1
            b[k] = -1
            k -= 1
        else:
            while b[k]<n and not isf(k,b[k]):
                b[k] += 1
            if b[k]<n: k += 1
            else: b[k] =- 1; k -= 1
    return x

n=8 # rozmiar szachownicy
b=Array(n)
init()
print(queens())
