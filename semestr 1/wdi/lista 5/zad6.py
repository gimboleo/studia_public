def fibonacci(n,p): 
    f1 = 1
    f2 = 1
    for i in range(3,n+1):
        f1,f2 = f2,(f1 + f2) % p 
    return f2

print(fibonacci(6,5))