import itertools
import time

def policz(slowo, slownik):
    s = 0
    for l in slowo:
        s = 10*s
        s += slownik[l]
    return s

def lamiglowka(zagadka):
    lewa,prawa = zagadka.lower().replace(' ','').split('=')
    lewa = lewa.split('+')

    litery = set(prawa)
    for slowo in lewa:
        for l in slowo: litery.add(l)
    litery = list(litery)

    cyfry = range(10)

    for p in itertools.permutations(cyfry, len(litery)):
        rozw = dict(zip(litery, p))

        if len(str(policz(prawa, rozw))) == len(prawa) and \
        sum(map(len,lewa)) == len(''.join(lewa)) and \
        sum(policz(slowo, rozw) for slowo in lewa) == policz(prawa, rozw):
            print(' + '.join(str(policz(slowo, rozw)) for slowo in lewa) + ' =', policz(prawa, rozw))
            print(rozw)
            break

start_time = time.time()
lamiglowka('SEND + MORE = MONEY')
print("--- %s seconds ---" % (time.time() - start_time))