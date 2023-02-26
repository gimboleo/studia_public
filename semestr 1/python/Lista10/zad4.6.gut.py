def zad41(T): 
    if len(T) == 0: return set([0])
    return set([T[0] + suma for suma in list(zad41(T[1:]))]).union(zad41(T[1:]))
  
T = [1, 2, 3, 100] 
print(zad41(T))

def zad42(L, P, N): 
    if not N: return [[]]
    if N == 1: return [[i] for i in range(L,P+1)]

    return [[i] + s for i in range(L,P+1) for s in zad42(i,P,N-1)]


print(zad42(3,7,3))