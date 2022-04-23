'''
• Zaczynamy od pewnego przypisania koloru wszystkim polom obrazka (np. losowo, albo same zera).

• W trakcie działania algorytm będzie on zmieniał kolor wybranego pola obrazka (jednego), 
  aż do momentu, w którym obrazek będzie gotowy

• Wybór pola realizujemy w następujący sposób:
    – Losujemy wiersz (lub kolumnę), która jest niezgodna ze specyfikacją (tzn. czarne piksele
      nie tworzą jednego bloku o wymaganej długości)
    – Wybieramy piksel o współrzędnych (i,j), którego zmiana w największym stopniu poprawi
      sumaryczny poziom dopasowania w wierszu i oraz w kolumnie j.

• Wszystkie wybory z niewielkim prawdopodobieństwem robimy nieoptymalnie (psujemy dobry
  wiersz, naprawiamy tylko wiersz, zamiast wiersza i kolumny, itd).

• Jeżeli nie otrzymaliśmy przez dłuższy czas rozwiązania, to losujemy jescze raz ustawienia początkowe.
'''


from cmath import inf
import numpy as np
from random import random, randrange
from zadanie4 import opt_dist_int as opt_dist

ITER_CAP = 500
RANDOM_FACTOR = 0.02





def solve(rows, columns):
    def is_done():
        for a, b in zip(res, rows):
            if opt_dist(a, b): return False
        for a, b in zip(res.T, columns): 
            if opt_dist(a, b): return False
        return True



    def change_cell():
        if random() < RANDOM_FACTOR: res[randrange(r)][randrange(c)] ^= 1
        else:
            if randrange(2):
                for i in np.random.permutation(r):
                    prev_r = opt_dist(res[i], rows[i])
                    if prev_r:
                        best = -1
                        improv = -inf

                        for j in range(c):
                            prev_c = opt_dist(res[:, j], columns[j])
                            res[i][j] ^= 1
                            aux = prev_r + prev_c - opt_dist(res[i], rows[i]) - opt_dist(res[:, j], columns[j])
                            if (aux > improv):
                                best = j
                                improv = aux
                            res[i][j] ^= 1
                        
                        res[i][best] ^= 1
                        break
            else:
                for j in np.random.permutation(c):
                    prev_c = opt_dist(res[:, j], columns[j])
                    if prev_c:
                        best = -1
                        improv = -inf

                        for i in range(r):
                            prev_r = opt_dist(res[i], rows[i])
                            res[i][j] ^= 1
                            aux = prev_r + prev_c - opt_dist(res[i], rows[i]) - opt_dist(res[:, j], columns[j])
                            if (aux > improv):
                                best = i
                                improv = aux
                            res[i][j] ^= 1
                        
                        res[best][j] ^= 1
                        break



    n = ITER_CAP
    r = len(rows)
    c = len(columns)

    while (True):
        if (n < ITER_CAP):
            n += 1
            change_cell()
            if is_done(): return res
        else:
            res = np.zeros((r, c), dtype = int)
            n = 0



def printer(res):
    printed = ''
    for i in res:
        for j in i:
            printed += '#' if j else '.'
        printed += '\n'
    return printed





if __name__ == '__main__':
    with open('zad5_input.txt', mode='r') as in_file, open('zad5_output.txt', mode='w') as out_file:
        r, c = [int(_) for _ in next(in_file).split()]
        rows = [next(in_file).strip() for _ in range(r)]
        columns = [next(in_file).strip() for _ in range(r)]

        res = printer(solve(rows, columns))
        print(res)
        out_file.write(res)