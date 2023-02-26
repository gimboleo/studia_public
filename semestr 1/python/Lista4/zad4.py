def pierwsza(n):
    W = [0] * 2 + [1] * (n-1)
    for i in range(2,n+1):
        if W[i]:
            for j in range(i*2,n+1,i):
                W[j] = 0  
    T = []
    for i in range(n+1):
        if W[i]: T.append(i)
    return T

print(pierwsza(30))

def palindromy(a,b):
    for i in pierwsza(b):
        j = str(i)
        if i >= a and j == j[::-1]:
            print(i)

palindromy(2,1000)
            