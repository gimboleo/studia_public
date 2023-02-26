from turtle import *
from duze_cyfry import *
from random import *

def teleport(x,y):
    penup()
    goto(x,y)
    pendown()

def kwadrat(a,kolor):
    fillcolor(kolor)
    begin_fill()
    for i in range(4):
        fd(a)
        lt(90)
    end_fill()

def cyfra(l,x,y):
    K = choice(kolorki)
    for i in range(5):
        for j in range(5):
            if daj_cyfre(l)[i][j] == '#' and T[i+y][j+x] == 1: return 0
    for i in range(5):
        for j in range(5):
            if daj_cyfre(l)[i][j] == '#': 
                T[i+y][j+x] = 1
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
    '''
    print()
    print(x,y)
    print(x*a,y*(-a))
    for i in range(30):
        print(T[i])
    done()
    '''

def mozaika():
    for i in range(80):
        x = randint(0,25)
        y = randint(0,25) 
        teleport(x*a,y*(-a))
        cyfra(randint(0,9),x,y)

screen = Screen()
screen.setup(500, 500)
screen.setworldcoordinates(0, -15*30, 15*30, 0)
T = [[0 for i in range(30)] for j in range(30)]
a = 15
kolorki = ['green','blue','red','cyan','purple','yellow','orange','brown','pink','gray']
speed('fastest')

'''
teleport(0,0)
kwadrat(a,'black')
'''
tracer(0,0)
mozaika()
update()
done()