import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# --- Configuration Constants ---
WIDTH, HEIGHT = 300, 300
LINE_WIDTH = 5
CELL_SIZE = WIDTH // 3 # 100 pixels per cell
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe - Human vs AI (Minimax)")
# Define font for displaying X's and O's and results
FONT = pygame.font.SysFont("arial", 60)

# --- Colors ---
WHITE = (255, 255, 255)
LINE_COLOR = (0, 0, 0)
X_COLOR = (200, 0, 0) # Red
O_COLOR = (0, 0, 200) # Blue (AI's color)

# --- Game State ---
# 3x3 list to represent the board. "" = empty, "X" = Human, "O" = AI
board = [["" for _ in range(3)] for _ in range(3)]

def draw_board():
    """Draws the game board and the current state of X's and O's."""
    screen.fill(WHITE)
    
    # Draw grid lines
    for i in range(1, 3):
        # Horizontal lines
        pygame.draw.line(screen, LINE_COLOR, (0, i * CELL_SIZE), (WIDTH, i * CELL_SIZE), LINE_WIDTH)
        # Vertical lines
        pygame.draw.line(screen, LINE_COLOR, (i * CELL_SIZE, 0), (i * CELL_SIZE, HEIGHT), LINE_WIDTH)
        
    # Draw X's and O's on the board
    for r in range(3):
        for c in range(3):
            if board[r][c] == "X":
                # Render and center the 'X' text
                text = FONT.render("X", True, X_COLOR)
                screen.blit(text, text.get_rect(center=(c * CELL_SIZE + CELL_SIZE // 2, r * CELL_SIZE + CELL_SIZE // 2)))
            elif board[r][c] == "O":
                # Render and center the 'O' text
                text = FONT.render("O", True, O_COLOR)
                screen.blit(text, text.get_rect(center=(c * CELL_SIZE + CELL_SIZE // 2, r * CELL_SIZE + CELL_SIZE // 2)))
    
    pygame.display.flip() # Update the full screen surface

def check_winner():
    """Checks the current board state for a winner (X or O)."""
    # Check rows and columns
    for i in range(3):
        # Check rows
        if board[i][0] == board[i][1] == board[i][2] != "":
            return board[i][0]
        # Check columns
        if board[0][i] == board[1][i] == board[2][i] != "":
            return board[0][i]
            
    # Check primary diagonal (top-left to bottom-right)
    if board[0][0] == board[1][1] == board[2][2] != "":
        return board[0][0]
        
    # Check secondary diagonal (top-right to bottom-left)
    if board[0][2] == board[1][1] == board[2][0] != "":
        return board[0][2]
        
    return None # No winner yet

def is_full():
    """Checks if all cells on the board are filled (indicating a draw, if no winner)."""
    # Returns True if every cell in every row is not an empty string
    return all(cell != "" for row in board for cell in row)

# ----------------- Minimax Algorithm -----------------

def minimax(is_maximizing):
    """
    The Minimax core function. Recursively evaluates game states to find the optimal score.
    
    The AI ("O") maximizes its score (+1 for win), the Human ("X") minimizes the score (-1 for win).
    
    Args:
        is_maximizing (bool): True if looking for the maximizing player's best move ("O"), 
                              False if looking for the minimizing player's best move ("X").

    Returns:
        int: The utility score (1 for O win, -1 for X win, 0 for draw).
    """
    # Base Case: Game is Over (Terminal States)
    winner = check_winner()
    if winner == "O": return 1  # AI Win
    if winner == "X": return -1 # Human Win
    if is_full(): return 0      # Draw

    if is_maximizing:
        # Maximizing Player ("O", the AI)
        best = -math.inf
        for r in range(3):
            for c in range(3):
                if board[r][c] == "":
                    # 1. Make the move (try the state)
                    board[r][c] = "O"
                    # 2. Recurse for the opponent (minimizing)
                    score = minimax(False)
                    # 3. Undo the move (backtrack)
                    board[r][c] = ""
                    # 4. Update the best score
                    best = max(score, best)
        return best
    else:
        # Minimizing Player ("X", the Human)
        best = math.inf
        for r in range(3):
            for c in range(3):
                if board[r][c] == "":
                    # 1. Make the move (try the state)
                    board[r][c] = "X"
                    # 2. Recurse for the opponent (maximizing)
                    score = minimax(True)
                    # 3. Undo the move (backtrack)
                    board[r][c] = ""
                    # 4. Update the best score
                    best = min(score, best)
        return best

def ai_move():
    """
    Calculates the best move for the AI ("O") by checking the Minimax score for every possible empty cell.
    """
    best_score = -math.inf
    move = None # Stores the (row, col) tuple of the optimal move
    
    for r in range(3):
        for c in range(3):
            if board[r][c] == "":
                # 1. Try the AI move
                board[r][c] = "O"
                # 2. Calculate the score assuming the opponent (Minimizer) moves next
                score = minimax(False)
                # 3. Undo the trial move
                board[r][c] = ""
                
                # 4. Choose the move that yields the highest score (closest to 1)
                if score > best_score:
                    best_score = score
                    move = (r, c)
    
    # Execute the best move found
    if move:
        board[move[0]][move[1]] = "O"

# ----------------- Game Loop and Presentation -----------------

def show_result(winner):
    """Displays the final game result (Win, Loss, or Draw) on the screen."""
    screen.fill(WHITE)
    
    if winner is None:
        msg = "Draw!"
    elif winner == "O":
        msg = "AI (O) wins! 🤖"
    else: # winner == "X"
        msg = "Human (X) wins! 🎉"
        
    # Render message centered
    text = FONT.render(msg, True, LINE_COLOR)
    screen.blit(text, text.get_rect(center=(WIDTH // 2, HEIGHT // 2)))
    pygame.display.flip()
    
    # Wait for a few seconds before quitting
    pygame.time.wait(3000)

def main():
    """The main game loop."""
    running = True
    player_turn = True # Human ("X") starts first
    
    while running:
        draw_board()
        
        # Check for game end conditions
        winner = check_winner()
        if winner or is_full():
            show_result(winner)
            running = False
            continue

        # --- Event Handling ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            # Handle Human Player's turn (Mouse Click)
            elif player_turn and event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                # Convert mouse coordinates to board indices
                row, col = y // CELL_SIZE, x // CELL_SIZE
                
                # Place 'X' if the cell is empty
                if board[row][col] == "":
                    board[row][col] = "X"
                    player_turn = False # Switch to AI's turn

        # Handle AI Player's turn
        if not player_turn and not check_winner() and not is_full():
            # Add a small delay for better user experience
            pygame.time.wait(300)
            ai_move()
            player_turn = True # Switch back to Human's turn

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
