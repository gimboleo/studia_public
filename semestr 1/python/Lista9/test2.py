from collections import defaultdict as dd
from itertools import product
from collections import Counter

s = ('ala','ma','kota','kot','ma','ale','ja','mam','depresje')
anadl = dd(list)
for i in s:
    anadl[len(i)].append(i)


print(anadl[4])
for i in anadl[3]:
    print(Counter(i))

a = [1,2,3]
b = [4,5,6]
c = [7,8,9]

print(list(product(a,a,b)))