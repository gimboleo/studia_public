def krzyzyk(n):
    for i in range(n):
        for j in range(n):
            print(" ",end="")
        for j in range(n):
            print("*",end="")
        print()
    
    for i in range(n):
        for j in range(3*n):
            print("*",end="")
        print()

    for i in range(n):
        for j in range(n):
            print(" ",end="")
        for j in range(n):
            print("*",end="")
        print()
            
    
liczba = int(input("Test: "))
krzyzyk(liczba)