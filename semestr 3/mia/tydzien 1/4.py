from sys import exit as e
from math import ceil

limit = 10 ** 5

n, r = [int(x) for x in input().split()]
ls = [int(x) for x in input().split()]
ts = [int(x) for x in input().split()]

for i in range(n):
    if ls[i] > ts[i]:
        print("-1")
        e()

timer = 0
aux_timer = 0
speed_mode = 0
res = 0
res2 = []

for i in range(n):
    if i: timer += ls[i - 1]
    if speed_mode > ls[i]: speed_mode -= ls[i]
    elif speed_mode + 2 * (ls[i] - speed_mode) <= ts[i]: speed_mode = 0
    else:
        speed_needed = speed_mode + 2 * (ls[i] - speed_mode) - ts[i]
        jj = speed_needed // r
        res += jj
        for j in range(jj):
            if len(res2) >= limit: break
            res2.append((timer + j * r + speed_mode) * 2 - aux_timer * r)
            aux_timer += 1
        if speed_needed % r:
            res += 1
            if len(res2) < limit:
                res2.append((timer + ls[i] - speed_needed % r) * 2 - aux_timer * r)
                aux_timer += 1
        speed_mode = (r - (speed_needed % r)) % r

print(res)
if res <= limit: print(*res2)