def pot(a, b, x=0):
    if not b:
        return 1
    if b%2:
        x = x + 2
        print(x)
        return a*pot(a*a,b//2,x)
    x = x + 1
    print(x)
    return pot(a*a,b/2,x)

pot(6,7)
print()
pot(6,1024)