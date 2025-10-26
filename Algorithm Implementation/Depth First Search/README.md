This algorithm implements Depth-First Search (DFS). 
________________________________________
**How the Algorithm Works**  

Depth-First Search (DFS) is an algorithm for traversing or searching tree or graph data structures. The algorithm starts at the root (or any arbitrary node) and explores as far as possible along each branch before backtracking. It is called "depth-first" because it favors moving deeper into the graph structure whenever possible.  
It typically uses a stack data structure (or recursion, which uses the system call stack) to keep track of the nodes to visit.  

The process for this iterative implementation is:  
I.	Start by putting the start node onto the stack.  
II.	While the stack is not empty:  
&nbsp;&nbsp;&nbsp;&nbsp;i.	Pop the top node from the stack.  
&nbsp;&nbsp;&nbsp;&nbsp;ii.	If the node has not been visited:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-> Visit and process the node (e.g., print it).  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-> Mark the node as visited.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-> Push all of its unvisited neighbors onto the stack. The neighbors are typically pushed in reverse order so that when popped, they are processed in a consistent order.  
The use of the stack ensures that the algorithm always explores the most recently added neighbor before its parent's other neighbors.  
________________________________________
**Applications of DFS**  

DFS is a versatile algorithm with many applications in computer science, including:  
i.	**Path Finding**: Determining if a path exists between two nodes in a graph.  
ii.	**Topological Sorting**: Ordering the nodes of a directed acyclic graph (DAG) in a linear way (e.g., in task scheduling).  
iii.	**Finding Connected Components**: Identifying all nodes reachable from a given node.  
iv.	**Solving Puzzles**: Such as mazes, by exploring one path fully before trying the next.  
v.	**Cycle Detection**: Detecting cycles in a graph.  
________________________________________
**Complexity**  

**Time Complexity**:  
The time complexity of algorithms like Depth-First Search (DFS) depends on how the graph is structured and represented:  
i.	**Adjacency List Representation**: The complexity is O(V + E), where V is the number of vertices (nodes) and E is the number of edges. This is efficient because to find all neighbors of a vertex, we only look at the edges actually connected to it. Every vertex is processed once, and every edge is examined once.  
ii.	**Adjacency Matrix Representation**: The complexity is O(V^2). In this representation, checking the neighbors of a single vertex requires iterating through an entire row (or column) of the V x V matrix, which takes O(V) time. Since every vertex is processed, the total time is V x O(V) = O(V^2). This is less efficient for sparse graphs (graphs with few edges) but can be preferred for dense graphs (graphs with many edges).  

**Space Complexity**:  
O(V) is required to store the visited set (or list) and the stack.
________________________________________
**Screenshots of the Game**  

**INPUT**  
<img src="Screenshot 2025-10-27 003707.png" width="450"/>  

**OUTPUT**  
<img src="Screenshot 2025-10-27 003711.png"/>
