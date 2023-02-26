from wdi import *

def wartosc(a,k):
    w = 0
    for i in range(k+1):
        w = 2*w + a[i]
    print(w)

a = Array(4)
a[0] = 1
a[1] = 0
a[2] = 1
a[3] = 0
k = 3

wartosc(a,k)