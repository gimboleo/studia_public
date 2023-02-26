import sys

str1 = "🐍afsdf"

print(sys.getsizeof(str1))

def dlugoscnapisu(string):
    temp = 0
    for l in string:
        if sys.getsizeof(l) > temp: temp = sys.getsizeof(l)
    if not temp: print('49')
    if temp == 50:
        suma = 49
        for l in string: suma+= 1
        print(suma)
    if temp == 78:
        suma = 76
        for l in string: suma += 2
        print(suma)
    if temp == 80:
        suma = 76
        for l in string: suma += 4
        print(suma)

print(dlugoscnapisu(str1))


