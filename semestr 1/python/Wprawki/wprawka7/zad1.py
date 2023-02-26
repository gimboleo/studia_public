def powerset(L):
    if L == []: return [[]]

    x = powerset(L[1:])

    return x + [[L[0]] + y for y in x]

print(powerset([1,2,3]))