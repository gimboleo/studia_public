from turtle import *

def obrot(x):
    if x%2 == 0: rt(90)
    else: lt(90)

def kwadraciki(n,m,k=0):
    if n == 0: return 1

    fillcolor(kolory[k%6])
    begin_fill()

    for i in range(4):      
        fd(m)
        obrot(n)

    end_fill()

    for i in range(4):  
        fd(m/4)
        kwadraciki(n-1,m/2,k+1)
        fd(m*3/4)
        obrot(n)

a = 5
ln = 250
kolory = ['red', 'green', 'blue', 'yellow', 'cyan', 'violet']

penup()
if a%2 == 0: goto(-ln/2,ln/2)
else: goto(-ln/2,-ln/2)
pendown()

speed('fastest')
tracer(0, 0)
kwadraciki(a,ln)
update()
done()