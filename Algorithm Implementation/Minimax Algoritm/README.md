This algorithm implements the Minimax Algorithm.  
________________________________________
**How the Algorithm Works**  

The Minimax Algorithm is a decision-making and game theory algorithm used primarily in two-player, zero-sum games (where one player's gain is the other player's equal loss), such as chess, checkers, and Tic-Tac-Toe. It determines the optimal move for a player, assuming the opponent is also playing optimally.  
The algorithm searches the game tree, working recursively from the leaf nodes up to the current state (the root of the subtree being analyzed).  
1.	**Terminal State (Leaf Node) Evaluation**:  
Leaf nodes represent the final states of the game and have associated utility values (scores or payoffs). The code handles a multi-utility list at a leaf by having the Max player choose the highest value and the Min player choose the lowest value from that list.  
2.	**Minimizing Layer (Opponent's Move)**:  
At a Minimizing node (usually odd depth), the algorithm assumes the opponent will choose the move that results in the minimum possible score for the maximizing player. The node's value is the minimum of its children's values: Value = min(Children's Values).  
3.	**Maximizing Layer (Player's Move)**:  
At a Maximizing node (usually even depth, including the root), the algorithm assumes the player will choose the move that results in the maximum possible score. The node's value is the maximum of its children's values: Value = max(Children's Values).

The search continues until the root node is reached, yielding the optimal value and the sequence of moves (the decision path) that achieves it.
________________________________________
**Applications of Minimax**  

Minimax is the foundational algorithm for making decisions in deterministic environments with perfect information.  
1.	**Classic Board Games**: Chess, Checkers, Go, and variants of Tic-Tac-Toe.  
2.	**Game AI**: Used to implement non-human players that make "rational" or optimal moves within the constraints of the game tree depth.  
3.	**Decision Making**: Can be adapted for scenarios involving competitive decisions in business, economics, or any domain where an intelligent adversary is involved.
________________________________________
**Complexity**  

The complexity is dependent on the size and depth of the game tree.  
1.	**Time Complexity (O(b^d))**: The algorithm explores every node in the game tree up to the search depth d. b is the branching factor (the average number of legal moves from a state). Since b is often large (e.g., $b \approx 35$ for chess), the exponential complexity means the search depth must be limited in practice.  
2.	**Space Complexity (O(b x d))**: When implemented recursively (as shown), the space required is linear with the search depth, d, to store the recursion stack. This is generally manageable.

In practice, the Minimax algorithm is often enhanced with Alpha-Beta Pruning to drastically reduce the number of nodes explored while guaranteeing the same result. The complexity remains $O(b^d)$ in the worst case but is closer to $O(b^{d/2})$ with a good ordering of moves.
