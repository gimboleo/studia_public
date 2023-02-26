'''
Rozwiązanie polega na dodaniu wnioskowania podobnego do tego z wykładu. Jest ono opisane w komentarzach.
'''

def B(i, j): return f'B_{i}_{j}'

def domains(bs): return [f'{q} in 0..1' for q in bs]



def storms(rows, cols, declarations):
    res = ':- use_module(library(clpfd)).\n\n'

    R = len(rows)
    C = len(cols)

    bs = ', '.join([B(i, j) for i in range(R) for j in range(C)])

    res += f'solve([{bs}]) :-\n\n'


    # Dziedzina zmiennych {0, 1}
    res += f'[{bs}] ins 0..1,\n'

    # Odpowiednia suma w rzędach
    for i, r in enumerate(rows):
        res += f'sum([{", ".join([B(i, j) for j in range(C)])}], #=, {str(r)}),\n'

    # Odpowiednia suma w kolumnach
    for j, c in enumerate(cols):
        res += f'sum([{", ".join([B(i, j) for i in range(R)])}], #=, {str(c)}),\n'

    # Wypełnienie jednej przekątnej kwadratu 2 x 2 implikuje wypełnienie drugiej przekątnej
    for i in range(R - 1):
        for j in range(C - 1):
            res += f'{B(i, j + 1)} + {B(i + 1, j)} #= 2 #<==> {B(i, j)} + {B(i + 1, j + 1)} #= 2,\n'

    # Każdy 'pasek' w kolumnach jest długości conajmniej 2 
    for j in range(C):
        for i in range(R - 2):
            res += f'{B(i + 1, j)} #= 1 #==> {B(i, j)} + {B(i + 2, j)} #>= 1,\n'

    # Każdy 'pasek' w rzędach jest długości conajmniej 2
    for i in range(R):
        for j in range(C - 2):
            res += f'{B(i, j + 1)} #= 1 #==> {B(i, j)} + {B(i, j + 2)} #>= 1,\n'

    # Deklaracje określonych pól podane w inpucie
    for x, y, val in declarations: res += f'{B(x, y)} #= {val},\n'


    res += '\n'
    res += f'labeling([ff], [{bs}]).\n\n'
    res += ":- tell('prolog_result.txt'), solve(X), write(X), nl, told.\n"

    return res





if __name__ == '__main__':
    with open('zad_input.txt', 'r') as in_file, open('zad_output.txt', 'w') as out_file:
        input = in_file.read().splitlines()
        filled_out = [map(int, declaration.split()) for declaration in input[2:]]

        out_file.write(storms(input[0].split(), input[1].split(), filled_out))