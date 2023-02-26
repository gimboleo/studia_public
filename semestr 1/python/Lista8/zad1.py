import re
#import time
import random
from collections import defaultdict as dd

d = dict()
with open(r'C:\Users\kubak\Desktop\Python\Lista8\brown.txt',encoding='utf-8') as plik:
    for linijka in plik:
        line = linijka
        line = re.sub(r"[^A-Za-z\s]", " ", line)
        line = line.lower()
        T = line.split()
        for slowo in T:
            if slowo in d: d[slowo] = d[slowo] + 1
            else: d[slowo] = 1   

pol_ang = dd(lambda:[])

for x in open('pol_ang.txt',encoding='utf-8'):
    x = x.strip()
    L = x.split('=')
    if len(L) != 2:
        continue    
    pol, ang = L
    pol_ang[pol].append(ang)

def tlumacz(polskie):
    wynik = []
    for s in polskie:
        if s in pol_ang:
            temp = pol_ang[s]
            counter = 0
            for w in pol_ang[s]:
                if w in d and d[w] > counter:
                    counter = d[w]
                    chosen = w
            wynik.append(chosen)
        else:
            wynik.append('[?]')
    return ' '.join(wynik)
    
zdanie = 'chłopiec z dziewczyna pójść do kino'.split()
print(tlumacz(zdanie))