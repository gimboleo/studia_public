from turtle import *

def kwadrat(bok):
    begin_fill()
    for i in range(4):
      fd(bok)
      rt(90)
    end_fill()
    
def murek(s,bok):
  for a in s:
     if a == 'f':
         kwadrat(bok)
         fd(bok)
     elif a == 'b':
         kwadrat(bok)
         fd(bok)         
     elif a == 'l':
         bk(bok)
         lt(90)
     elif a == 'r':
        rt(90)
        fd(bok)
     elif a =='v':
         fillcolor('medium violet red')
     elif a =='p':
         fillcolor('medium purple')
     elif a =='g':
         fillcolor('dark slate blue')
     elif a =='w':
         fillcolor('white')

def kwadracik(a):
    rysunek = 'vf'
    for i in range(a):
        for j in range(a-1):
            rysunek = rysunek + 'f'
            if i == a-1 and j== a-2: return rysunek
        if i%2 == 0: rysunek = rysunek + 'lpfl'
        if i%2 == 1: rysunek = rysunek + 'rvfr'

def spirala(a):
    x = 0
    b = a
    rysunek = ''
    while b != 0:
        for i in range(b):
            if x%3 == 0: rysunek = rysunek + 'v'
            elif x%3 == 1: rysunek = rysunek + 'p'
            elif x%3 == 2: rysunek = rysunek + 'g'
            rysunek = rysunek + 'f'
            x = x + 1
        rysunek = rysunek + 'l'
        b = b - 1
    return rysunek

ht()

tracer(0,0)  
murek(kwadracik(10),15)
penup()
murek('wf',15)
pendown()
murek(spirala(10),15)
update()
done()