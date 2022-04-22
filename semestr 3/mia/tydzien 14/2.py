n = int(input())
a = sorted([int(x) for x in input().split()])
m = int(input())
b = sorted([int(x) for x in input().split()])

res = 0
i = 0
j = 0

while i < n and j < m:
    if abs(a[i] - b[j]) < 2:
        res += 1
        i += 1
        j += 1
    elif a[i] < b[j]: i += 1
    else: j += 1

print(res)