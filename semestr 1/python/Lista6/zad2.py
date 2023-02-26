from itertools import combinations

def pary(L):
    P = []
    for i in combinations(L,2): P.append(i)
    return P

def odwrotne(P):
    for i in range(len(P)):
        if P[i][0] == P[i][1][::-1]: print(P[i])

def importlisty():
    plik = open(r'C:\Users\kubak\Desktop\Python\Lista6\slowa.txt','r',encoding='utf-8')
    L = plik.read().splitlines()
    return L

odwrotne(pary(importlisty()))