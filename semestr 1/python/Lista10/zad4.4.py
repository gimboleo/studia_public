def zad42(L, P, N, T = None): 
    if T is None: T = [[L] * N] 
    cur = T[-1].copy() 
    for i in reversed(range(N)): 
        if cur[i] < P: 
            cur[i] += 1 
            for j in range(i+1, N): cur[j] = cur[i] 
            T.append(cur) 
            return zad42(L, P, N, T) 
    return T

print(zad42(3,7,3))