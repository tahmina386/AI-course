This algorithm implements Beam Search.
________________________________________
**How the Algorithm Works**  

Beam Search is a heuristic search algorithm that is an optimization of Breadth-First Search (BFS) or Best-First Search (Greedy BFS). It restricts the number of states explored at each level of the search tree, aiming to find a good solution quickly while conserving memory.  
It uses a parameter called the beam width (k).  

The process is as follows:  
i.	Start the search with the root node at Level 0.  
ii.	For each subsequent level, the algorithm generates all successor nodes of the nodes kept from the previous level.  
iii.	**Evaluation**: Each successor node is evaluated using a heuristic function (h(n)), which estimates the cost from that node to the goal.  
iv.	**Pruning (The "Beam")**: The algorithm then prunes the list of successors, selecting only the k most promising nodes (those with the lowest heuristic values) to form the current level's beam.  
v.	This process repeats level by level until the goal node is reached or the search terminates.  
Beam Search sacrifices completeness (it might miss the goal even if reachable) and optimality (it does not guarantee the shortest path) for significant improvements in time and space efficiency due to the fixed, limited number of nodes explored at each level.
________________________________________
**Applications of Beam Search**  

Beam Search is widely used in problems where the search space is vast, and a quick, near-optimal solution is highly valued over a guaranteed optimal solution.  
i.	**Sequence-to-Sequence Models (NLP)**: It's the standard decoding algorithm in many Natural Language Processing tasks, such as Machine Translation and Image Captioning, to generate the most probable sequence of words.  
ii.	**Speech Recognition**: Used to find the most likely sequence of phonemes or words given an acoustic signal.  
iii.	**Pattern Recognition**: Applied in various domains for efficient exploration of potential matches or states.
________________________________________
**Complexity**  

The complexity of Beam Search is significantly better than a full Best-First Search, provided the beam width k is small. k is the beam width, b is the branching factor, and d is the depth of the solution.  
i.	**Time Complexity**: Since only k nodes are kept at each depth, and each has at most b successors, the time spent per level is largely dominated by generating successors (O(k . b)) and sorting the k . b  candidates (O(k . b log(k . b))). For practical purposes where b is often included in the constant factor, the time is often cited as $\mathbf{O(d \cdot k \cdot \log k)}$.  
ii.	**Space Complexity**: Only the nodes in the current beam and their immediate successors need to be stored, resulting in a linear space complexity of $\mathbf{O(d \cdot k)}$, which is a major advantage over exponential complexity algorithms.
________________________________________
**Screenshots of the Game**  

**INPUT**  
<img src="Screenshot 2025-10-27 005238.png" width="450"/>  

**OUTPUT**  
<img src="Screenshot 2025-10-27 005247.png" />
