t = int(input())

for i in range(t):
    k = int(input())
    ks = input()
    res = 0
    A = -1

    for j in range(k):
         if ks[j] == "P" and A > -1 : res = max(res, j - A)
         elif ks[j] == "A": A = j

    print(res)