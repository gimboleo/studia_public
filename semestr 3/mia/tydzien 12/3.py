import sys
input = sys.stdin.buffer.readline   #This Little Maneuver's Gonna Save Us 51 Years



ceil = 10 ** 18
res = []



for _ in range(int(input())):
    n = int(input())

    p = [ceil] * 3
    p0 = [0] * 3
    prev = ceil


    for _ in range(n):
        a, b = [int(x) for x in input().split()]

        for i in range(3):
            for j in range(3):
                if not prev + i == a + j: p[j] = min(p[j], p0[i] + b * j)
        
        prev = a

        for i in range(3):
            p0[i] = p[i]
            p[i] = ceil
    
    res.append(min(p0))



print(*res, sep = '\n')