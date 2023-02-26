from turtle import *
from math import sqrt
from random import randint
from random import random
from random import choice
from time import sleep

def trojkat(a,kolor):
    fillcolor(kolor)
    begin_fill()
    T = list()
    for i in range(3):
        T.append(pos())
        fd(a)
        lt(120)
    end_fill()
    print(T)
    print (T[1][1])
    return T

def wtrojkacie(T,xp,yp):
    x1 = T[0][0]+5
    y1 = T[0][1]+5
    x2 = T[1][0]-5
    y2 = T[1][1]-5
    x3 = T[2][0]-5
    y3 = T[2][1]
    c1 = (x2-x1)*(yp-y1)-(y2-y1)*(xp-x1)
    c2 = (x3-x2)*(yp-y2)-(y3-y2)*(xp-x2)
    c3 = (x1-x3)*(yp-y3)-(y1-y3)*(xp-x3)
    if (c1<0 and c2<0 and c3<0) or (c1>0 and c2>0 and c3>0): return True
    else: return False

speed('fastest')
tracer(0,0)
bgcolor('navy')

penup()
goto(-500,-270)
fillcolor('white')
begin_fill()
fd(1000)
rt(90)
fd(300)
rt(90)
fd(1000)
rt(90)
fd(300)
end_fill()

goto(0,0)
rt(90)

penup()
rt(90)
fd(300)
lt(90)
pendown()

fillcolor('brown')
begin_fill()
for i in range(4):
    fd(50)
    lt(90)
end_fill()

penup()
lt(90)
fd(50)
rt(90)
bk(150)
pendown()

T1 = trojkat(350,'dark green')

penup()
fd(25)
lt(90)
fd(sqrt(3)*350/2*1/3)
rt(90)
pendown()

T2 = trojkat(300,'forest green')

penup()
fd(25)
lt(90)
fd(sqrt(3)*300/2*1/3)
rt(90)
pendown()

T3 = trojkat(250,'lime green')

bombki = Turtle()

wspolrzedne = list() 
for i in range(40):
    x = randint(-150,200)
    y = randint(-250,154)
    if wtrojkacie(T1,x,y) or wtrojkacie(T2,x,y) or wtrojkacie(T3,x,y):
        wspolrzedne.append((x,y))

gwiazdka = ['gold','yellow']

while True:        
    bombki.penup()
    bombki.goto(25,175)
    bombki.pendown()
    bombki.fillcolor(choice(gwiazdka))
    bombki.begin_fill()
    for i in range(5):
        bombki.fd(20)
        bombki.rt(120)
        bombki.fd(20)
        bombki.rt(72-120)
    bombki.end_fill()
    for i in wspolrzedne:
        x = i[0]
        y = i[1]
        bombki.penup()
        bombki.goto(x,y)
        bombki.pendown()
        bombki.fillcolor(random(),random(),random())
        bombki.begin_fill()
        bombki.circle(10)
        bombki.end_fill()
    update()
    sleep(1)
    bombki.clear()

done()