from wdi import *

def nwd(a,b):
    if a<b:
        c = a
        a = b
        b = c
    while(b>0):
        a = a%b
        if a<b:
            c = a
            a = b
            b = c
    return a

def nwd2():
    n = int(input("n: "))
    T = Array(n)
    for i in range(n):
        print("T[",i,"]: ",sep="",end="")
        T[i] = int(input())

    x = nwd(T[0],T[1])
    for i in range(2,n):
        x = nwd(x,T[i])
    print(x)

nwd2()