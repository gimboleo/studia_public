n, k = [int(x) for x in input().split()]
string = input()

l = res = 0
beauty = [0, 0]

for lt in string:
    beauty[ord(lt) - 97] += 1
    if min(beauty) > k:
        beauty[ord(string[l]) - 97] -= 1
        l += 1
    else: res += 1

print(res)