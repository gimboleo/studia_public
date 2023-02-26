def zad2(n):
    if n == 1: return 0
    elif n%2 == 0: return zad2(n/2) + 1
    else: return zad2((n+1)/2) + 1

print(zad2(16))