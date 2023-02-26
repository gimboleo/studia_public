from wdi import *

def min_cost(T,n):
    temp = Array(n,n)
    temp[0][0] = T[0][0]

    for i in range(1,n):
        temp[i][0] = temp[i-1][0] + T[i][0]
        temp[0][i] = temp[0][i-1] + T[0][i]

    for i in range(1,n):
        for j in range(1,n):
            temp[i][j] = min(temp[i-1][j],temp[i][j-1]) + T[i][j]

    print()
    for i in range(n):
        for j in range(n):
            print(T[i][j],end=' ')
        print()
    print()
    for i in range(n):
        for j in range(n):
            print(temp[i][j],end=' ')
        print()
    print()
    return temp[n-1][n-1]


T = Array(3,3)
T[0][0] = 10; T[0][1] = 9; T[0][2] = 31
T[1][0] = 21; T[1][1] = 7; T[1][2] = 8
T[2][0] = 13; T[2][1] = 14; T[2][2] = 10
n = 3

print(min_cost(T,n))
