n, r = [int(x) for x in input().split()]
xs = [int(x) for x in input().split()]
res = []


for x in xs:
    y = r

    for px, py in zip(xs, res):
        if abs(x - px) <= 2 * r: y = max(y, py + (4 * r ** 2 - (x - px) ** 2) ** 0.5)
    
    res.append(y)


print(*res)