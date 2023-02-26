def szachownica(n,k):

    x = 0
    
    for a in range(2*n):
        for b in range(k):
            if x%2==0:
                for c in range(n):
                    for d in range(k):
                        print(" ",end="")
                    for d in range(k):
                        print("#",end="")
            else:
                for c in range(n):
                    for d in range(k):
                        print("#",end="")
                    for d in range(k):
                        print(" ",end="")
            print()
        x = x+1
        
print("Podaj n i k: ")        
a = int(input())
b = int(input())
szachownica(a,b)