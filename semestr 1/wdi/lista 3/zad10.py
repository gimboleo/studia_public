from wdi import *

def u2(n,i):
    if n >= 0:
        if n > 1:
            u2(n // 2, i-1)
        T[i] = n%2

b = 24
T = Array(b)
a = int(input())
if a < 0:
    T[0] = 1
    a = 2**b + a
u2(a,b-1)
for i in range(b):
    print(T[i],end=' ')