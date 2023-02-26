from turtle import *
import random
import sys
from copy import deepcopy

def kwadrat(x,y,kolor):
    fillcolor(kolor)
    penup()
    goto(-100 + x*15, y*15)
    pendown()
    begin_fill()
    for i in range(4):
        fd(15)
        rt(90)
    end_fill()

def rysuj_plansze(tab,X,Y):
    clear()
    for y in range(Y):
        for x in range(X):
            if tab[y][x][0] == '.':
                kolor = 'white'
            elif tab[y][x][0] == 'p':
                kolor = (0.2 * tab[y][x][1], 0 , 0)
            elif tab[y][x][0] == 'k':
                kolor = (0 , 0.2 * tab[y][x][1] , 0)
            elif tab[y][x][0] == 'n':
                kolor = (0 , 0 , 0.2 * tab[y][x][1])
            kwadrat(x, y, kolor)
    update()

def losowy_sasiad(x,y,X,Y):
    if x > 0: left = 1
    else: left = 0
    if x < X: right = 1
    else: right = 0
    if y > 0: up = 1
    else: up = 0
    if y < Y: down = 1
    else: down = 0
    s = list()
    if left: s.append((x-1,y))
    if right: s.append((x+1,y))
    if up: s.append((x,y-1))
    if down: s.append((x,y+1))
    return random.choice(s)

txt1 = '''
...kkkkkkkkkkkk.......
......................
......................
......................
..nnnn................
..nnnn................
..n...................
......................
.........kkkkkkkkkkk..
......................
......................
......................
......................
.........ppppp........
......................
'''

txt2 = '''
...kkkkkkkkkkkk.......
......................
......................
......................
......................
......................
......................
......................
.........kkkkkkkkkkk..
......................
......................
......................
......................
......................
......................
'''

txt3 = '''
pnkpnk
k....p
n....n
p....k
k....p
pknpkn
'''

txt = txt3

temp = [wiersz for wiersz in txt.split()]
temp.reverse()

Y = len(temp)
X = len(temp[0])

tab = list()

for i in temp:
    temp1 = list(i)
    tab.append(temp1)

for y in range(Y):
    for x in range(X):
        if tab[y][x] != '.':
            tab[y][x] = [tab[y][x],random.randint(1,5)]
        else: tab[y][x] = [tab[y][x],0]

tracer(0,0) 

while True:
    rysuj_plansze(tab,X,Y)
    nowa = deepcopy(tab)
    for y in range(Y):
        for x in range(X):
            if tab[y][x][0] != '.':
                sasiad = losowy_sasiad(x,y,X-1,Y-1)
                x1 = sasiad[0]
                y1 = sasiad[1]
                if tab[y1][x1][0] == '.' and tab[y][x][1] > 1: nowa[y1][x1] = [tab[y][x][0],tab[y][x][1]-1]
                elif tab[y1][x1][0] != '.' and tab[y1][x1][0] != tab[y][x][0]:
                    if (tab[y][x][0] == 'p' and tab[y1][x1][0] == 'k') or (tab[y][x][0] == 'k' and tab[y1][x1][0] == 'n') or (tab[y][x][0] == 'n' and tab[y1][x1][0] == 'p'):
                        if nowa[y][x][1] < 5: nowa[y][x][1] += 1
                        nowa[y1][x1][1] -= 1
                        if nowa[y1][x1][1] == 0: nowa[y1][x1][0] = '.'
                    else:
                        if nowa[y1][x1][1] < 5: nowa[y1][x1][1] += 1
                        nowa[y][x][1] -= 1
                        if nowa[y][x][1] == 0: nowa[y][x][0] ='.'
    tab = deepcopy(nowa)




