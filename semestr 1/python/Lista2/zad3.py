def kolko(r):
    import math
    
    for i in range(2*r+1):
        for j in range(2*r+1):
            odleglosc = math.sqrt((i-r)**2+(j-r)**2)
            if odleglosc < r+0.5:
                print("*",end="")
            else:
                print(" ",end="")
        print()
            
def balwan(r):
    import math
    
    for i in range(2*r+1):
        for k in range(4): print(" ",end="")
        for j in range(2*r+1):
            odleglosc = math.sqrt((i-r)**2+(j-r)**2)
            if odleglosc < r+0.5:
                print("*",end="")
            else:
                print(" ",end="")
        print()
    
    r=r+1
    
    for i in range(2*r+1):
        for k in range(3): print(" ",end="")
        for j in range(2*r+1):
            odleglosc = math.sqrt((i-r)**2+(j-r)**2)
            if odleglosc < r+0.5:
                print("*",end="")
            else:
                print(" ",end="")
        print()
    
    r=r+3
    
    for i in range(2*r+1):
        for j in range(2*r+1):
            odleglosc = math.sqrt((i-r)**2+(j-r)**2)
            if odleglosc < r+0.5:
                print("*",end="")
            else:
                print(" ",end="")
        print()

x = int(input("Test: "))
y = int(x/2)
kolko(y)
for i in range(5): print()
balwan(y)
