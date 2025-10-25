**Tic Tac Toe (Minimax AI)**  

This is a classic 3x3 game of Tic Tac Toe where the Human player ("X") competes against an optimal AI opponent ("O"). The AI utilizes the Minimax algorithm to ensure it never loses a game (it will either win or draw).  

___________________________________

**How to Run the File**  

1.	Save the Code: Save the Python code (e.g., tic_tac_toe_minimax.py) to your local machine.  
2.	Execute: Open your terminal or command prompt, navigate to the directory where you saved the file, and run the following command:  
3.	python tic_tac_toe_minimax.py

___________________________________

**Required Software/Library/Framework**  

1.	**Python**: You must have Python 3 installed on your system.  
2.	**Pygame**: This game requires the Pygame library for the graphical interface. You must install it before running:  
<p align=center><b>pip install pygame</b></p>  

___________________________________

**How to Play the Game**  

1.	**Objective**: Get three of your marks ("X") in a row, column, or diagonal before the AI ("O") does.  
2.	**Players**:  
a.	**Human**: Plays as "X" and goes first.  
b.	**AI**: Plays as "O" and goes second.  
3.	**Moves**: Use your mouse to click on any empty cell on the 3x3 grid to place your "X".  
4.	**Gameplay**: After you make a move, the AI will calculate and place its "O" mark automatically.  

___________________________________

**Algorithm Used**  

The AI for this game employs the Minimax Algorithm.  

**Minimax in Tic Tac Toe**  
Since Tic Tac Toe is a fully solved game with a small game tree, Minimax can be used to achieve perfect play:  
1.	**Utility Scores**:  
a.	+1: Win for the AI ("O").  
b.	-1: Win for the Human ("X").  
c.	0: Draw.  
2.	**Maximizing Player (AI / "O")**: The AI explores possible moves and chooses the one that maximizes the resulting score (aims for +1).  
3.	**Minimizing Player (Human / "X")**: The algorithm assumes the human will play optimally to minimize the AI's score (aims for -1).  
4.	**Perfection**: Because the Minimax algorithm explores all terminal states, the AI is guaranteed to find a move that leads to a win or, at worst, a draw. The Human player can only win if the AI makes an implementation error or if the Human is given a forced-win starting position (which is not the case here).
