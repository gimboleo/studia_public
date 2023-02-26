def gcd(n,m):
    if (m==0): return n
    if (n<m): return gcd(m,n)
    ilenp = n%2 + m%2
    if (ilenp==2):
        return gcd(n-m,m)
    if (ilenp==0):
        return 2*gcd(n/2,m/2)
    if (n%2==0): 
        return gcd(n/2,m)
    else: return gcd(n,m/2)         # m%2 ==0

def nwd(a,b):
    x = 1
    if a<b:
        c = a
        a = b
        b = c
    while(b>0):
        ilenp = a%2 + b%2
        if (ilenp==2):
            a = a-b
        elif (ilenp==0):
            x = x*2
            a = a/2
            b = b/2
        elif (a%2==0): 
            a = a/2
        else: 
            b = b/2         # m%2 ==0
        if a<b:
            c = a
            a = b
            b = c
    return x*a

a,b = 171,348
print(gcd(a,b))
print(nwd(a,b))