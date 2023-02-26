import math

def pierwsza(n):
    if n>1:
        for i in range(2,int(math.sqrt(n)+1)): 
            if (n%i == 0):
                return False
        return True
    return False

def dzielnikipierwsze(n):
    T = []
    for i in range(1,int(math.sqrt(n)+1)):
        if n%i == 0:
            if n/i == i: T.append(i)
            else:
                T.append(i)
                T.append(int(n/i))
        i = i+1
    
    print(T)

    for i in T:
        if pierwsza(i): print(i)

dzielnikipierwsze(1040)
