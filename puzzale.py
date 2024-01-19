import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Paramètres de l'écran
WIDTH, HEIGHT = 300, 300
TILE_SIZE = 50
ROWS, COLS = 6, 6

# Couleurs
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Création de l'écran
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Puzzle Game")

# Position initiale et finale du joueur
player_position = [0, 0]
end_position = [ROWS - 1, COLS - 1]

# Grille du jeu
game_map = [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 0],
    [0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0]
]

# Dessiner la grille
def draw_map():
    for row in range(ROWS):
        for col in range(COLS):
            tile = game_map[row][col]
            pygame.draw.rect(screen, BLUE if tile == 1 else WHITE, (col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE))
            pygame.draw.rect(screen, RED, (player_position[1] * TILE_SIZE, player_position[0] * TILE_SIZE, TILE_SIZE, TILE_SIZE))
            pygame.draw.rect(screen, GREEN, (end_position[1] * TILE_SIZE, end_position[0] * TILE_SIZE, TILE_SIZE, TILE_SIZE))

# Boucle principale
running = True
while running:
    screen.fill(WHITE)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and player_position[0] > 0 and game_map[player_position[0] - 1][player_position[1]] == 0:
                player_position[0] -= 1
            elif event.key == pygame.K_DOWN and player_position[0] < ROWS - 1 and game_map[player_position[0] + 1][player_position[1]] == 0:
                player_position[0] += 1
            elif event.key == pygame.K_LEFT and player_position[1] > 0 and game_map[player_position[0]][player_position[1] - 1] == 0:
                player_position[1] -= 1
            elif event.key == pygame.K_RIGHT and player_position[1] < COLS - 1 and game_map[player_position[0]][player_position[1] + 1] == 0:
                player_position[1] += 1
    
    draw_map()
    pygame.display.update()
