'''
Zadanie zaimplementowane jest protym BFS-em, ktorego ruchy ograniczone sa przez mozliwe ruchy danych pionkow.
Mat wystepuje w sytuacji, kiedy czarny krol nie moze wykonac legalnego ruchu.
INF wystepuje w sytuacji, kiedy mat nie zostanie znaleziony.
(sytuacje patowa, przykladowo zbicie wiezy, traktujemy jako niewygrywajacy stan koncowy)
'''


from collections import deque

from numpy import true_divide

KING_MOVES = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, -1), (-1, 1)]





def possible_rook(rook, wk, bk):
    h, v = rook
    for i in range(8):
        if i != v and not is_blocked_w(rook, wk, bk, (h, i)): yield (h, i)
        if i != h and not is_blocked_w(rook, wk, bk, (i, v)): yield (i, v)


def possible_wk(rook, wk, bk):
    h, v = wk

    for move in KING_MOVES:
        nh = h + move[0]
        nv = v + move[1]
        if 0 <= nh <= 7 and 0 <= nv <= 7 and not is_blocked_w(rook, wk, bk, (nh, nv)): yield (nh, nv)


def possible_bk(rook, wk, bk):
    h, v = bk

    for move in KING_MOVES:
        nh = h + move[0]
        nv = v + move[1]
        if 0 <= nh <= 7 and 0 <= nv <= 7 and not is_blocked_b(rook, wk, bk, (nh, nv)): yield (nh, nv)


def is_blocked_w(rook, wk, bk, pos):
    return pos == rook or pos == wk or (abs(pos[0] - bk[0]) <= 1 and abs(pos[1] - bk[1]) <= 1)


def is_blocked_b(rook, wk, bk, pos):
    return (abs(pos[0] - wk[0]) <= 1 and abs(pos[1] - wk[1]) <= 1) or ((pos[0] == rook[0]) ^ (pos[1] == rook[1]))
    #ignoring situations in which wk is blocking rook from attacking bk as they would lead to inoptimal solutions




def find_mate(rook, wk, bk, first):
    prev = {}
    states = set()
    Q = deque()
    init = (rook, wk, bk, first)

    prev[init] = init
    Q.append(init)
    states.add(init)


    while Q:
        state = Q.popleft()

        if state[3]:    #white
            for move in possible_wk(*state[:3]):
                new = (state[0], move, state[2], 0)
                if new not in states:
                    states.add(new)
                    Q.append(new)
                    prev[new] = state
            for move in possible_rook(*state[:3]):
                new = (move, state[1], state[2], 0)
                if new not in states:
                    states.add(new)
                    Q.append(new)
                    prev[new] = state
        else:           #black
            flag = False
            for move in possible_bk(*state[:3]):
                flag = True
                if move == state[0]: continue   #rook is eliminated
                new = (state[0], state[1], move, 1)
                if new not in states:
                    states.add(new)
                    Q.append(new)
                    prev[new] = state
            
            if not flag:    #black couldn't make a move
                res = []
                while state != prev[state]:
                    res.append((prev[state], state))
                    state = prev[state]
                return res
    
    return 'INF'




def process(piece): return (ord(piece[0]) - 97, int(piece[1]) - 1)

def deprocess(move):
    for i, j in zip(move[0], move[1]):
        if i != j: return f'{chr(i[0] + 97)}{i[1] + 1}{chr(j[0] + 97)}{j[1] + 1}'

def printer(state):
    res = ''
    for i in range(8):
        for j in range(8):
            if state[0] == (j, i): res += 'R'
            elif state[1] == (j, i): res += 'W'
            elif state[2] == (j, i): res += 'B'
            else: res += '□'
        res += '\n'
    return res



if __name__ == '__main__':
    moving_player, white_king, white_rook, black_king = input().split()

    #print(find_mate(process(white_rook), process(white_king), process(black_king), ord(moving_player[0]) % 2))

    for move in reversed(find_mate(process(white_rook), process(white_king), process(black_king), ord(moving_player[0]) % 2)):
        print(deprocess(move), end = ' ')
    print()

'''
    first = True
    for move in reversed(find_mate(process(white_rook), process(white_king), process(black_king), ord(moving_player[0]) % 2)):
        if first:
            first = False
            print(printer(move[0]))
        print(printer(move[1]))
'''



'''
if __name__ == '__main__':
    with open('zad1_input.txt', mode='r') as in_file, open('zad1_output.txt', mode='w') as out_file:
        moving_player, white_king, white_rook, black_king = next(in_file).split()
        out_file.write(f'{len(find_mate(process(white_rook), process(white_king), process(black_king), ord(moving_player[0]) % 2))}')
'''