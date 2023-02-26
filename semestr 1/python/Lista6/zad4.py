def podziel(napis):
    T = []
    temp = ''
    for l in range(len(napis)):
        if napis[l] == ' ':
            if temp != '': T.append(temp)
            temp = ''
        else: temp = temp + napis[l]
    if temp != '': T.append(temp)
    print(T)

podziel("   Ala ma   m  kota         ")