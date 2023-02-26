from turtle import *
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
    
    screen = Screen()
    screen.setup(800, 800)
    tracer(0,0)
    speed('fastest')
    penup()
    goto(-10*len(K[0])/2,375)

    for i in range(len(K)):
        for j in range(len(K[i])):
            kwadrat(10,eval(K[i][j]))
            goto(pos() + (10,0))
        goto(pos() - (10*len(K[i]),10))
    
    update()
    done()

rysunek()