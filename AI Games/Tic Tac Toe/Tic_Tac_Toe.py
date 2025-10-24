import pygame
import sys
import math

# Initialize Pygame
pygame.init()
WIDTH, HEIGHT = 300, 300
LINE_WIDTH = 5
CELL_SIZE = WIDTH // 3
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe - Human vs AI")
FONT = pygame.font.SysFont("arial", 60)

# Colors
WHITE = (255, 255, 255)
LINE_COLOR = (0, 0, 0)
X_COLOR = (200, 0, 0)
O_COLOR = (0, 0, 200)

# Board setup
board = [["" for _ in range(3)] for _ in range(3)]

def draw_board():
    screen.fill(WHITE)
    for i in range(1, 3):
        pygame.draw.line(screen, LINE_COLOR, (0, i * CELL_SIZE), (WIDTH, i * CELL_SIZE), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (i * CELL_SIZE, 0), (i * CELL_SIZE, HEIGHT), LINE_WIDTH)
    for r in range(3):
        for c in range(3):
            if board[r][c] == "X":
                text = FONT.render("X", True, X_COLOR)
                screen.blit(text, text.get_rect(center=(c * CELL_SIZE + CELL_SIZE // 2, r * CELL_SIZE + CELL_SIZE // 2)))
            elif board[r][c] == "O":
                text = FONT.render("O", True, O_COLOR)
                screen.blit(text, text.get_rect(center=(c * CELL_SIZE + CELL_SIZE // 2, r * CELL_SIZE + CELL_SIZE // 2)))
    pygame.display.flip()

def check_winner():
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != "":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != "":
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != "":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != "":
        return board[0][2]
    return None

def is_full():
    return all(cell != "" for row in board for cell in row)

def minimax(is_maximizing):
    winner = check_winner()
    if winner == "O": return 1
    if winner == "X": return -1
    if is_full(): return 0

    if is_maximizing:
        best = -math.inf
        for r in range(3):
            for c in range(3):
                if board[r][c] == "":
                    board[r][c] = "O"
                    score = minimax(False)
                    board[r][c] = ""
                    best = max(score, best)
        return best
    else:
        best = math.inf
        for r in range(3):
            for c in range(3):
                if board[r][c] == "":
                    board[r][c] = "X"
                    score = minimax(True)
                    board[r][c] = ""
                    best = min(score, best)
        return best

def ai_move():
    best_score = -math.inf
    move = None
    for r in range(3):
        for c in range(3):
            if board[r][c] == "":
                board[r][c] = "O"
                score = minimax(False)
                board[r][c] = ""
                if score > best_score:
                    best_score = score
                    move = (r, c)
    if move:
        board[move[0]][move[1]] = "O"

def show_result(winner):
    screen.fill(WHITE)
    msg = "Draw!" if winner is None else f"{winner} wins!"
    text = FONT.render(msg, True, (0, 0, 0))
    screen.blit(text, text.get_rect(center=(WIDTH // 2, HEIGHT // 2)))
    pygame.display.flip()
    pygame.time.wait(3000)

def main():
    running = True
    player_turn = True
    while running:
        draw_board()
        winner = check_winner()
        if winner or is_full():
            show_result(winner)
            running = False
            continue

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif player_turn and event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                row, col = y // CELL_SIZE, x // CELL_SIZE
                if board[row][col] == "":
                    board[row][col] = "X"
                    player_turn = False

        if not player_turn and not check_winner() and not is_full():
            pygame.time.wait(300)
            ai_move()
            player_turn = True

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()