def zad41(L):
    temp = [[]]
    for i in L:
        temp += [sub + [i] for sub in temp]
    return temp

print(zad41([1,2,3]))
