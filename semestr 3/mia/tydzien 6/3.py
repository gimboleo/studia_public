from collections import defaultdict


def dfs(graph, x, y):
    visited = {x}
    stack = [x]

    while stack:
        e = stack.pop()
        visited.add(e)

        for ch in graph[e]:
            if ch != y and ch not in visited: stack.append(ch)
    
    return len(visited)


n, x, y = [int(x) for x in input().split()]
edges = defaultdict(list)


for i in range(n - 1):
    u, v = [int(x) for x in input().split()]
    edges[u].append(v)
    edges[v].append(u)

x_n = n - dfs(edges, x, y)
y_n = n - dfs(edges, y, x)

print(n * (n - 1) - x_n * y_n)