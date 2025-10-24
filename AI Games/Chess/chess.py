import pygame, sys, chess, math

# Initialize Pygame and set up constants
pygame.init()
WIDTH, HEIGHT = 640, 640
SQUARE_SIZE = WIDTH // 8
# Font for displaying the chess pieces (using Unicode symbols)
FONT = pygame.font.SysFont("segoeuisymbol", 48)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess - Player vs Computer (Minimax AI)")

# Define colors for the chessboard and highlights
WHITE_COLOR = (220, 220, 220)  # Light gray for light squares
BROWN = (70, 130, 180)         # Steel blue for dark squares
HIGHLIGHT = (255, 255, 0)      # Yellow for selected square
MOVE_HINT = (100, 255, 100)    # Green for legal move targets

# Dictionary mapping standard FEN piece symbols to Unicode characters
symbols = {
    "r": "♜", "n": "♞", "b": "♝", "q": "♛", "k": "♚", "p": "♟",
    "R": "♖", "N": "♘", "B": "♗", "Q": "♕", "K": "♔", "P": "♙"
}

# Simple material evaluation for the AI's heuristic function
piece_values = {
    chess.PAWN: 1,
    chess.KNIGHT: 3,
    chess.BISHOP: 3,
    chess.ROOK: 5,
    chess.QUEEN: 9,
    chess.KING: 0  # King's value is irrelevant in material evaluation, only important for checkmate
}

# ----------------------------------------------------------------------
# GRAPHICS AND INTERACTION FUNCTIONS
# ----------------------------------------------------------------------

