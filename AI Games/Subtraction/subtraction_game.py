import tkinter as tk
from tkinter import messagebox
import math
# os and sys imports were removed as they were not present in your provided code block, maintaining strict adherence to your request.

# ----------------- Minimax Algorithm -----------------
def minimax(stones, is_maximizing):
    """
    The core recursive function for the Minimax algorithm.
    It evaluates the utility of a game state assuming both players play optimally.

    Args:
        stones (int): The number of stones currently remaining.
        is_maximizing (bool): True if this is the AI's turn (Maximizing player), 
                              False if it is the Human's turn (Minimizing player).

    Returns:
        int: The utility score of the state (1 for AI win, -1 for AI loss).
    """
    # Base case: No stones left (Game Termination)
    if stones == 0:
        if is_maximizing:
            # If AI was supposed to move, but there are 0 stones, the opponent (Human) won the previous turn.
            return -1   # AI lost (Score: -1)
        else:
            # If Human was supposed to move, but there are 0 stones, the AI won the previous turn.
            return 1    # AI won (Score: 1)

    scores = [] # List to store the Minimax result for every possible move from this state

    # Iterate through all legal moves: 1, 2, or 3 stones
    for move in [1, 2, 3]:
        # Check if the move is legal (stones remaining must be non-negative)
        if stones - move >= 0:
            # Recursively call minimax for the opponent's perspective (maximizing vs. minimizing)
            next_score = minimax(stones - move, not is_maximizing)
            scores.append(next_score)

    # --- Recursive Step: Choose the optimal score ---
    # Instead of best_score = ... return ..., we use simpler logic:
    if is_maximizing:
        # If it's the AI's turn, choose the move that leads to the highest possible score (max(1))
        return max(scores)
    else:
        # If it's the Human's turn, assume they will choose the move that leads to the lowest score (min(-1)) for the AI
        return min(scores)

def ai_move(stones):
    """
    Calculates the best immediate move for the AI using the minimax function.

    Args:
        stones (int): The current number of stones.

    Returns:
        int: The optimal number of stones (1, 2, or 3) to remove.
    """
    best_score = -math.inf # Initialize best score to negative infinity
    best_move = 1          # Default best move

    # Evaluate each possible move (1, 2, or 3)
    for move in [1, 2, 3]:
        if stones - move >= 0:
            # Determine the score resulting from this move, assuming the next player (Human, minimizing) plays optimally
            score = minimax(stones - move, False)
            
            # Check if this move results in a better outcome (higher score) for the AI
            if score > best_score:
                best_score = score
                best_move = move

    # Return the move that leads to the highest minimax score (i.e., a guaranteed win, if possible)
    return best_move
    
# ----------------- Game Logic -----------------
stones = 25 # Initial number of stones for the game

def update_stones_display():
    """
    Redraws the canvas to visually represent the remaining number of stones in a grid pattern.
    """
    canvas.delete("all") # Clear previous drawings
    
    # Draw stones in a 5-column grid pattern
    for i in range(stones):
        # Calculate X and Y coordinates for the stone (i % 5 for column, i // 5 for row)
        x = 20 + (i % 5) * 60
        y = 20 + (i // 5) * 60
        
        # Alternate colors for visual distinction
        color = "#FF6F61" if i % 2 == 0 else "#6B5B95"
        
        # Create the stone circle (oval)
        canvas.create_oval(x, y, x + 50, y + 50, fill=color, outline="#333", width=2)
        
        # Add a number inside the stone for counting (shows the current index/count)
        canvas.create_text(x + 25, y + 25, text=str(stones - i), fill="white", font=("Helvetica", 14, "bold"))

def player_move(move):
    """
    Processes the move chosen by the human player.
    
    Args:
        move (int): The number of stones (1, 2, or 3) the player chose to remove.
    """
    global stones
    
    # 1. Input Validation
    if move > stones:
        messagebox.showwarning("Invalid Move", "Not enough stones!")
        return

    # 2. Update game state
    stones -= move
    update_stones_display()

    # 3. Check for Human Win Condition (Human took the last stone)
    if stones == 0:
        messagebox.showinfo("Game Over", "You win! 🎉")
        root.destroy() # Close the application window
        return

    # 4. Schedule AI's turn after a short delay (for visual effect)
    root.after(500, ai_turn)

def ai_turn():
    """
    Executes the move determined by the AI (Minimax algorithm).
    """
    global stones
    
    # 1. Calculate optimal move
    move = ai_move(stones)
    
    # 2. Update game state
    stones -= move
    update_stones_display()
    
    # 3. Update status label to show AI's move
    ai_label.config(text=f"AI removed {move} stone{'s' if move > 1 else ''}")

    # 4. Check for AI Win Condition (AI took the last stone)
    if stones == 0:
        messagebox.showinfo("Game Over", "AI wins! 🤖")
        root.destroy() # Close the application window
        return
        
# ----------------- GUI Setup -----------------
# 1. Initialize the main Tkinter window
root = tk.Tk()
root.title("Subtraction Game")
root.configure(bg="#2C3E50") # Set dark blue background

# 2. Title Label
title_label = tk.Label(root, text="Subtraction Game", font=("Helvetica", 24, "bold"), fg="white", bg="#2C3E50")
title_label.pack(pady=20)

# 3. Canvas for displaying stones
canvas = tk.Canvas(root, width=350, height=325, bg="#34495E", highlightthickness=0)
canvas.pack(pady=20)
update_stones_display() # Initial draw of stones

# 4. Status Label (for displaying AI move/game status)
ai_label = tk.Label(root, text="", font=("Helvetica", 16, "bold"), fg="#F1C40F", bg="#2C3E50")
ai_label.pack(pady=5)

# 5. Frame for move buttons
buttons_frame = tk.Frame(root, bg="#2C3E50")
buttons_frame.pack(pady=10)

# 6. Define button style dictionary
btn_style = {
    "font": ("Helvetica", 16, "bold"), 
    "bg": "#1ABC9C", 
    "fg": "white", 
    "width": 10, 
    "height": 2, 
    "bd": 0, 
    "activebackground": "#16A085"
}

# 7. Create and place move buttons (Remove 1, 2, 3)
for i in [1, 2, 3]:
    # Use lambda to pass the specific move value to the player_move function when clicked
    btn = tk.Button(buttons_frame, text=f"Remove {i}", **btn_style, command=lambda x=i: player_move(x))
    btn.grid(row=0, column=i - 1, padx=15, pady=10)

# 8. Start the Tkinter event loop
root.mainloop()
