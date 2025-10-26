The code implements the Bidirectional Search algorithm.
________________________________________
**How the Algorithm Works**  
The Bidirectional Search is a graph search algorithm designed to find the shortest path between a start node and a goal node in an unweighted graph. It achieves efficiency by performing two simultaneous, independent BFS searches:  
i.	**Forward Search**: Starts from the start node and moves toward the goal.  
ii.	**Backward Search**: Starts from the goal node and moves toward the start.  
The search expands one level alternately from both directions until a meeting point (a common node) is found. This convergence confirms that a path exists.  

**Key Mechanism:**  
i.	**Queues**: Two separate queues (qstart and qgoal) manage the nodes to be expanded for each search direction.  
ii.	**Traversal Trees/Parent Pointers**: Two dictionaries (tstart and tgoal) store the parent of each visited node, allowing the path to be traced back from the meeting node to the respective start/goal nodes.  
iii.	**Path Construction**: Once the meeting node is found, the final path is created by reversing the backward trace from the start search and concatenating it with the forward trace from the goal search.  
________________________________________
**Applications of the Algorithm**  
Bidirectional search is highly effective in scenarios where the branching factor of the search space is high and the goal is known. Its primary applications include:  
I.	**Shortest Path Finding**: Crucial in network routing protocols, geographical mapping, and navigation systems where the shortest distance (in terms of hops/edges) is needed.  
II.	**Game AI and Puzzles**: Solving state-space problems like the 15-puzzle or determining minimum moves in certain board games by working simultaneously from the initial and final states.  
III.	**Social Network Analysis**: Efficiently determining the degrees of separation (shortest link) between two individuals in a massive network.  
________________________________________
**Complexity**  
For a graph where a search space has a branching factor $b$ (average number of edges per node) and the distance (length of the shortest path) between the start and goal is $d$:  
I.	**Time Complexity**: $\mathbf{O(b^{d/2})}$  
II.	**Space Complexity**: $\mathbf{O(b^{d/2})}$  

The space complexity is also $\mathbf{O(b^{d/2})}$ because two queues and two visited sets (or traversal trees) must be maintained for the nodes explored by both searches.
________________________________________
**Screenshots of the Game**  

**INPUT**  
<img src="Screenshot 2025-10-27 003404.png" width="300"/>  

**OUTPUT**  
<img src="Screenshot 2025-10-27 003410.png"/>
