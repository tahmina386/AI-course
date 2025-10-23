graph = {}
n = int(input("Number of nodes: "))
for i in range(n):
    node = input(f"Node name {i+1}: ")
    graph[node] = input(f"Neighbors of {node}: ").split()

start = input("Start node: ")
goal = input("Goal node: ")
limit = int(input("Limit: "))

# Depth Limited Search (Recursive with Traversed Tracking)
def dls_recursive(node, goal, limit, traversed, path):
    traversed.append(node)  

    if node == goal:
        return path + [node]

    if limit <= 0:
        return None

    for neighbor in graph[node]:
        result = dls_recursive(neighbor, goal, limit - 1, traversed, path + [node])
        if result:
            return result

    return None

# Iterative Deepening Search (Recursive DLS ব্যবহার করে)
def ids_recursive(start, goal, max_depth):
    for depth in range(max_depth + 1):
        traversed = []
        print(f"\n Depth Limit = {depth}")
        path = dls_recursive(start, goal, depth, traversed, [])
        print("Traversed Nodes:", traversed)
        if path:
            print("Goal Found! Path =", path)
            return path
    print("\nGoal not found within given depth")
    return None

ids_recursive(start, goal, limit)