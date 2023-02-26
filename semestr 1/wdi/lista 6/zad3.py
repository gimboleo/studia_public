from wdi import *

def zad3(T,l):
    for i in range(l-1,0,-1):
        flag = 0
        for j in range(i):
            if T[j] > T[j+1]:                      #dominująca
                T[j],T[j+1] = T[j+1],T[j]
                flag = 1
        if not flag: break        
    for i in range(l):
        print(T[i])

T = Array(10)
T[0] = 4
T[1] = 7
T[2] = 3
T[3] = 1
T[4] = 2
T[5] = 6
T[6] = 5
T[7] = 0
T[8] = 8
T[9] = 9
l = 10 #len(T)
zad3(T,l)