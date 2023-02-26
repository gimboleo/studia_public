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


def mult(a,b):

    for i in range(len(b)):
        if len(b) != len(a[i]): return 'error'  #rzad a = kolumna b (dlugosc)

    x = len(a[0])
    for i in range(1,len(a)):
        if len(a[i]) != x: return 'error'      #rzedy a i b takiej samej dlugosci

    x = len(b[0])
    for i in range(1,len(b)):
        if len(b[i]) != x: return 'error'

    c = []
    for i in range(len(a)):
        d = []
        for j in range(len(a[i])):
            temp = 0
            for k in range(len(a[i])):
                temp = temp + (a[i][k] * b[k][j])
            d.append(temp)
        c.append(d)
    return c



with open(r'C:\Users\kubak\Desktop\Python\wprawka3\A.matrix') as plikA:
        for linijka in plikA:
            A = literal_eval(linijka)

with open(r'C:\Users\kubak\Desktop\Python\wprawka3\B.matrix') as plikB:
        for linijka in plikB:
            B = literal_eval(linijka)

print(mult(A,B))
print(mult(B,A))
