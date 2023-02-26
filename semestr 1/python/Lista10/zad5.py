def relacje(lista):
    if len(lista) == 1:
        yield [lista]
        return

    pierwszy = lista[0]
    for ogon in relacje(lista[1:]):
        for i, podzbior in enumerate(ogon): 
            yield ogon[:i] + [[pierwszy] + podzbior] + ogon[i+1:] 
        yield [[pierwszy]] + ogon

l1 = [1,2]
l2 = [1, 2, 3]
a = list(relacje(l1))
b = list(relacje(l2))

print()
for i in a: print(i)
print()
for i in b: print(i)
print()