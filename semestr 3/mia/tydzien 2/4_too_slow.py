n, u, r = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
k = [int(x) for x in input().split()]
p = [int(x) for x in input().split()]


res = 0
a2 = a.copy()


def f(depth, op):
    global res, a, b, k, p

    if not (u - depth) % 2:
        aux = 0
        for i in range(n): aux += a[i] * k[i]
        res = max(res, aux)

    if depth == u: return

    temp = a.copy()

    if op:
        for i in range(n): a[i] = temp[p[i] - 1] + r
        a3 = a.copy()
        f(depth + 1, 0)
        a = a3.copy()
        f(depth + 1, 1)
    else:
        for i in range(n): a[i] = temp[i] ^ b[i]
        f(depth + 1, 1)


f(0, 0)
a = a2.copy()
f(0, 1)
print(res)