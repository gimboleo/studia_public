def a(n):
    if n%2 == 1: return -1*n
    else: return n

for i in range(11):
    print(a(i))
print()



def b(n):
    sum = 0
    for i in range(1,n+1):
        if i%2 == 1: sum = sum - 1/i
        else: sum = sum + 1/i
    return sum

for i in range(1,11):
    print(b(i))
print()



def c(n,x):
    sum = 0
    for i in range(1,n+1):
        liczba = 1
        for j in range(i):
            liczba = liczba * x
        liczba = liczba * i
        sum = sum + liczba
    return sum

for i in range(1,11):
    print(c(i,3))        
