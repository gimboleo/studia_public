n, w = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]



if w > n:
    print(0)
    exit()

if w == 1:
    print(n)
    exit()



res = 0

a = [a[i + 1] - a[i] for i in range(n - 1)]
b = [b[i + 1] - b[i] for i in range(w - 1)]
arr = b + ['###'] + a
aux = [0] * len(arr)

for i in range(1, len(arr)):
    j = aux[i - 1]
    while j > 0 and arr[i] != arr[j]: j = aux[j - 1]

    if arr[i] == arr[j]:
        j += 1
        aux[i] = j

    if j == len(b): res += 1

print(res)