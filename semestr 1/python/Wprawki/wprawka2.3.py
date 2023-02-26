from turtle import *
def pascal(n):
    if n == 0: return [[1]]
    nowy_rzad = [1]
    wynik = pascal(n-1)
    stary_rzad = wynik[-1]
    for i in range(len(stary_rzad)-1):
        nowy_rzad.append(stary_rzad[i]+stary_rzad[i+1])
    nowy_rzad+=[1]
    wynik.append(nowy_rzad)
    return wynik

def sierpinski(P,x,y,z):
    if z == 0: return 0
    penup()
    goto(x,y)
    pendown()
    for i in range(len(P[z-1])):
        if P[z-1][i]%2 == 1:
            dot()
        penup()
        fd(20)
        pendown()
    sierpinski(P,x+10,y+10,z-1)

speed('fastest')
x = 0
y = 0
z = 31
tracer(0,0)
sierpinski(pascal(z),x,y,z+1)
update()
done()
