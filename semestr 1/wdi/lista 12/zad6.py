def czyopn(napis):
    dlugoscstosu = 0
    liczby = {'0','1','2','3','4','5','6','7','8','9'}
    operatory = {'+','*'}
    for l in napis:
        if l in liczby: dlugoscstosu += 1
        elif l in operatory: dlugoscstosu -= 1
        if dlugoscstosu <= 0: return False
    if dlugoscstosu == 1: return True
    return False

print(czyopn("21+"))
print(czyopn("5+67*"))