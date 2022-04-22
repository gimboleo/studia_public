n, m = [int(x) for x in input().split()]

res = [0] * n
next = [i + 1 for i in range(n + 1)]

for i in range(m):
    l, r, x = [int(x) for x in input().split()]
    j = l

    while j <= r:
        if not res[j - 1] and j != x: res[j - 1] = x
        aux = next[j]
        next[j] = x if j < x else r + 1
        j = aux

print(*res)