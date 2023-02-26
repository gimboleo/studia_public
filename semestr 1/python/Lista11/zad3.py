def ppn(slowo):
    litery = dict()
    counter = 1
    for l in slowo:
        if l not in litery:
            litery[l] = counter
            counter += 1
    return '-'.join([str(litery[l]) for l in slowo])

print(ppn('tak'))
print(ppn('nie'))
print(ppn('tata'))
print(ppn('indianin'))