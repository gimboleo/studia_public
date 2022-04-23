'''
Najpierw zachłannie dopychamy wszystkie pozycje do boków na obu osiach, potem wykonujemy BFS-a.
W BFS-ie w celach optymalizacji traktujemy stany o mniejszej ilości możliwych pozycji jako lepsze.
'''


from collections import deque

Y = [-1, 1, 0, 0]
X = [0, 0, -1, 1]
MOVES_NAMES = {0: 'U', 1: 'D', 2: 'L', 3: 'R'}





walls = set()
goals = set()

class State:
    def __init__(self, positions, movs):
        self.positions = positions
        self.movs = movs





def init(data):
    positions = set()

    for i in range(len(data)):
        for j in range(len(data[0])):
            x = data[i][j]
            if x == '#': walls.add((i, j))
            elif x == 'G': goals.add((i, j))
            elif x == 'S': positions.add((i, j))
            elif x == 'B':
                goals.add((i, j))
                positions.add((i, j))

    return State(frozenset(positions), [])



def move(state, mov):
    n_positions = set()
    
    for pos in state.positions:
        y = pos[0] + Y[mov]
        x = pos[1] + X[mov]
        if (y, x) not in walls: n_positions.add((y, x))
        else: n_positions.add(pos)

    return State(frozenset(n_positions), [*state.movs, MOVES_NAMES[mov]])



def moves(state, mov, n):
    for _ in range(n): state = move(state, mov)
    return state



def is_final(state):
    for position in state.positions:
        if position not in goals: return False
    return True



def get_adjs(state): return [move(state, i) for i in range(len(X))]



def bfs(state):
    visited = set()
    visited.add(state.positions)

    shortest = len(state.positions)

    q = deque()
    q.append(state)


    while q:
        curr = q.popleft()

        if is_final(curr): return curr.movs
        
        adjs = get_adjs(curr)
        for adj in adjs:
            if adj.positions not in visited:
                if len(adj.positions) < shortest:
                    visited.clear()
                    visited.add(adj.positions)
                    shortest = len(adj.positions)
                    q.clear()
                    q.append(adj)
                    break
                
                visited.add(adj.positions)
                q.append(adj)





if __name__ == '__main__':
    with open('zad_input.txt', 'r') as in_file, open('zad_output.txt', 'w') as out_file:
        data = in_file.readlines()


        init_state = init(data)

        mid_state_1 = moves(init_state, 1, len(data) - 2)
        mid_state_2 = moves(mid_state_1, 2, len(data[0]) - 2)

        final_state = bfs(mid_state_2)


        out_file.write(''.join(final_state))