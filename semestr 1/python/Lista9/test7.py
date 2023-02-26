import math
T = 5*[math.inf]
print(T)
for i in range(5):
    if i < T[i]: T[i] = i
print(T)

X = [0,1,2,3,4]
print(len(X))
print(X[len(X)-1])
N = len(X) * [0]
print(N)