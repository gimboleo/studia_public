vs = [0]
ds = [0]
ps = [0]
total = 0
res = []


n = int(input())


for i in range(1, n + 1): 
    v, d, p = [int(x) for x in input().split()]
    vs.append(v)
    ds.append(d)
    ps.append(p)


for i in range(1, n + 1):
    if ps[i] < 0: continue
    
    total += 1
    res.append(i)
    hall_screams = 0
    scream = vs[i]

    for j in range(i + 1, n + 1):
        calm_flag = 0

        if ps[j] >= 0:
            calm_flag = 1

            if scream > 0: 
                ps[j] -= scream
                scream -= 1

        if ps[j] >= 0: ps[j] -= hall_screams
        if ps[j] < 0 and calm_flag: hall_screams += ds[j]

print(total)
print(*res)