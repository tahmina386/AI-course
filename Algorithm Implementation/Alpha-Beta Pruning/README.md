The code implements the Alpha-Beta Pruning algorithm, a search algorithm used primarily for two-player game trees.
________________________________________
**How the Algorithm Works:**  
The Alpha-Beta Pruning algorithm is an optimization technique for the Minimax Algorithm, which is used to determine the optimal move for a player in a two-player game (like chess, tic-tac-toe, etc.), assuming the opponent also plays optimally.  

**Minimax Principle**  
Minimax explores the game tree to a certain depth:  
i.	Max Player: Tries to maximize the utility (score/payoff).  
ii.	Min Player: Tries to minimize the utility (which is equivalent to maximizing the opponent's loss).  

**Alpha-Beta Optimization**  
Alpha-Beta Pruning eliminates branches of the search tree that cannot possibly influence the final decision, thus speeding up the search significantly. It maintains two values, alpha and beta:  
i.	$\alpha$ (Alpha): The best (highest-value) choice found so far for the Max player along the path from the root to the current node. Initialized to $-\infty$.  
ii.	$\beta$ (Beta): The best (lowest-value) choice found so far for the Min player along the path from the root to the current node. Initialized to $+\infty$.  

**The Pruning Rules**  
i.	Beta Pruning (Max Node): If, at a Max node, the current best value for the Max player ($\alpha$) is greater than or equal to the current best value for the Min player ($\beta$), the remaining children of this Max node are pruned. This is because the Min player at the parent node (or any ancestor Min node) is already guaranteed a move that results in a value of $\beta$ or less, and Max cannot possibly force a better outcome than $\beta$ from this node. Condition: $\beta <= \alpha$ (in the Max player's loop).  
ii.	Alpha Pruning (Min Node): If, at a Min node, the current best value for the Max player ($\alpha$) is greater than or equal to the current best value for the Min player ($\beta$), the remaining children of this Min node are pruned. This is because the Max player at the parent node (or any ancestor Max node) is already guaranteed a move that results in a value of $\alpha$ or more, and Min cannot possibly force a worse outcome (for Max) than $\alpha$ from this node. Condition: $\beta >= \alpha$ (in the Min player's loop).  
By passing $\alpha$ and $\beta$ down through the recursive calls, the algorithm avoids exploring large subtrees, making it much more efficient than plain Minimax.  
________________________________________
**Applications of the Algorithm:**  
The primary application of Alpha-Beta Pruning is in Artificial Intelligence for Games.  
i.	Board Games: It's extensively used in AI for complex two-player, perfect-information games like Chess, Checkers, Go, Othello (Reversi), and Shogi.  
ii.	Strategic Decision Making: It can be adapted for any scenario that involves alternating choices with an objective to maximize one's own utility while minimizing the opponent's.  
iii.	Adversarial Search: It forms the basis for searching in any zero-sum adversarial environment where opponents have conflicting goals.  
________________________________________
**Complexity:**  
The time complexity of the Minimax algorithm is $O(b^d)$, where $b$ is the branching factor (average number of legal moves from any position) and $d$ is the depth of the search.  
The Alpha-Beta Pruning algorithm, in the best-case scenario (when the best moves are searched first), reduces the effective branching factor from $b$ to approximately $\sqrt{b}$.  
i.	Best-Case Complexity (Perfect Ordering): $O(b^{d/2})$ or $O(\sqrt{b^d})$  
ii.	Worst-Case Complexity (No Pruning): $O(b^d)$ (Same as Minimax)  
In practice, with good move ordering heuristics, the performance gain is substantial, effectively allowing the search to explore twice the depth in the same amount of time compared to standard Minimax.