def draw_board(board, selected_square=None, legal_moves=[]):
    """
    Draws the chessboard, pieces, highlights the selected square, and hints for legal moves.
    """
    for row in range(8):
        for col in range(8):
            # Calculate the rectangle for the current square
            rect = pygame.Rect(col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
            
            # Alternate colors for the board squares
            color = BROWN if (row + col) % 2 else WHITE_COLOR
            pygame.draw.rect(screen, color, rect)
            
            # Map Pygame coordinates (top-left is 0,0) to python-chess coordinates (bottom-left is a1)
            square = chess.square(col, 7 - row)
            
            # Highlight the currently selected piece
            if square == selected_square:
                pygame.draw.rect(screen, HIGHLIGHT, rect, 4)
            
            # Draw circles to indicate legal target squares for the selected piece
            elif square in legal_moves:
                pygame.draw.circle(screen, MOVE_HINT, rect.center, 10)
                
            # Draw the piece symbol if a piece is on the square
            piece = board.piece_at(square)
            if piece:
                # Render the Unicode symbol for the piece
                text = FONT.render(symbols[piece.symbol()], True, (0, 0, 0))
                text_rect = text.get_rect(center=rect.center)
                screen.blit(text, text_rect)
    pygame.display.flip()

def get_square_under_mouse(pos):
    """
    Converts mouse (x, y) coordinates to a python-chess square index (0 to 63).
    """
    x, y = pos
    col = x // SQUARE_SIZE
    row = y // SQUARE_SIZE
    # Inverse the row mapping (Pygame is top-down, Chess is bottom-up)
    return chess.square(col, 7 - row)

# ----------------------------------------------------------------------
# AI SEARCH ALGORITHM (MINIMAX WITH ALPHA-BETA PRUNING)
# ----------------------------------------------------------------------

def evaluate_board(board):
    """
    The heuristic function used by the AI. Calculates the material advantage.
    Positive scores favor White (Human), negative scores favor Black (Computer).
    """
    # Check for immediate game-ending states (Checkmate/Stalemate)
    if board.is_checkmate():
        # Assign a massive score to force the AI to choose a checkmate if available
        # If it's White's turn (board.turn), White was just mated (-9999).
        # If it's Black's turn (not board.turn), Black was just mated (+9999).
        return -9999 if board.turn else 9999
    elif board.is_stalemate() or board.is_insufficient_material():
        return 0 # Draw is neutral
        
    score = 0
    # Iterate through all 64 squares to sum up material
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece:
            value = piece_values[piece.piece_type]
            # Add value for White pieces, subtract value for Black pieces
            score += value if piece.color == chess.WHITE else -value
            
    return score

def minimax(board, depth, alpha, beta, maximizing):
    """
    The Minimax algorithm with Alpha-Beta Pruning.
    Finds the best move by recursively searching the game tree.
    
    :param board: The current chess board state (python-chess Board object).
    :param depth: How many more moves to look ahead.
    :param alpha: The best value (highest) found so far for the maximizing player.
    :param beta: The best value (lowest) found so far for the minimizing player.
    :param maximizing: True if it's the maximizing player's (White/Human) turn.
                       False if it's the minimizing player's (Black/AI) turn.
    :return: (evaluation_score, best_move)
    """
    # Base Case: Stop searching when depth limit is reached or the game is over.
    if depth == 0 or board.is_game_over():
        return evaluate_board(board), None

    best_move = None
    
    if maximizing:
        # MAX Player (Human, trying to maximize the score)
        max_eval = -math.inf
        for move in board.legal_moves:
            board.push(move) # Make the move
            eval, _ = minimax(board, depth - 1, alpha, beta, False) # Recurse for MIN
            board.pop()      # Undo the move (backtrack)
            
            if eval > max_eval:
                max_eval = eval
                best_move = move
                
            # Alpha-Beta Pruning: If the current MAX score is >= MIN's best score,
            # MIN will never allow this path, so we can stop searching this branch.
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval, best_move
        
    else:
        # MIN Player (AI, trying to minimize the score)
        min_eval = math.inf
        for move in board.legal_moves:
            board.push(move) # Make the move
            eval, _ = minimax(board, depth - 1, alpha, beta, True) # Recurse for MAX
            board.pop()      # Undo the move
            
            if eval < min_eval:
                min_eval = eval
                best_move = move
                
            # Alpha-Beta Pruning: If the current MIN score is <= MAX's best score,
            # MAX will never allow this path, so we can stop searching this branch.
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval, best_move

# ----------------------------------------------------------------------
# GAME CONTROL FUNCTIONS
# ----------------------------------------------------------------------

def ai_move(board):
    """
    Wrapper function to calculate and execute the AI's move (Black).
    The AI is the minimizing player (False for maximizing).
    Depth is currently set to 2 for reasonable performance.
    """
    # Call minimax, starting with a depth of 2 (can be increased for stronger play)
    # The initial alpha is -inf, and beta is +inf.
    _, move = minimax(board, 2, -math.inf, math.inf, False) 
    if move:
        board.push(move)

def promote_pawn(board, move):
    """
    Handles pawn promotion by promoting to a Queen by default.
    The python-chess library handles the move validation for the promotion.
    """
    # Attempt to push the non-promoting move first (should fail for a promotion move)
    if board.is_legal(move):
        board.push(move)
    else:
        # If the standard move is illegal, it's likely a promotion. 
        # Iterate through promotion types and push the first legal one (Queen is tried first)
        for promo in [chess.QUEEN, chess.ROOK, chess.BISHOP, chess.KNIGHT]:
            promo_move = chess.Move(move.from_square, move.to_square, promotion=promo)
            if promo_move in board.legal_moves:
                board.push(promo_move)
                break

def display_result(board):
    """
    Displays the final game outcome (Checkmate, Draw, etc.) on the screen.
    """
    screen.fill((0, 0, 0)) # Black background
    
    # Determine the game result based on python-chess board properties
    if board.is_checkmate():
        # Check whose turn it is to determine the winner
        winner = "Player Wins!" if not board.turn else "Computer Wins!"
    elif board.is_stalemate():
        winner = "Draw (Stalemate)"
    elif board.is_insufficient_material():
        winner = "Draw (Insufficient Material)"
    # Also check other draw rules for completeness
    elif board.is_seventyfive_moves():
        winner = "Draw (75-move rule)"
    elif board.is_fivefold_repetition():
        winner = "Draw (Fivefold repetition)"
    else:
        winner = f"Game Over: {board.result()}"

    # Render and center the result text
    result_font = pygame.font.SysFont("arial", 48)
    result_text = result_font.render(winner, True, (255, 255, 255))
    text_rect = result_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(result_text, text_rect)
    pygame.display.flip()
    
    # Pause the game to let the user see the result
    pygame.time.wait(4000)

# ----------------------------------------------------------------------
# MAIN GAME LOOP
# ----------------------------------------------------------------------

def main():
    """
    The main execution function containing the game loop and user interaction logic.
    """
    board = chess.Board() # Initialize the chess board
    selected_square = None # Stores the square index of the currently clicked piece
    running = True

    while running:
        legal_moves = []
        # If a square is selected, pre-calculate the legal target squares for drawing hints
        if selected_square is not None:
            legal_moves = [move.to_square for move in board.legal_moves if move.from_square == selected_square]

        # Redraw the board state every frame
        draw_board(board, selected_square, legal_moves)

        # Check for game termination conditions
        if board.is_game_over():
            display_result(board)
            running = False
            continue

        # Handle user input (events)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Player's Turn (White)
            elif event.type == pygame.MOUSEBUTTONDOWN and board.turn == chess.WHITE:
                # Get the square clicked by the mouse
                square = get_square_under_mouse(pygame.mouse.get_pos())
                
                if selected_square is not None:
                    # Case 1: A piece was already selected, this click is the destination
                    move = chess.Move(selected_square, square)
                    
                    if move in board.legal_moves:
                        # Move is legal: handle promotion or standard push
                        if board.piece_at(selected_square).piece_type == chess.PAWN and chess.square_rank(square) in [0, 7]:
                            promote_pawn(board, move)
                        else:
                            board.push(move)
                        selected_square = None # Deselect the piece after move
                    else:
                        # Invalid target, deselect
                        selected_square = None
                        
                elif board.piece_at(square) and board.piece_at(square).color == chess.WHITE:
                    # Case 2: No piece selected, but a White piece was clicked (select it)
                    selected_square = square

        # AI's Turn (Black)
        if board.turn == chess.BLACK and not board.is_game_over():
            # Add a small delay for a smoother user experience
            pygame.time.wait(300) 
            ai_move(board)

    # Clean up Pygame resources and exit
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
