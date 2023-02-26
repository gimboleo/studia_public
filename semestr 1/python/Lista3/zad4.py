from turtle import *

def gwiazdka(a):
    for i in range(10):
        fd(a)
        bk(a)
        rt(36)

def duzagwiazdka(b):
    for i in range(10):
        fd(b)
        gwiazdka(b/10)
        bk(b)
        rt(36)

speed('fastest')
duzagwiazdka(150)
done()