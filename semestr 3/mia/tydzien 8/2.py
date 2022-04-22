from math import gcd

x = int(input())

i = 1

while i * i <= x:
    if (not x % i) == gcd(x // i, i): res = i     #i|x and gcd(x/i, i) = 1
    i += 1

print(res, x // res)