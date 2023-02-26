def zad42(L,P,N,W):
    if N < 1: print(W)
    for i in range(L,P+1): 
        W.append(i)
        zad42(i,P,N-1,W)

zad42(0,6,2,[])
