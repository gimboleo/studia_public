a, b, n = [int(x) for x in input().split()]


modulo = int(1e9 + 7)
res = 0
s = set()
fib = [1] * (n + 1)


for x in range(2, 1 << 8):
    z = 0
    while x > 1:
        z = z * 10 + (a, b)[x & 1]
        x >>= 1
        s.add(z)


for i in range(1, n + 1):
    fib[i] = fib[i - 1] * i % modulo


for i in range(n + 1):
    if i * a + (n - i) * b in s: res += pow(fib[i] * fib[n - i], modulo - 2, modulo)


print(res * fib[n] % modulo)