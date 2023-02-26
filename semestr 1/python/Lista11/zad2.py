from colorsys import hsv_to_rgb, rgb_to_hsv
import turtle
import random
import time
import os

win = turtle.Screen()
win.bgcolor('black')
#win.setup(width = 1.0, height = 1.0)
win.setup(700, 700)
win.tracer(0)

#canvas = win.getcanvas()
#root = canvas.winfo_toplevel()
#root.overrideredirect(1)

def zderzenie(Ma, Mb, Va, Vb):
    nowa_a = ((Ma-Mb)/(Ma+Mb))*Va + ((2*Mb)/(Ma+Mb))*Vb
    nowa_b = ((2*Ma)/(Ma+Mb))*Va + ((Mb-Ma)/(Ma+Mb))*Vb
    return (nowa_a, nowa_b)

class kulka(turtle.Turtle):
    def __init__(self, masa, nr):
        super().__init__(shape = 'circle')
        self.up()
        self.masa = masa
        self.goto(random.randint(-350, 350), random.randint(-350,350))
        self.shapesize(masa/20)
        self.promien = masa/2
        self.nr = nr
        self.kolory = [hsv_to_rgb(0,1,1), hsv_to_rgb(120/360,1,1), hsv_to_rgb(240/360,1,1), hsv_to_rgb(60/360,1,1), hsv_to_rgb(300/360,1,1), hsv_to_rgb(180/360,1,1)]
        self.color('white', random.choice(self.kolory))
        self.zderzenie = True
        self.predkosci = [-3, -2, -1, 1, 2, 3]
        self.Vx = random.choice(self.predkosci)
        self.Vy = random.choice(self.predkosci)

    def kolorki(self):
        temp = self.fillcolor()
        obecny = rgb_to_hsv(temp[0], temp[1], temp[2])
        self.color(hsv_to_rgb((obecny[0]+0.001)%1, obecny[1], obecny[2]))

    def ruch(self):
        self.goto(self.xcor() + self.Vx, self.ycor() + self.Vy)

        if (self.xcor() >= 345 - self.promien and self.Vx > 0) or (self.xcor() <= -345 + self.promien and self.Vx < 0): self.Vx *= -1

        if (self.ycor() >= 345 - self.promien and self.Vy > 0) or (self.ycor() <= -345 + self.promien and self.Vy < 0): self.Vy *= -1

kulki = []
for i in range(10): kulki.append(kulka(random.randint(30,90), i))
licznik = 0

while True:
    win.update()
    time.sleep(0.01)
    
    for i in kulki:
        i.kolorki()
        if (not i.zderzenie) and licznik%10==0: i.zderzenie = True
        i.ruch()

        for j in kulki:
            if i.nr != j.nr and (i.zderzenie or j.zderzenie) and i.distance(j) < (i.promien + j.promien):
                i.zderzenie = False
                j.zderzenie = False

                temp = zderzenie(i.masa, j.masa, i.Vx, j.Vx)     
                i.Vx = temp[0]
                j.Vx = temp[1]
                        
                temp = zderzenie(i.masa, j.masa, i.Vy, j.Vy)
                i.Vy = temp[0]
                j.Vy = temp[1]

    licznik += 1