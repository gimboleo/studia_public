n = int(input())
aa = [int(x) for x in input().split()]

pr = [[] for i in range(10**5 + 1)]
good_sequence = [0 for i in range(10**5 + 1)]
maximum = [0 for i in range(10**5 + 1)]
res = 0

for i in range(2, aa[n - 1] + 1):
    for j in range(i, aa[n - 1] + 1, i): pr[j].append(i)

for i in range(n):
    a = aa[i]

    for j in range(len(pr[a])): good_sequence[i] = max(good_sequence[i], maximum[pr[a][j]] + 1)

    for j in range(len(pr[a])): maximum[pr[a][j]] = good_sequence[i]

    res = max(res, good_sequence[i])

print(max(res, 1))