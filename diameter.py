import io
from collections import defaultdict



test1 = io.StringIO('''5
1 2
1 3
1 4
1 5''')

test2 = io.StringIO('''4
1 2
2 3
3 4''')


int BFS(G: (V, E), source: int, destination: int):
d = int[|V|]
fill(d, ∞)
d[source] = 0
Q = ∅
Q.push(source)
while Q ≠∅
u = Q.pop()
for v: (u, v) in E
if d[v] == ∞
d[v] = d[u] + 1
Q.push(v)
return d[destination]

def bfs(graph, node):
    distances = []
    queue = []
    visited.append(node)
    queue.append(node)
    while queue:
        s = queue.pop(0)
        print(s, end = " ")
        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
    return len(visited)

def diameterTree(g, graph_len):
    v = u = w = 1
    d = bfs(g, v)
    for i in range(graph_len):
        if d[i] > d[u]:
            u = i
    bfs(g, u)
    for i in range(graph_len):
        if d[i] > d[w]:
            w = i
    return d[w]

def main(str_buffer):
    graph = defaultdict(list)
    graph_len = int(next(str_buffer))
    for i in range(graph_len-1):
        node1, node2 = map(int, next(str_buffer).strip().split())
        graph[node1].append(node2)
        graph[node2].append(node1)
    print(graph)
    diameterTree(graph, graph_len)

main(test1)