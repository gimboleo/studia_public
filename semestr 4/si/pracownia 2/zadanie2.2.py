'''
. - puste pole
W - ściana
K - magazynier
B - skrzynia
G - pole docelowe
* - skrzynia na polu docelowym
+ - magazynier na polu docelowym
'''

from collections import deque

Y = [-1, 1, 0, 0]
X = [0, 0, -1, 1]
MOVES_NAMES = {0: 'U', 1: 'D', 2: 'L', 3: 'R'}





walls = set()
goals = set()

class State:
    def __init__(self, storeman, crates, movs):
        self.storeman = storeman
        self.crates = crates
        self.movs = movs





def init(data):
    crates = set()

    for i in range(len(data)):
        for j in range(len(data[0])):
            x = data[i][j]
            if x == 'W': walls.add((i, j))
            elif x == 'K': storeman = (i, j)
            elif x == 'B': crates.add((i, j))
            elif x == 'G': goals.add((i, j))
            elif x == '*':
                goals.add((i, j))
                crates.add((i, j))
            elif x == '+':
                storeman = (i, j)
                goals.add((i, j))

    return State(storeman, frozenset(crates), [])



def corner(y, x): 
    return ((y, x) not in goals and 
           ((y - 1, x) in walls or (y + 1, x) in walls) and 
           ((y, x - 1) in walls or (y, x + 1) in walls))



def move(state, mov):
    n_storeman = (state.storeman[0] + Y[mov], state.storeman[1] + X[mov])

    if n_storeman not in walls:
        if n_storeman in state.crates:
            n_crate = (n_storeman[0] + Y[mov], n_storeman[1] + X[mov])
            if n_crate not in state.crates and n_crate not in walls and not corner(*n_crate):
                n_crates = set(state.crates)
                n_crates.remove(n_storeman)
                n_crates.add(n_crate)
                return State(n_storeman, frozenset(n_crates), [*state.movs, MOVES_NAMES[mov]])
            return None
        return State(n_storeman, state.crates, [*state.movs, MOVES_NAMES[mov]])
    return None



def is_final(state):
    for crate in state.crates:
        if crate not in goals: return False
    return True



def get_adjs(state): return [x for x in (move(state, i) for i in range(len(X))) if x]



def bfs(state):
    visited = set()
    visited.add((state.storeman, state.crates))

    q = deque()
    q.append(state)


    while q:
        curr = q.popleft()

        if is_final(curr): return curr.movs

        for adj in get_adjs(curr):
            if (adj.storeman, adj.crates) not in visited:
                visited.add((adj.storeman, adj.crates))
                q.append(adj)





if __name__ == '__main__':
    with open('zad_input.txt', 'r') as in_file, open('zad_output.txt', 'w') as out_file:
        data = in_file.read().splitlines()
        out_file.write(''.join(bfs(init(data))))