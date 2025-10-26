This algorithm implements Iterative Deepening Search (IDS), which relies on the nested function for Depth-Limited Search (DLS). 
________________________________________
**How the Algorithm Works**  

Iterative Deepening Search (IDS) combines the benefits of Breadth-First Search (BFS)—completeness and optimality (for unweighted graphs)—with the memory efficiency of Depth-First Search (DFS).  
IDS works by repeatedly calling the Depth-Limited Search (DLS) algorithm, progressively increasing the depth limit in each iteration (starting from depth 0 up to a max_depth).  

The overall process is:  
I.	**Outer Loop (IDS)**: Start a loop that iterates over the depth limit, L = 0, 1, 2, . . . ., max_depth.  
II.	**Inner Search (DLS)**: In each iteration L, execute a full DLS search from the start node, restricted to paths of length L.  
III.	**Termination**:  
i.	If the goal is found at depth L, the search stops, and the path is returned. Since the depths are checked in increasing order, the first path found is guaranteed to be the shortest (optimal) path.  
ii.	If the loop completes without finding the goal up to max_depth, the goal is considered unreachable within that bound.  
Although IDS repeatedly regenerates the search tree at shallow depths, the majority of the work is done in the deepest level (where the solution is typically found), making the overall time complexity close to that of a single BFS or DFS at the goal depth.  
________________________________________
**Applications of IDS**  

IDS is highly effective in large search spaces where the depth of the solution is unknown. Its applications include:  
i.	**Shortest Path Finding (Unweighted Graphs)**: Guarantees finding the shortest path to a goal, making it an optimal search algorithm.  
ii.	**Game Tree Searching**: Used in game AI (e.g., chess, checkers) when combined with evaluation functions, allowing for deeper searches given time constraints.  
iii.	**General State-Space Search**: Used as a standard, reliable algorithm in Artificial Intelligence problems when memory is limited.
________________________________________
**Complexity**  

The complexity of IDS is analyzed relative to b (the branching factor) and d (the depth of the shallowest goal).  
i.	**Time Complexity (O(b^d))**: Despite repeated searches, the time complexity is dominated by the searches at the deepest level. The total number of nodes visited is about 1.2 times the number of nodes visited by a single BFS/DFS, which is asymptotically equivalent to $\mathbf{O(b^d)}$.  
ii.	**Space Complexity (O(b \times d))**: Because it only performs DLS at each iteration, the maximum number of nodes stored on the call stack (or the explicit stack for an iterative DLS) is linear with respect to the depth limit $\mathbf{O(b \times d)}$. This memory efficiency is a major advantage over BFS.
________________________________________
**Screenshots of the Game**  

**INPUT**  
<img src="Screenshot 2025-10-27 004926.png" width="450"/>  

**OUTPUT**  
<img src="Screenshot 2025-10-27 004938.png" />
