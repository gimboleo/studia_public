import turtle
import random
import colorsys

screen = turtle.Screen()
screen.tracer(0,0)
screen.setup(700,700)
screen.bgcolor('black')

strzalki = [turtle.Turtle() for i in range(100)]

h = 0
for i in range(100):
    h += 1/100
    strzalki[i].color(colorsys.hsv_to_rgb(h,1,0.8))
    strzalki[i].up()
    strzalki[i].seth(random.randint(0,359))
    strzalki[i].goto(random.randint(-350,350), random.uniform(-350,350))

while True:
    for i in range(99): strzalki[i].seth(strzalki[i].towards(strzalki[i+1]))
    strzalki[99].seth(strzalki[99].towards(strzalki[0]))
    for i in range(100): strzalki[i].fd(1)
    screen.update()
    
