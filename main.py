from algorithm import shortest_path

# to open input file
f = open('input.txt', 'r')

# to read the whole document
lines = f.readlines()

# (no. of nodes, no. of edges)
size = tuple((lines[0].replace('\n', '').split(' ')))

# names of the nodes
names = lines[1].replace('\n', '').split(' ')

# starting index
start = int(lines[2])

# to check if the graph is cyclic or not
def has_cycle(graph):
    visited = set()
    recursion_stack = set()

    def dfs(node):
        visited.add(node)
        recursion_stack.add(node)

        for neighbor, weight in graph[node]:
            if neighbor not in visited:
                if graph.get(neighbor) and dfs(neighbor):
                    return True
            elif neighbor in recursion_stack:
                return True

        recursion_stack.remove(node)
        return False

    for node in graph:
        if node not in visited:
            if dfs(node):
                return True

    return False

# to get the edges from file
edges = []
for i in range(3, len(lines)):
    edges.append(tuple(lines[i].replace('\n', '').split(' ')))

# to create graph which represents { node: [neighbors] }
graph = {}
for src, dest, weight in edges:
    if src not in graph:
        graph[src] = []
    if dest not in graph:
        graph[dest] = []
    graph[src].append((dest, weight))

# to check the cycle
has_cycle_result = has_cycle(graph)


# djikstra's algorithm is used which is efficient for both cyclic and acyclic graphs
shortest_distances = shortest_path(graph, str(start))
for key, value in shortest_distances.items():
    print(names[int(key)] + ':' , value)

