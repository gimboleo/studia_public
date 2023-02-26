from turtle import *
from random import choice

def obrot(x):
    if x%2 == 0: rt(90)
    else: lt(90)

def kwadraciki(n,m):
    if n == 1:
        for i in range(4):
            fd(20*m)
            obrot(n)
    else:
        for i in range(4):      
            fd(20*m/3)
            kwadraciki(n-1,m/3)
            fd(20*m*2/3)
            obrot(n)

a = 4
ln = 18

penup()
if a%2 == 0: goto(-10*ln,10*ln)
else: goto(-10*ln,-10*ln)
pendown()

speed('fastest')
tracer(0, 0)
kwadraciki(a,ln)
update()
done()