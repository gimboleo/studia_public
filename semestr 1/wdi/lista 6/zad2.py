from wdi import *

def zad2(T,l):
    for i in range(l-1):
        m = i
        for j in range(i+1,l): 
            if T[j] < T[m]:            #dominująca
                m = j
        temp = T[i]
        T[i] = T[m]
        T[m] = temp
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
zad2(T,l)