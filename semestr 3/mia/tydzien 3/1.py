from bisect import bisect_left

n = int(input())
a = [int(x) for x in input().split()]
m = int(input())
q = [int(x) for x in input().split()]

aa = [0 for i in range(n + 1)]
for i in range(n): aa[i + 1] = aa[i] + a[i]

for i in range(m):
    print(bisect_left(aa, q[i]))