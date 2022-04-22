t = int(input())

for i in range(t):
    b, p, f = [int(x) for x in input().split()]  
    h, c = [int(x) for x in input().split()] 
    b = b // 2 

    if h > c: (PR, pr, M, m) = (h, c, p, f)
    else: (PR, pr, M, m) = (c, h, f, p)
    
    if b >= M:
        res = M * PR
        b -= M
        if (b >= m): res += m * pr
        else: res += b * pr
    else: res = b * PR

    print(res)