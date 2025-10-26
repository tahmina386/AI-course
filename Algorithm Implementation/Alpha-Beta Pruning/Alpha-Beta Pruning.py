tree = {}        # adjacency list for game tree
utilities = {}   # leaf node utilities

n = int(input("Number of nodes in the game tree: "))
for i in range(n):
    node = input(f"Node name {i+1}: ")
    children = input(f"Children of {node} (space separated, leave empty if leaf): ").split()
    if children:
        tree[node] = children
    else:
        vals = list(map(int, input(f"Utility values of leaf node {node} (space separated): ").split()))
        utilities[node] = vals

pruned_nodes = []
prune_count = 0

def alphabeta(node, depth, alpha, beta):
    global prune_count, pruned_nodes

    if node in utilities:
        chosen = max(utilities[node]) if depth % 2 == 0 else min(utilities[node])
        return chosen, [f"{node}({chosen})"]

    if depth % 2 == 0:  # Max node
        best_val = float('-inf')
        best_path = []
        for i, child in enumerate(tree[node]):
            val, path = alphabeta(child, depth + 1, alpha, beta)
            if val > best_val:
                best_val = val
                best_path = [node] + path
            alpha = max(alpha, best_val)
            if beta <= alpha:
                pruned = tree[node][i+1:]
                pruned_nodes.extend(pruned)
                prune_count += len(pruned)
                break
        return best_val, best_path
    else:  # Min node
        best_val = float('inf')
        best_path = []
        for i, child in enumerate(tree[node]):
            val, path = alphabeta(child, depth + 1, alpha, beta)
            if val < best_val:
                best_val = val
                best_path = [node] + path
            beta = min(beta, best_val)
            if beta <= alpha:
                pruned = tree[node][i+1:]
                pruned_nodes.extend(pruned)
                prune_count += len(pruned)
                break
        return best_val, best_path

root = input("Enter root node of the game tree: ")
value, decision_path = alphabeta(root, 0, float('-inf'), float('inf'))

print(f"\nOptimal value at root '{root}': {value}")
print("Decision path:", " → ".join(decision_path))
print("\nTotal prunings:", prune_count)
print("Pruned nodes:", ", ".join(pruned_nodes) if pruned_nodes else "None")
