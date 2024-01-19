import pygame
import sys
import pickle

# Initialisation de Pygame
pygame.init()

# Paramètres de l'écran
WIDTH, HEIGHT = 300, 400
LINE_WIDTH = 15
BOARD_ROWS, BOARD_COLS = 3, 3
SQUARE_SIZE = WIDTH // BOARD_COLS

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LINE_COLOR = (23, 145, 135)

# Création de l'écran
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")
screen.fill(WHITE)

# Tableau pour stocker les valeurs du jeu (0 pour vide, 1 pour X, 2 pour O)
board = [[0 for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]

# Chargement des scores depuis le fichier (s'ils existent)
try:
    with open("scores.pickle", "rb") as file:
        player1_score, player2_score = pickle.load(file)
except FileNotFoundError:
    player1_score, player2_score = 0, 0

# Dessiner la grille
def draw_lines():
    # Lignes horizontales
    pygame.draw.line(screen, LINE_COLOR, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, 2 * SQUARE_SIZE), (WIDTH, 2 * SQUARE_SIZE), LINE_WIDTH)
    # Lignes verticales
    pygame.draw.line(screen, LINE_COLOR, (SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT - 100), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (2 * SQUARE_SIZE, 0), (2 * SQUARE_SIZE, HEIGHT - 100), LINE_WIDTH)

# Dessiner les X et O
def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 1:
                pygame.draw.circle(screen, BLACK, (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), SQUARE_SIZE // 3, LINE_WIDTH)
            elif board[row][col] == 2:
                pygame.draw.line(screen, BLACK, (col * SQUARE_SIZE + LINE_WIDTH, row * SQUARE_SIZE + SQUARE_SIZE - LINE_WIDTH), 
                                 (col * SQUARE_SIZE + SQUARE_SIZE - LINE_WIDTH, row * SQUARE_SIZE + LINE_WIDTH), LINE_WIDTH)
                pygame.draw.line(screen, BLACK, (col * SQUARE_SIZE + LINE_WIDTH, row * SQUARE_SIZE + LINE_WIDTH), 
                                 (col * SQUARE_SIZE + SQUARE_SIZE - LINE_WIDTH, row * SQUARE_SIZE + SQUARE_SIZE - LINE_WIDTH), LINE_WIDTH)

# Fonction pour marquer une case
def mark_square(row, col, player):
    board[row][col] = player

# Fonction pour vérifier si un joueur a gagné
def check_win(player):
    # Vérification des lignes et des colonnes
    for i in range(BOARD_ROWS):
        if all(board[i][j] == player for j in range(BOARD_COLS)) or all(board[j][i] == player for j in range(BOARD_ROWS)):
            return True
    # Vérification des diagonales
    if all(board[i][i] == player for i in range(BOARD_ROWS)) or all(board[i][BOARD_COLS - i - 1] == player for i in range(BOARD_ROWS)):
        return True
    return False

# Fonction pour vérifier si le tableau est plein
def check_draw():
    return all(board[i][j] != 0 for i in range(BOARD_ROWS) for j in range(BOARD_COLS))

# Variable pour alterner les tours des joueurs
current_player = 1

# Boucle principale
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Sauvegarde des scores dans un fichier avant de quitter
            with open("scores.pickle", "wb") as file:
                pickle.dump((player1_score, player2_score), file)
            running = False
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and not check_win(1) and not check_win(2):
            mouseX = event.pos[0]
            mouseY = event.pos[1]
            
            clicked_row = mouseY // SQUARE_SIZE
            clicked_col = mouseX // SQUARE_SIZE
            
            if board[clicked_row][clicked_col] == 0:
                mark_square(clicked_row, clicked_col, current_player)
                if check_win(current_player):
                    if current_player == 1:
                        player1_score += 1
                    else:
                        player2_score += 1
                    print(f"Player {current_player} wins!")
                elif check_draw():
                    print("It's a draw!")
                else:
                    current_player = 2 if current_player == 1 else 1
    
    screen.fill(WHITE)
    draw_lines()
    draw_figures()

    # Affichage des scores
    font = pygame.font.Font(None, 36)
    text1 = font.render(f"Player 1 Score: {player1_score}", True, BLACK)
    text2 = font.render(f"Player 2 Score: {player2_score}", True, BLACK)
    screen.blit(text1, (10, HEIGHT - 80))
    screen.blit(text2, (10, HEIGHT - 40))

    pygame.display.update()
