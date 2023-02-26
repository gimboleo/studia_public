from turtle import *
from random import randint
colormode(255)

def teleport(x,y):
    penup()
    goto(x,y)
    pendown()

def kwadrat(a,kolor):
    fillcolor(x for x in kolor)
    print(kolor)
    begin_fill()
    for i in range(4):
        fd(a)
        lt(90)
    end_fill()

def tablica(a,x,y):
    for i in range(x):
        for j in range(y):
            T = [randint(0,255) for k in range(3)]
            teleport(i*a,j*a)
            kwadrat(a,T)

speed('fastest')
tracer(0, 0)
tablica(20,15,15)
update()
done()