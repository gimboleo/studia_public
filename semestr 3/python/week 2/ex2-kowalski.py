#This function works for all positive real numbers, will return -1 for negative ones
def square_root(n):
    s, i = 0, 0

    #Sum from i = 1 to k of (2i - 1) = k^2
    #Sum from i = 1 to floor(k) of (2i - 1) <= k^2
    #Sum from i = 1 to floor(k) + 1 of (2i - 1) > k^2
    #We're searching for the smallest partial sum that is bigger than our entry number (floor(k) + 1)
    #The previous one is our answer (floor(k))
    while s <= n:
        i += 1
        s += (2 * i - 1)
    return i - 1


for i in range(36 * 4 + 1): print(i / 4, square_root(i / 4))