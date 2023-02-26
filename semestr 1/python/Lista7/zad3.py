import re
#import time

d = dict()

'''
line = "1. 14124 'POLSKA' biało-czerwoni!!!!. Ala ma kota, a ja nie. ĄĘÓŻ ***** ***"
line = re.sub(r"[^A-Za-ząćęłńóśźżĄĆĘŁŃÓŚŹŻ\s]", " ", line)
line = line.lower()
T = line.split()
for slowo in T:
    if slowo in d: d[slowo] = d[slowo] + 1
    else: d[slowo] = 1
'''

with open(r'C:\Users\kubak\Desktop\studia\semestr 1\Python\Lista7\lalka.txt',encoding='utf-8') as plik:
    for linijka in plik:
        line = linijka
        line = re.sub(r"[^A-Za-ząćęłńóśźżĄĆĘŁŃÓŚŹŻ\s]", " ", line)
        line = line.lower()
        T = line.split()
        for slowo in T:
            if slowo in d: d[slowo] = d[slowo] + 1
            else: d[slowo] = 1


#print(d)
#print(wokulski,d['wokulski'])
'''
for i in sorted(d, key=d.get, reverse=True):
        print(i, d[i])
        time.sleep(0.5)
'''

for a in range(0,4):
    print('a:',a)
    W = []
    for i in d:
        W.append((i,d[i]*(len(i)**a)))
    W.sort(key=lambda x: x[1], reverse=True)
    for i in range(10):
        print(i+1,': ',W[i],sep='')
    print()


