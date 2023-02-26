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

    for key in s1:
        if key not in s2: return False
        if s1[key] > s2[key]: return False
    return True
 
print(ukladalne('ala','alabama'))
print(ukladalne('alabama','ala'))
print(ukladalne('łoś','łosoś'))