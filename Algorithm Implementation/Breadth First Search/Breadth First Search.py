graph = {}
n = int(input("Number of nodes: "))
for i in range(n):
    node = input(f"Node name {i+1}: ")
    graph[node] = input(f"Neighbors of {node}: ").split()

start = input("Start node: ")

def bfs(start):
    visited = []        
    queue = [start]     

    while queue:
        node = queue.pop(0)    
        if node not in visited:
            print(node, end=" ")
            visited.append(node)
            queue.extend(graph[node])  

bfs(start)