def pierwsza(n):
    if n>1:
        for i in range(2,(n//2)+1): #pierwiastek zamiast n//2
            if (n%i == 0):
                return False
        return True
    return False

x = 0   
for i in range(1,100000+1):
    if pierwsza(i) and "777" in str(i):
        x = x+1
        print(i)
print("Ilość: ",x)        