This algorithm implements Depth-Limited Search (DLS). 
________________________________________
**How the Algorithm Works**  

Depth-Limited Search (DLS) is an uninformed search algorithm that behaves identically to Depth-First Search (DFS) but with an added constraint: a depth limit (limit). The search is not allowed to explore any path that is deeper than this specified limit.  

The process for this iterative implementation is:  
I.	Start by pushing the start node and its current depth (0) onto the stack.  
II.	While the stack is not empty:  
&nbsp;&nbsp;&nbsp;&nbsp;i.	Pop the top (node, depth) pair from the stack.  
&nbsp;&nbsp;&nbsp;&nbsp;ii.	If the node hasn't been visited:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;->	Visit and process the node (e.g., print it).  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;->	Mark the node as visited.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;->	**Check the Limit**: If the current depth is less than the limit, push all of the node's unvisited neighbors onto the stack, assigning them a depth of depth + 1.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;->	If the depth equals the limit, the node is not expanded further, effectively cutting off the search at that depth.  
DLS avoids the potential non-termination problem of standard DFS in graphs with cycles or infinite depth, but it is incomplete if the shallowest goal state is beyond the depth limit.
________________________________________
**Applications of DLS**  

DLS is primarily used when there is a reasonable suspicion or knowledge of the depth at which the solution lies. Its applications include:  
i.	**As a Component of Iterative Deepening Depth-First Search (IDDFS)**: This is the most common use. IDDFS calls DLS repeatedly, incrementing the limit in each iteration (from 0 up to a maximum depth).  
ii.	**Searches in Defined Structures**: Used in games or problems where the solution space has a known maximum depth, or where extremely deep paths are unlikely to yield a good solution.  
iii.	**Bounded Searches**: Where computational resources (time/memory) are strictly constrained, preventing an infinite search.
________________________________________
**Complexity**  

The complexity of DLS is similar to DFS but is restricted by the limit (L) instead of the full depth of the graph. V is the number of vertices and E is the number of edges.  
i.	**Time Complexity (O(b^L))**: The algorithm explores a tree structure up to depth L. b is the branching factor (the average number of neighbors per node). In a worst-case graph scenario using an Adjacency List, the complexity is $O(V_{L} + E_{L})$, where $V_{L}$ and $E_{L}$ are the number of vertices and edges within the limit L. The exponential complexity ($b^L$) is often cited for tree-based searches and is a simpler way to represent the time spent.  
ii.	**Space Complexity (O(b x L))**: This is linear with respect to the limit. The maximum size of the stack is bounded by the branching factor (b) times the limit (L).  
________________________________________
**Screenshots of the Game**  

**INPUT**  
<img src="Screenshot 2025-10-27 004435.png" width="300"/>  

**OUTPUT**  
<img src="Screenshot 2025-10-27 004442.png" />
