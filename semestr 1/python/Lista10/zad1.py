def caesar(s,k):
    s = s.lower()
    alfabet = 'aąbcćdeęfghijklłmnńoóprsśtuwyzźż'
    mapa = dict(zip(alfabet, ''.join((alfabet[k:],alfabet[:k]))))
    wynik = ''.join([mapa[l] for l in s])
    print(wynik)

caesar('abcd',1)