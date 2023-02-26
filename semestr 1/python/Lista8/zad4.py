from random import randint
import numpy as np
from turtle import *

def kwadrat(a,k):
    fillcolor(k)
    begin_fill()
    for i in range(4):
        fd(a)
        lt(90)
    end_fill()

def mapa():
    T = np.zeros((100,100))

    for i in range(3700):
        y = randint(0,99)
        x = randint(0,99)
        T[y,x] = 1

    for i in range(100000):
        y = randint(0,99)
        x = randint(0,99)
        srednia = 3*T[y,x]
        z = 3

        if y != 0:
            srednia = srednia + 2*T[y-1,x]
            z = z+2
            if x != 0: 
                srednia = srednia + T[y-1,x-1]
                z = z+1
            if x !=  99: 
                srednia = srednia + T[y-1,x+1]
                z = z+1

        if x != 0: 
            srednia = srednia + 2*T[y,x-1]
            z = z+2
        if x !=  99: 
            srednia = srednia + 2*T[y,x+1]
            z = z+2

        if y != 99:
            srednia = srednia + 2*T[y+1,x]
            z = z+2
            if x != 0: 
                srednia = srednia + T[y+1,x-1]
                z = z+1
            if x !=  99: 
                srednia = srednia + T[y+1,x+1]
                z = z+1

        srednia = srednia/z
        T[y,x] = srednia

    kolory = ['dark green', 'lime', 'yellow', 'orange', 'red', 'maroon']

    for i in range(100):
        for j in range(100):
            for k in range(6):
                kolor = kolory[k]
                if T[i][j] < (k+1) * 0.15: break
            kwadrat(5,kolor)
            fd(5)
        goto(pos()+(-5*100,-5))

tracer(0,0)
goto(-200,200)
speed('fastest')
penup()
mapa()
done()