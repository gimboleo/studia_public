def nww(a,b):
    if a==0 or b==0: return 0
    c = a
    d = b
    while(c!=d):
        if c<d:
            c=c+a
        else:
            d=d+b
    return c

print(nww(6,9))
print()



def nwd(a,b):
    if a<b:
        c = a
        a = b
        b = c
    while(b>0):
        a = a%b
        if a<b:
            c = a
            a = b
            b = c
    return a
        
def skracanie(a,b):
    if b == 0: return "Dzielenie przez 0"
    c = nwd(a,b)
    print(a/c)
    print('---')
    print(b/c)

skracanie(27,90)