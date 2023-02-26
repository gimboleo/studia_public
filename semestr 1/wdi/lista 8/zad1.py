def zad1(n):
    if n == 1: return 1
    else: return zad1(n-1) + n

print(zad1(8))

