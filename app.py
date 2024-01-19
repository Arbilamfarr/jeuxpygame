import pygame
import sys
import random

# Initialisation de Pygame
pygame.init()

# Paramètres de la fenêtre
WIDTH, HEIGHT = 800, 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jeu de Tir")

# Couleurs
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Joueur
player_width, player_height = 50, 50
player = pygame.Rect(WIDTH // 2 - player_width // 2, HEIGHT - player_height - 10, player_width, player_height)
player_speed = 5

# Ennemis
enemy_width, enemy_height = 50, 50
enemies = []
enemy_speed = 2
enemy_spawn_timer = 1000  # Délai de création d'un nouvel ennemi (en millisecondes)
last_enemy_spawn = pygame.time.get_ticks()

# Projectiles
projectile_width, projectile_height = 10, 30
projectiles = []
projectile_speed = 7

# Score
score = 0
font = pygame.font.Font(None, 36)

# Clock pour contrôler la vitesse de rafraîchissement
clock = pygame.time.Clock()

# Fonction pour afficher le score
def draw_score():
    score_text = font.render(f"Score: {score}", True, BLUE)
    window.blit(score_text, (10, 10))

# Boucle de jeu
running = True
while running:
    window.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Tirer un projectile lorsque la barre d'espace est enfoncée
                projectile = pygame.Rect(player.x + player.width // 2 - projectile_width // 2, player.y, projectile_width, projectile_height)
                projectiles.append(projectile)

    keys = pygame.key.get_pressed()
    # Déplacement du joueur avec les touches fléchées gauche/droite
    if keys[pygame.K_LEFT] and player.x - player_speed > 0:
        player.x -= player_speed
    if keys[pygame.K_RIGHT] and player.x + player_speed < WIDTH - player.width:
        player.x += player_speed

    # Création et déplacement des ennemis
    if pygame.time.get_ticks() - last_enemy_spawn > enemy_spawn_timer:
        enemy = pygame.Rect(random.randint(0, WIDTH - enemy_width), -enemy_height, enemy_width, enemy_height)
        enemies.append(enemy)
        last_enemy_spawn = pygame.time.get_ticks()

    for enemy in enemies:
        pygame.draw.rect(window, RED, enemy)
        enemy.y += enemy_speed
        # Supprimer les ennemis qui sortent de l'écran
        if enemy.y > HEIGHT:
            enemies.remove(enemy)

    # Mouvement des projectiles et collisions avec les ennemis
    for projectile in projectiles[:]:
        pygame.draw.rect(window, BLUE, projectile)
        projectile.y -= projectile_speed
        # Vérifier les collisions avec les ennemis
        for enemy in enemies[:]:
            if projectile.colliderect(enemy):
                projectiles.remove(projectile)
                enemies.remove(enemy)
                score += 1
        # Supprimer les projectiles qui sortent de l'écran
        if projectile.y < 0:
            projectiles.remove(projectile)

    # Affichage du joueur
    pygame.draw.rect(window, RED, player)

    draw_score()
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
