def zad41(L):
    if not L: return [[]]
    temp = zad41(L[1:])
    return temp + [[L[0]] + n for n in temp]

print(zad41([1,2,3]))
