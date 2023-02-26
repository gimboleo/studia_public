from itertools import combinations

def pary(L):
    for i in combinations(L,2):
        odwrotne(i)

def odwrotne(P):
    if P[0] == P[1][::-1]: print(P)

def importlisty():
    plik = open(r'C:\Users\kubak\Desktop\Python\Lista6\slowa.txt','r',encoding='utf-8')
    L = plik.read().splitlines()
    return L

odwrotne(pary(importlisty()))