import random
from collections import defaultdict as dd

pol_ang = dd(lambda:[])

for x in open('pol_ang.txt',encoding='utf-8'):
    x = x.strip()
    L = x.split('=')
    if len(L) != 2:
        continue    
    pol, ang = L
    pol_ang[pol].append(ang)
    print(pol_ang)
    
def tlumacz(polskie):
    wynik = []
    for s in polskie:
        if s in pol_ang:
            wynik.append(random.choice(pol_ang[s]))
        else:
            wynik.append('[?]')
    return ' '.join(wynik)
    
zdanie = 'chłopiec z dziewczyna pójść do kino'.split()
print(tlumacz(zdanie))