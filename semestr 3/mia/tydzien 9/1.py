n, k = [int(x) for x in input().split()]
t = input()

i = 1

while t[i:] != t[:-i]: i += 1
print(t[:i] * k + t[i:])