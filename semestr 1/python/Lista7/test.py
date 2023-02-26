from random import shuffle
T = [[1,2,3],[4,5,6],[7,8,9]] 
shuffle(T)
for i in range(len(T)):
    shuffle(T[i])
print(T)  

R = []
for i in range(len(T)):
    for j in range(len(T[0])):
        R.append((i,j))
shuffle(R)
print(R)