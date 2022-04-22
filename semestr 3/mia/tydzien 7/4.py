n = int(input())


res = 1
modulo = int(1e9 + 7)
r = 2 * n + 1               #range
wish = [0] * r
rev = [[] for i in range(r)]
count = [0] * r


for i in range(n):
    curr, next = [int(x) for x in input().split()]
    wish[curr] = next

    if curr != next:
        rev[next].append(curr)
        count[next] += 1


for d in range(1, r):
    if not wish[d]:
        x = 0
        aux = [d]
        
        while aux:
            x += 1
            y = aux.pop()
            count[y] = -1
            aux += rev[y]

        res = (res * x) % modulo


for d in range(1, r):
    if not count[d]:
        x = wish[d]
        
        while count[x] == 1:
            count[x] = -1
            x = wish[x]

        count[x] -= 1


for d in range(1, r):
    if count[d] == 1:
        res = (res * 2) % modulo

        while count[d]:
            count[d] = 0
            d = wish[d]


print(res)