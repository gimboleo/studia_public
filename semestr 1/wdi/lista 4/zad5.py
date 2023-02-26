def binarna(n):
    if n<=0: return 0
    return (10 * binarna(n//2)) + n%2

def palindrom2(n):
    bi = binarna(n)
    x = bi
    print(x)
    obrocona = 0
    while x>0:
        cyfra = x%10
        obrocona = 10*obrocona + cyfra
        x = x//10
    print(obrocona)
    if(obrocona == bi): return True
    else: return False

print(palindrom2(51)) 