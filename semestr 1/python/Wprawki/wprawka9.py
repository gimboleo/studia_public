import itertools
import matplotlib.pyplot as plt
import numpy as np

class wielomian:
    def __init__(self, *wspolczynniki):
        self.wspolczynniki = list(wspolczynniki)
        while self.wspolczynniki[0] == 0: 
            if len(self.wspolczynniki) < 2: break
            self.wspolczynniki = self.wspolczynniki[1:]

    def __str__(self):
        if len(self.wspolczynniki) == 1: return str(self.wspolczynniki[0])
        wynik = ""
        stopien = len(self.wspolczynniki) - 1
        wynik += str(self.wspolczynniki[0]) + "x^" + str(stopien)
        for i in range(1, len(self.wspolczynniki)-1):
            x = self.wspolczynniki[i]
            if x < 0:
                wynik += " - " +  str(-x) + "x^" + str(stopien - i)
            elif x > 0:
                wynik += " + " +  str(x) + "x^" + str(stopien - i)
                
        if self.wspolczynniki[-1] < 0:
            wynik += " - " + str(-self.wspolczynniki[-1])
        elif self.wspolczynniki[-1] > 0:
            wynik += " + " + str(self.wspolczynniki[-1])

        return wynik
    
    def __len__(self):
        return len(self.wspolczynniki)

    def plot(self,a,b):
        X = np.linspace(a,b, (b-a)*1000, endpoint=True)
        F = self(X)
        plt.plot(X, F)
        plt.show()

    def __call__(self,x):
        temp = 0
        for w in self.wspolczynniki: temp = temp * x + w
        return temp 

    def __add__(self, o):
        x1 = self.wspolczynniki[::-1]
        x2 = o.wspolczynniki[::-1]
        suma = [w1+w2 for w1, w2 in itertools.zip_longest(x1,x2,fillvalue=0)]
        return wielomian(*suma[::-1])

    def __sub__(self, o):
        x1 = self.wspolczynniki[::-1]
        x2 = o.wspolczynniki[::-1]
        suma = [w1-w2 for w1, w2 in itertools.zip_longest(x1,x2,fillvalue=0)]
        return wielomian(*suma[::-1])

    def __mul__(self, o):
        x1 = self.wspolczynniki[::-1]
        x2 = o.wspolczynniki[::-1]
        suma = [0]*(len(x1)+len(x2)-1)
        for w1, a1 in enumerate(x1):
            for w2, a2 in enumerate(x2):
                suma[w1+w2] += a1*a2
        return wielomian(*suma[::-1])
 

p4 = wielomian(1,-2,0,0)
p5 = wielomian(3,-2)
print(p4,p5,sep='   ')
print(p4*p5)
