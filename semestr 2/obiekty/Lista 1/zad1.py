class typfig:
    triangle, circle, square = range(3)

def new_triangle(x1,y1,x2,y2,x3,y3):
    assert not((x1 == x2 and y1 == y2) or (x1 == x3 and y1 == y3) or (x2 == x3 and y2 == y3)), "Wspolrzedne musza byc rozne."
    return [typfig.triangle, [x1,y1], [x2,y2], [x3,y3]]

def new_circle(x,y,r):
    assert r > 0, "Promien kola musi byc dodatni."
    return [typfig.circle, [x,y], r]

def new_square(x,y,a):                                          #x,y - wspolrzedne lewego dolnego rogu kwadratu
    assert a > 0, "Dlugosc boku kwadratu musi byc dodatnia."
    return [typfig.square, [x,y], a]

def pole(f):
    if f[0] == 0: return 0.5 * abs((f[2][0] - f[1][0]) * (f[3][1] - f[1][1]) - (f[2][1] - f[1][1]) * (f[3][0] - f[1][0]))
    if f[0] == 1: return 3.141 * f[2]**2
    if f[0] == 2: return f[2]**2

def przesun(f,x,y):
    f[1][0] = f[1][0] + x
    f[1][1] = f[1][1] + y
    if f[0] == 0:
        f[2][0] = f[2][0] + x
        f[2][1] = f[2][1] + y
        f[3][0] = f[3][0] + x
        f[3][1] = f[3][1] + y

def sumapol(F,size):
    res = 0
    for i in range(size): res = res + pole(F[i])
    return res