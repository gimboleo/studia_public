t = int(input())

for i in range(t):
    n = int(input())
    ds = input()

    sort = "".join(sorted(ds))
    res = ["0" for i in range(n)]
    f1 = n-1
    f2 = 0

    for i in range(n - 1, -1, -1):
        if ds[i] == sort[f1]:
            res[i] = "2"
            f1 -= 1
    f1 += 1

    for i in range(n):
        if res[i] == "0" and ds[i] == sort[f2]:
            res[i] = "1"
            f2 += 1
    
    print("".join(res)) if f1 == f2 else print("-")