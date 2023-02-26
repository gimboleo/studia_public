'''
Rozwiązanie polega na prostym systemie wnioskowania.
Komórki potencjalnych podrozwiązań porównujemy z template'ami (informacjami, które już o nich mamy):
· 0 - sprzeczność (coś poszło nie tak)
· 1 - komórka zamalowana
· 2 - komórka pusta
· 3 - komórka bez jednoznacznego rozwiązania
Algorytm naprzemiennie rozważa kolumny i wiersze tablicy.

Jeśli po wnioskowaniu zostały jakieś pola bez rozwiązania, musimy wykonać backtracking:
· Bierzemy dowolne takie pole i ustawiamy jego stan na 1
· Wywołujemy rekurencyjnie wnioskowanie
· Jeśli się ono powiodło, zwracamy wynik, w przeciwnym wypadku ustawiamy nasze pole 2 i powracamy do wnioskowania\
· Jeśli się ono powiodło, zwracamy wynik, w przeciwnym wypadku otrzymaliśmy sprzeczność
'''

from functools import reduce
import numpy as np





def solve(h_hints, v_hints):
    def gen_line(length, line_hint):
        '''Generacja wszystkich możliwych kombinacji danego wiersza/kolumny'''

        def gen_segment(seg, whites):
            if not seg: return [[2] * whites]
            return [[2] * i + seg[0] + tail for i in range(1, whites - len(seg) + 2) for tail in gen_segment(seg[1:], whites - i)]
 
        return [x[1:] for x in gen_segment([[1] * i for i in line_hint], length + 1 - sum(line_hint))]


    def gen_template(line): 
        '''Ustalanie stanów danych kwadratów w linii: 1 | 1 = 1     1 | 2 = 3     2 | 2 = 2     3 | * = 3'''
        return reduce(lambda a, b: [x | y for x, y in zip(a, b)], line) if line else []
 

    def matches(a, b): 
        '''
        Ustalanie czy rozwiązanie linii pasuje do template'u:
        0 | * = 0     1 | 1 = 1     1 | 2 = 0     2 | 2 = 2     3 | * = *
        '''
        return all(x & y for x, y in zip(a, b))
 

    def infer_row(n):
        mod_cols = set()
        template = templates[n]
        rows[n] = list(filter(lambda e: matches(e, template), rows[n]))
        if not rows[n]: return False

        for i, x in enumerate(gen_template(rows[n])):
            if x != templates[n][i]:
                mod_cols.add(i)
                templates[n][i] &= x
                if not templates[n][i]: return False
        return mod_cols


    def infer_col(n):
        mod_rows = set()
        template = [x[n] for x in templates]
        cols[n] = list(filter(lambda e: matches(e, template), cols[n]))
        if not cols[n]: return False

        for i, x in enumerate(gen_template(cols[n])):
            if x != templates[i][n]:
                mod_rows.add(i)
                templates[i][n] &= x
                if not templates[i][n]: return False
        return mod_rows


    def deduct(y = -1, x = -1):
        nonlocal rows, cols, templates

        # Zbiory linii do naprawienia
        if y >= 0 and x >= 0: mod_rows, mod_cols = {y}, {x}
        else: mod_rows, mod_cols = set(), set(range(width))

        while mod_cols:
            for i in mod_cols: 
                aux = infer_col(i)
                if aux == False: return False
                mod_rows |= aux
            mod_cols.clear()
            for i in mod_rows: 
                aux = infer_row(i)
                if aux == False: return False
                mod_cols |= aux
            mod_rows.clear()

        aux = np.where(templates == 3)
        if len(aux[0]):
            i, j = aux[0][0], aux[1][0]
            rows_backup = [[k[:] for k in l] for l in rows]
            cols_backup = [[k[:] for k in l] for l in cols]
            templates_backup = templates.copy()
            templates[i][j] = 1
            aux2 = deduct(i, j)
            if aux2: return aux2
            rows = rows_backup
            cols = cols_backup
            templates = templates_backup
            templates[i][j] = 2
            return deduct(i, j)

        return '\n'.join(''.join('x#.?'[i] for i in x) for x in templates)



    width, height = len(v_hints), len(h_hints)
    rows = [gen_line(width, x) for x in h_hints]
    cols = [gen_line(height, x) for x in v_hints]
    templates = np.array(list(map(gen_template, rows)))
  
    return deduct()





if __name__ == '__main__':
    with open('zad_input.txt', 'r') as in_file, open('zad_output.txt', 'w') as out_file:
        i = int(in_file.readline().split()[0])
        input = in_file.read().splitlines()
        
        data = [[[*map(int, h.split(' '))] for h in input[:i]], [[*map(int, v.split(' '))] for v in input[i:]]]
        #print(data)
        #print(solve(*data))
        res = solve(*data)
        out_file.write(res if res else 'IMPOSSIBLE')