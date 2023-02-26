from turtle import *

def zad2(x):
    if not x: return 0
    pencolor(kolory[x%len(kolory)])
    fd(x)
    lt(91)
    zad2(x-1)

speed('fastest')
tracer(0,0)
pensize(2)
bgcolor("black")
kolory = ["red","green","yellow","purple"]
screensize(3000,3000)
zad2(600)
update()
done()