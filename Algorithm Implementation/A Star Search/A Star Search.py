graph = {}
heuristic = {}

n = int(input("Number of nodes: "))
for i in range(n):
    node = input(f"Node name {i+1}: ")
    graph[node] = {}
    neighbors = input(f"Neighbors of {node}: ").split()

    for neigh in neighbors:
        cost = int(input(f"Cost from {node} to {neigh}: "))
        graph[node][neigh] = cost
        
    h = int(input(f"Heuristic value for {node}: "))
    heuristic[node] = h

def a(start, goal):
    pq = [(heuristic[start], 0, start, [start])]
    visited = {}

    while pq:
        pq.sort(key=lambda x: x[0])   # sort by f
        f, g, node, path = pq.pop(0)

        if node in visited and visited[node] <= g:
            continue
        visited[node] = g

        print(f"Visiting: {node}, g={g}, h={heuristic[node]}, f={f}")

        if node == goal:
            print(f"\nGoal '{goal}' reached!")
            print("Path:", " → ".join(path))
            print("Total Cost (g):", g)
            return

        for neighbor, cost in graph[node].items():
            g_new = g + cost
            f_new = g_new + heuristic.get(neighbor, 999999)
            pq.append((f_new, g_new, neighbor, path + [neighbor]))

    print("\nGoal not reachable.")

start = input("Start node: ")
goal = input("Goal node: ")
a(start, goal)
