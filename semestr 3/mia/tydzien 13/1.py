r, d = [int(x) for x in input().split()]

res = 0

for _ in range(int(input())):
    x, y, rr = [int(x) for x in input().split()]
    aux = (x ** 2 + y ** 2) ** 0.5
    if aux - rr >= r - d and aux + rr <= r: res += 1

print(res)