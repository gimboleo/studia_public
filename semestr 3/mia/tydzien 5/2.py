n, m, k = [int(x) for x in input().split()]
c = [int(x) for x in input().split()]


socks = [[] for i in range(n)]
done = [False for i in range(n)]
res = 0


for i in range(m):
    l, r = [int(x) for x in input().split()]
    socks[l - 1].append(r - 1)
    socks[r - 1].append(l - 1)


for i in range(n):
    if done[i]: continue
    done[i] = True

    s = [i]
    q = {}

    while s:
        x = s.pop()
        if c[x] not in q: q[c[x]] = 0
        q[c[x]] += 1
        for j in socks[x]:
            if done[j]: continue
            done[j] = True
            s.append(j)

    S = 0
    M = 0

    for x in q:
        M = max(M, q[x])
        S += q[x]

    res += S - M

print(res)