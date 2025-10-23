tree = {}        
utilities = {}   

n = int(input("Number of nodes in the game tree: "))
for i in range(n):
    node = input(f"Node name {i+1}: ")
    children = input(f"Children of {node} (space separated, leave empty if leaf): ").split()
    if children:
        tree[node] = children
    else:
        vals = list(map(int, input(f"Utility values of leaf node {node} (space separated): ").split()))
        utilities[node] = vals

def minimax(node, depth, path):
    if node in utilities:
        if depth % 2 == 0:   # Max
            chosen = max(utilities[node])
        else:                # Min
            chosen = min(utilities[node])
        return chosen, path + [f"{node}({chosen})"]

    # Max
    if depth % 2 == 0:
        best_val = -999999
        best_path = []
        for child in tree.get(node, []):
            val, new_path = minimax(child, depth + 1, path + [node])
            if val > best_val:
                best_val = val
                best_path = new_path
        return best_val, best_path

    # Min
    else:
        best_val = 999999
        best_path = []
        for child in tree.get(node, []):
            val, new_path = minimax(child, depth + 1, path + [node])
            if val < best_val:
                best_val = val
                best_path = new_path
        return best_val, best_path


root = input("Enter root node of the game tree: ")
value, decision_path = minimax(root, 0, [])
print(f"\nOptimal value at root '{root}': {value}")
print("Decision path:", " → ".join(decision_path))
