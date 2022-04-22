l, r, x, y, k = [int(x) for x in input().split()]

l += k - 1
l //= k
r //= k

print('NO' if l > r or l > y or x > r else 'YES')