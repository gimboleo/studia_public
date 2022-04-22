def aux(mid):
    s = mid

    M = mid - 1
    MR = min(right, M)
    ML = min(left, M)

    s += mid * MR - ((MR / 2) * (MR + 1))
    s += max(0, right - MR)
    s += mid * ML - ((ML / 2) * (ML + 1))
    s += max(0, left - ML)
    
    return 1 if s <= m else 0


n, m, k = [int(x) for x in input().split()]
res = 0
l = 1
r = m


while (l <= r):
    mid = (l + r) // 2
    right = n - k
    left = k - 1

    if (aux(mid) == 1):
        res = mid
        l = mid + 1
    else: r = mid - 1

print(res)