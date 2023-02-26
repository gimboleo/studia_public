from turtle import *
def kolko(n,a):
    if n == 0: return 0
    fillcolor(kolory[n%3])
    begin_fill()
    for i in range(360):
        fd(a)
        rt(1)
    end_fill()
    kolko(n-1,a-0.2)

x = 13
a = 3
kolory = ['#ff4e50','#f9d423','#e1f5c4']

penup()
goto(0,a*60)
pendown()
#lt(6)

speed('fastest')
tracer(0,0)
kolko(x,a)
update()
done()