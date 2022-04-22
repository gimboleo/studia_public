t = int(input())


for i in range(t):
    n, x, y = [int(x) for x in input().split()]

    d = y - x

    for i in range(n - 1, 0, -1):
        if not d % i:
            d //= i
            aux = min(n - (i + 1), (x - 1) // d)
            print(*map(str, [x - aux * d + j * d for j in range(n)]))
            break