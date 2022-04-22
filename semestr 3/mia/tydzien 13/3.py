def aux(p0, p1, p2):
    return abs((p2[0] - p1[0]) * (p1[1] - p0[1]) - (p1[0] - p0[0]) * (p2[1] - p1[1])) / (2 * ((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2) ** 0.5)


n = int(input())

vertices = []
res = float('inf')

for i in range(n): vertices.append([int(x) for x in input().split()])

for i in range(n):
    a, b, c = vertices[i], vertices[(i + 1) % n], vertices[(i + 2) % n]
    res = min(res, aux(a, b, c), aux(b, c, a), aux(c, a, b))

print(res)