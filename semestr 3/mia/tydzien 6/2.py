n = int(input())

after = [[] for i in range(26)]
before = [0 for i in range(26)]
res = True


for i in range(n):
    name = input()

    if i:
        res = res and prev[:len(name)] != name
        if not res: break
        if name[:len(prev)] != prev:
            a, b = next(filter(lambda x: x[0] != x[1], zip(prev, name)))
            after[ord(a) - 97].append(ord(b) - 97)
            before[ord(b) - 97] += 1

    prev = name


if res:
    res = []
    q = []
    l = 0

    for i in range(26):
        if not before[i]: q.append(i)

    while l < len(q):
        aux = q[l]
        l += 1
        res.append(chr(aux + 97))

        for i in after[aux]:
            before[i] -= 1
            if not before[i]: q.append(i)


if res and len(res) == 26: print(''.join(res))
else: print('Impossible')
