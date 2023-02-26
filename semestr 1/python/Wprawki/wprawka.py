from turtle import *
def sierp(a,b):
    if a == 0: return 1
    for i in range (3):
        fd(b/2)
        sierp(a-1,b/2)
        fd(b/2)
        lt(120)

speed('fastest')
sierp(4,300)
done()
