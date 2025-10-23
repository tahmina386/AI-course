def best_fs(graph, start, goal, heuristic):
    queue = [(heuristic[start], start)]   # (heuristic value, node)
    path = ""

    while queue:
        print("OPEN:", queue)

        queue = sorted(queue)
        cost,node = queue[0]
        queue = queue[1:]

        print("Visiting:", node)
        path = path + node + " "

        if node == goal:
            print("Goal found:", node)
            print("Path:", path)
            return

        for neigh in graph[node]:
            if neigh not in path:   
                queue.append((heuristic[neigh], neigh))

graph = {}
heuristic = {}

n = int(input("How many nodes? "))

for i in range(n):
    node = input("Node name: ")
    neighbors = input("Neighbors of " + node + ": " ).split()
    graph[node] = neighbors
    h = int(input("Heuristic of " + node + ": "))
    heuristic[node] = h

start = input("Start node: ")
goal = input("Goal node: ")

best_fs(graph, start, goal, heuristic)