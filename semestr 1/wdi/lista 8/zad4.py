def zad4(a,l,p):
    if l == p: return a[l]
    elif p-1 == l:
        if a[l] < a[p]: return a[l]
        else: return a[p]
    else:
        m1 = zad4(a,l,(l+p)//2)
        m2 = zad4(a,(l+p)//2+1,p)
        if m1 < m2: return m1
        else: return m2

a = [1,5,8,4,9]
print(zad4(a,0,4))
