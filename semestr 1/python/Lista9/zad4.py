import sys
import random
import time
import matplotlib.pyplot as plt

sys.setrecursionlimit(10000)
        
def rev1(L):
    if len(L) == 0:
        return []
    return rev1(L[1:]) + [L[0]]

def rev2(L):
    wynik = []
    for i in range(len(L)):
        wynik.append(L[-i-1])
    return wynik

dane1 = []
dane2 = []
K = 5

for d in range(0, 1000, 3):
    L = list(range(d))
    
    ts = []
    for i in range(K):
        t0 = time.perf_counter_ns()
        rev1(L)
        t  = time.perf_counter_ns() - t0
        ts.append(t)
        
    dane1.append( (d, min(ts)) )

    ts = []
    for i in range(K):
        t0 = time.perf_counter_ns()
        rev2(L)
        t  = time.perf_counter_ns() - t0
        ts.append(20*t)
    dane2.append( (d, min(ts)))
    
xs1 = [ d[0] for d in dane1]
ys1 = [ d[1] for d in dane1]

xs2, ys2 = zip(*dane2)    

plt.plot(xs1, ys1, color='blue')
plt.plot(xs2, ys2, color='red')

plt.show()