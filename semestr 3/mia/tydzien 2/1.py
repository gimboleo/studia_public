n = int(input())
ts = set(int(x) for x in input().split())

res = False

for ball in ts:
    if ball + 1 in ts and ball - 1 in ts:
        res = True
        break

print("YES") if res else print("NO")