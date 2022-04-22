from math import gcd

n = int(input())
a = [int(x) for x in input().split()]

aux = a[0]

for aa in a[1:]: aux = gcd(aux, aa)

print('Alice' if (max(a) // aux - n) % 2 == 1 else 'Bob')