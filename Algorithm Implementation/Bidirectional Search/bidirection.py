graph = {}
n = int(input("Number of nodes: "))
for i in range(n):
    node = input(f"Node name {i+1}: ")
    graph[node] = input(f"Neighbors of {node}: ").split()

start = input("Start node: ")
goal = input("Goal node: ")

def b_bfs(graph, start, goal):
    if start == goal:
        return [start]

    qstart = [start]
    qgoal = [goal]
    tstart = {start: None}
    tgoal = {goal: None}

    while qstart and qgoal:
        # expand from start side
        current = qstart.pop(0)
        for neigh in graph.get(current, []):
            if neigh not in tstart:
                tstart[neigh] = current
                qstart.append(neigh)
                if neigh in tgoal:
                    return build_path(neigh, tstart, tgoal)

        # expand from goal side
        current = qgoal.pop(0)
        for neigh in graph.get(current, []):
            if neigh not in tgoal:
                tgoal[neigh] = current
                qgoal.append(neigh)
                if neigh in tstart:
                    return build_path(neigh, tstart, tgoal)

    return None

def build_path(meet, tstart, tgoal):
    # path from start to meeting
    path_left = []
    node = meet
    while node is not None:
        path_left.append(node)
        node = tstart[node]
    path_left.reverse()

    # path from meeting to goal
    path_right = []
    node = tgoal[meet]
    while node is not None:
        path_right.append(node)
        node = tgoal[node]

    full_path = path_left + path_right
    print(" ".join(full_path))  # space separated output
    return full_path

b_bfs(graph, start, goal)