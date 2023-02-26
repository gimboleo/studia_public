x = 6

T = set()
for i in range(x-2,0,-1):
    for j in range(i,0,-1):
        if i+j >= x: continue
        for k in range(j,0,-1):
            if i+j+k == x: T.add((i,j,k))

for i in T:
    print(i[0])