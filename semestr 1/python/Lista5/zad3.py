from turtle import *
from duze_cyfry import *
from random import randint
colormode(255)

def kwadrat(a,kolor):
    fillcolor(x for x in kolor)
    begin_fill()
    for i in range(4):
        fd(a)
        lt(90)
    end_fill()

def cyfra(l):
    K = [randint(0,255) for k in range(3)]
    for i in range(5):
        for j in daj_cyfre(l)[i]:
            if j == '#': 
                kwadrat(a,K)
                fd(a)
            else:
                penup()
                fd(a)
                pendown()
        penup()
        rt(180)
        fd(5*a)
        lt(90)
        fd(a)
        lt(90)
        pendown()                

def tablica():
    for x in range(15):
        for y in range(10):
            z = randint(0,9)
            cyfra(z)
            penup()
            rt(90)
            fd(a)
            lt(90)
            pendown()
        penup()
        fd(7*a)
        lt(90)
        fd(60*a)
        rt(90)
        pendown()

a = 10

tracer(0,0)
penup()
goto(-500,300)
pendown()
tablica()
update()
done()