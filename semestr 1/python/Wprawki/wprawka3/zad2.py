from ast import literal_eval

def mprint ( m ) :
    for row in m :
        for i in range (len( row ) ) :
            if i == 0:
                print (" |{:^4} ". format ( row [ i ]) , end ="")
            elif i == len ( row ) -1:
                print (" {:^4}| ". format ( row [ i ]) )
            else :
                print (" {:^4} ". format ( row [ i ]) , end ="")
    print ()

def kronecker(a,b):

    x = len(a[0])
    for i in range(1,len(a)):
        if len(a[i]) != x: return 'error'

    x = len(b[0])
    for i in range(1,len(b)):
        if len(b[i]) != x: return 'error'

    d = []
    for i in range(len(a)):
        for j in range(len(b)):
            c = []
            for k in a[i]:
                for l in b[j]:
                    temp = k*l
                    c.append(temp)
            d.append(c)
    return d


with open(r'C:\Users\kubak\Desktop\Python\wprawka3\A.matrix') as plikA:
        for linijka in plikA:
            A = literal_eval(linijka)

with open(r'C:\Users\kubak\Desktop\Python\wprawka3\B.matrix') as plikB:
        for linijka in plikB:
            B = literal_eval(linijka)

A = [[1 ,2 ,3] ,[4 ,5 ,6]] # to wczytaj z pliku A. matrix
B = [[1 ,2 ,3 ,0] , [4 ,5 ,6 ,0] , [7 , 8 , 9 ,0]]# to wczytaj z pliku B. matrix


mprint(kronecker(A,B))
print()
mprint(kronecker(B,A))