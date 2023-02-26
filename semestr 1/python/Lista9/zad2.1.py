from turtle import *

def zad2(x,l):
    if not l:
        fd(x)
        return 0
    x = x//5
    zad2(x*2,l-1)
    lt(90)
    zad2(x,l-1)
    for i in range(2):
        rt(90)
        zad2(x,l-1)
    lt(90)
    zad2(x*2,l-1)


speed('fastest')
tracer(0,0)
screensize(3000,3000)
for i in range(4):
    zad2(1200,4)
    rt(90)
update()
done()