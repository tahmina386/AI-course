def dls(start, limit):
    visited = []                 
    stack = [(start, 0)] 

    while stack:
        node, depth = stack.pop()   
        if node not in visited:
            print(node, end=" ")
            visited.append(node)

            if depth < limit:
                for neighbor in reversed(graph[node]):
                    stack.append((neighbor, depth + 1))


graph = {}
n = int(input("Number of nodes: "))
for i in range(n):
    node = input(f"Node name {i+1}: ")
    graph[node] = input(f"Neighbors of {node}: ").split()

start = input("Start node: ")
limit = int(input("Limit: "))
dls(start, limit)
