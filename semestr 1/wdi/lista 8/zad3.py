def zad3(n):
    if n == 1: return 1
    elif n%2 == 0: return 2*zad3(n/2) + 1
    else: return zad3((n-1)/2) + zad3((n+1)/2) + 1

print(zad3(16))