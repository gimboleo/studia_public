from turtle import *
import time

tracer(0,0)
FRAME_RATE = 1/30

pensize(3)

def kwadrat(bok):
    for i in range(4):
        fd(bok)
        rt(90)

def rozeta(N, kat):
    for i in range(N): 
        fd(70)
        rt(kat)
        kwadrat(30)
        lt(kat)
        bk(70)
        rt(360 / N)


D1 = 10

kat = 0
D2 = 6

while True:       
    t0 = time.time()
    clear()
    rozeta(10, kat)
    update()
    rt(D2)
    kat += D1
    dt = time.time() - t0
    if dt < FRAME_RATE:
        time.sleep(FRAME_RATE - dt)

input()