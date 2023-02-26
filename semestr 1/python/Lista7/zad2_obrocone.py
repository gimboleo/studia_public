from turtle import *
from random import shuffle
colormode(255)

def kwadrat(a,kolor):
    fillcolor(kolor)
    begin_fill()
    for i in range(4):
        fd(a)
        lt(90)
    end_fill()


def rysunek():
    with open(r'C:\Users\kubak\Desktop\Python\Lista7\rysunek.txt') as plik:         #w test.txt: LG: red; PG: green; LD: blue
        K = [linijka.split() for linijka in plik]

        R = []
        for i in range(len(K)):
            for j in range(len(K[0])):
                R.append((i,j))
        shuffle(R)
        #print(R)
    
    setworldcoordinates(-600,-600,0,0)
    tracer(0,0)
    speed('fastest')
    penup()

    for i in range(len(R)):
        y = R[i][0]
        x = R[i][1]
        goto(-y*10,-x*10)
        kwadrat(10,eval(K[y][x]))
        if i%20 ==0: update()

    update()
    done()


rysunek()