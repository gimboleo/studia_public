'''
Rozwiązanie najpierw zmniejsza niepewność podobnie do zadania 4, a następnie wykonuje algorytm A* z heurystyką przemnożoną przez
dużą stałą.
'''


from collections import deque
from heapq import heappush, heappop

Y = [-1, 1, 0, 0]
X  = [0, 0, -1, 1]
MOVES_NAMES = {0: 'U', 1: 'D', 2: 'L', 3: 'R'}





walls = set()
goals = set()
distances = {}

class State:
    def __init__(self, positions, movs):
        self.positions = positions
        self.movs = movs

    def __lt__(self, other): return len(self.movs) < len(other.movs)





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



def find_dist(position):
    visited = set()
    visited.add(position)

    q = deque()
    q.append((position, 0))

    while q:
        curr, dist = q.popleft()

        if curr in goals: return dist

        for i in range(len(X)):
            next = (curr[0] + Y[i], curr[1] + X[i])
            if next not in walls and next not in visited:
                visited.add(next)
                q.append((next, dist + 1))



def gen_dists(y, x):
    for i in range(y):
        for j in range(x):
            if (i, j) not in walls: distances[(i, j)] = find_dist((i, j))



def priority(state):
    return 3 * max(distances[position] for position in state.positions) + len(state.movs)



def a_star(state):
    visited = set()
    visited.add(state.positions)

    h = []
    heappush(h, (priority(state), state))


    while h:
        _, curr = heappop(h)

        if is_final(curr): return curr.movs
        
        adjs = get_adjs(curr)
        for adj in adjs:
            if adj.positions not in visited:                
                visited.add(adj.positions)
                heappush(h, (priority(adj), adj))





if __name__ == '__main__':
    with open('zad_input.txt', 'r') as in_file, open('zad_output.txt', 'w') as out_file:
        data = in_file.readlines()


        init_state = init(data)

        gen_dists(len(data) - 1, len(data[0]) - 1)

        mid_state_1 = moves(init_state, 1, len(data) - 15)
        mid_state_2 = moves(mid_state_1, 3, len(data[0]) - 15)

        final_state = a_star(mid_state_2)


        out_file.write(''.join(final_state))