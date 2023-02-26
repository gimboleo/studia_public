def silnia(n):
    a = 1
    for i in range(1,n+1):
        a = a*i
    return a
    
liczba = int(input("Test: "))
print (silnia(liczba))
print()

for i in range(101):
    print(i,"! ma ",len(str(silnia(i))),sep="",end=" ")
    j = len(str(silnia(i)))
    if j == 1:
        print("cyfrę")
    elif j>=10 and j<=19:
        print("cyfr")
    elif j%10>=2 and j%10<=4:
        print("cyfry")
    else:
        print("cyfr")