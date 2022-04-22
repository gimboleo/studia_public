m, b = [int(x) for x in input().split()]

res = 0

for y in range(b + 1):      #Highest point will always be (0,b)
    x = m * (b - y)
    res = max(res, (x * (x + 1) // 2 * (y + 1)) + (y * (y + 1) // 2 * (x + 1)))    #sum of 0 to x + sum of 0 to y'

print(res)