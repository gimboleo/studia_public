from wdi import *

def T(n,m):
    if m == 0: return n
    if n == 0: return m
    return T(n-1,m) + 2*T(n,m-1)

def T1(n,m):
    nowy = Array(n + m+1)
    for i in range(0, n+m):
        if i > n:
            maxc = n
        else:
            maxc = i
        j = maxc
        while j > 0:
            nowy[j] = nowy[j-1]+2*nowy[j]
            j = j-1
        if i <= m:
            nowy[0]=i+1
        if i <= n: 
            nowy[i+1] = i+1
        #for k in range(n+m+1):
            #print(nowy[k],end=' ')
        #print()
    #print()
    print(nowy[n])

a,b=9,11
print(T(a,b))
T1(a,b)