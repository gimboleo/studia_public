def koperta(n):
    
    for i in range(2*n+1):
        print("*",end="")
    print()
    
    for i in range(n-1):
        print("*",end="")
        for j in range(i): print(" ",end="")
        print("*",end="")
        for j in range((2*n)-3-(2*i)): print(" ",end="")
        print("*",end="")
        for j in range(i): print(" ",end="")
        print("*")
        
    print("*",end="")
    for i in range(n-1): print(" ",end="")
    print("*",end="")
    for i in range(n-1): print(" ",end="")
    print("*")
    
    for i in range(n-2,-1,-1):
        print("*",end="")
        for j in range(i): print(" ",end="")
        print("*",end="")
        for j in range((2*n)-3-(2*i)): print(" ",end="")
        print("*",end="")
        for j in range(i): print(" ",end="")
        print("*")
        
    for i in range(2*n+1):
        print("*",end="")
    print()
        
x = int(input("Podaj n: ")) 
koperta(x)