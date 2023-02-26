import re

def importbrown():
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

    return d

importbrown()
print('Done')