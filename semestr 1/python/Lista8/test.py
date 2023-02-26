def ukladalne(slowo1,slowo2):
    slowo1 = slowo1.lower()
    slowo2 = slowo2.lower()
    if len(slowo1.split()) > 1 or len(slowo2.split()) > 1: return "Błąd"
    s2 = dict()
    for l in slowo2:
        if l not in s2: s2[l] = 1
        else: s2[l] += 1
    s1 = dict()
    for l in slowo1:
        if l not in s1: s1[l] = 1
        else: s1[l] += 1

    s3 = {sum: s1.get(sum, 0) + s2.get(sum, 0) for sum in set(s1) | set(s2)}
    print(s3)

ukladalne('ala','boba')
