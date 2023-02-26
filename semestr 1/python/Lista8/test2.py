string = "Gabrysia modnisia"
string = string.lower()
string = string.replace(' ','')
print(string)
s1 = string[15:]
s2 = string[:15]
print(s1)
print(s2)
print(len(string))
for i in range(1,len(string)):
    s1 = string[i:]
    s2 = string[:i]
    print(s1)
    print(s2)

from itertools import permutations
T = [''.join(p) for p in permutations('gabrysia')]
print(len(T))