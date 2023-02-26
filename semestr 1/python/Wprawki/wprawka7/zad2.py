def cycles(p):
    mapa = {i+1: p[i] for i in range(len(p))}
    cycles = []
    
    while mapa:
        element = next(iter(mapa))
        obecny = mapa[element]
        nastepny = mapa[obecny]

        cycle = []
        while True:
            cycle.append(obecny)
            del mapa[obecny]
            obecny = nastepny
            if nastepny in mapa:
                nastepny = mapa[nastepny]
            else: break

        cycles.append(cycle)

    return cycles

print(cycles([1,2,3,4,5,6,7,8]))
print(cycles([4,2,7,6,5,8,1,3]))
print(cycles([4,1,7,6,8,2,5,3]))