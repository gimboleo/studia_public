from wdi import *

def zad4():
    n = int(input("n: "))
    k = int(input("k: "))
    A = Array(k)
    L = Array(k)
    for i in range(k):
        print("A[",i,"]: ",sep="",end="")
        A[i] = int(input())
    print()

    for i in range(k):
        x = n
        while(x%A[i] == 0):
            x = x/A[i]
            L[i] = L[i] + 1

    p = 0
    for i in range(k):
        if L[i] > p: p = L[i]
    print("p:",p)

    for i in range(k):
        if L[i] == p: print(A[i])

zad4()