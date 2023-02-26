from zad1 import *

F = []
F.append(new_triangle(0, 0, 5, 10, 10, 5))
F.append(new_circle (5, 5, 2))
F.append(new_square(4, -3, 7))

for i in F: print(pole(i))
print()

print(F[1][1])
przesun(F[1], -4, 8)
print(F[1][1])
print()

print(F[0][1], F[0][2], F[0][3])
przesun(F[0], 1, -1)
print(F[0][1], F[0][2], F[0][3])
print()

print(sumapol(F,3))

'''
Jeśli chcielibyśmy dodać trapezy, należałoby dodać trapez do typfig, stworzyć nową funkcję new_trapezoid, za pomocą której
jednoznacznie będzie można określić trapez (Przykładowo z 8 argumentami, gdzie każdy reprezentuje jedną ze współrzędnych jednego
z wierzchołków figury), dodać do funkcji pole wzór na obliczanie trapezu, a do funkcji przesuń dodać wyjątek dla trapezu.
(dla przesuwania 4 współrzędnych).
'''