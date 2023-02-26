from wdi import *

def init():
    for i in range(n):
        b[i] = -1
    
def isf(x,y):
    for i in range(x):
        if b[i]-i == y-x or b[i]+i == y+x or b[i] == y: return 0
    return 1

def poprawne(a,n):
    for i in range(n):
        x = i
        y = a[i]
        for j in range(x):
            if b[j]-j == y-x or b[j]+j == y+x or b[j] == y: 
                return 0
    return 1

def hetmany(n,k,a):
    if k == n: return poprawne(a,n)
    for i in range(n):
        a[k] = i
        if (hetmany(n,k+1,a)): return 1
    return 0

def drawresult():
    print()
    for i in range(n):
        print(b[i],end=' ')
    print()
    print()
    for i in range(n):
        for j in range(n):
            if b[j] == i: print("x",end=' ')
            else: print("o",end=' ')
        print()


n=6 # rozmiar szachownicy
b=Array(n)
init()
if hetmany(n,0,b):
    drawresult()
else: print("brak rozwiazania")

#Ten algorytm sprawdza duzo wiecej hetmanow, poniewaz nie odrzuca czesciowych ustawien ktore sa zle, sprawdza dopiero cale