n = int(input())
p = [int(x) for x in input().split()]
c = [int(x) for x in input().split()]

counter = 1
for i in range(1, n):
    if c[i] != c[p[i - 1] - 1]: counter += 1

print(counter)