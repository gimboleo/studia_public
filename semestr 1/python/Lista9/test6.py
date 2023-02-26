import time

def rev2(L):
    wynik = []
    for i in range(len(L)):
        wynik.append(L[-i-1])
    return wynik

for d in range(0, 1000, 3):
    L = list(range(d))

    t0 = time.time()
    rev2(L)
    t  = time.time() - t0
    print(2000*t)