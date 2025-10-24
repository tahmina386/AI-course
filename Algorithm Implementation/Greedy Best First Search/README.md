This algorithm implements Best-First Search (BFS), also known as Greedy Best-First Search.
________________________________________
**How the Algorithm Works:**  

Best-First Search (BFS) is an informed search algorithm that uses a heuristic function (h(n)) to guide its search. It explores the node that appears to be closest to the goal first, based on the heuristic value. It is considered "greedy" because it only focuses on the immediate estimate of the cost to the goal, ignoring the path cost taken so far.  

The process for this implementation is:  
I.	Initialize a priority queue (or a list that is repeatedly sorted, as in this code) with the starting node, prioritized by its heuristic value, h(start).  
II.	While the queue is not empty:  
&nbsp;&nbsp;&nbsp;&nbsp;i.	**Select the "best" node**: Extract the node from the queue that has the lowest heuristic value. This is the node estimated to be closest to the goal.  
&nbsp;&nbsp;&nbsp;&nbsp;ii.	**Check for Goal**: If the extracted node is the goal, the search is complete.  
&nbsp;&nbsp;&nbsp;&nbsp;iii.	**Expand the Node**: For each unvisited neighbor of the current node:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;->	Calculate its heuristic value, h(neighbor).  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;->	Add the neighbor and its heuristic value to the queue.  
This greedy approach leads the search straight to the goal if the heuristic is accurate, but it can easily get stuck in a local minimum or find a suboptimal (non-shortest) path if the heuristic is misleading.  
________________________________________
**Applications of Best-First Search**  

Greedy Best-First Search is useful in scenarios where a quick, possibly non-optimal, solution is acceptable or necessary. Its applications include:  
i.	**Heuristic Pathfinding**: Used in games and robotics for fast path generation when finding the absolute shortest path is not the top priority.  
ii.	**Search Optimization**: As an alternative to uninformed searches in large state spaces where only an estimate is available.  
iii.	**Initial State Estimation**: Can provide a quick, decent path to serve as a baseline or initial estimate for more sophisticated algorithms like A*.  
________________________________________
**Complexity**  

The complexity of Best-First Search is highly dependent on the quality of the heuristic function, h(n). b is the branching factor (average number of successors) and d is the depth of the solution.  
i. **Time Complexity (O(b^m))**: In the worst case, the search might explore the entire state space up to depth $m$ (the maximum depth). However, with a good heuristic, the search is often much faster, closer to $\mathbf{O(b^d)}$, which is the complexity of finding a goal at depth d.  
ii. **Space Complexity (O(b^m))**: In the worst case, the algorithm must store all generated nodes in the queue, leading to exponential space consumption. This is a primary drawback, similar to Depth-First Search.  
