from random import randint
x = 20*['.']
for i in range(len(x)):
    x[i] = (x[i],randint(1,5))
print(x)