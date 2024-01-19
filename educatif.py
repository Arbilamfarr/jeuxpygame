import pygame
import sys
import random

# Initialisation de Pygame
pygame.init()

# Paramètres de l'écran
WIDTH, HEIGHT = 800, 600
FPS = 60
FONT = pygame.font.SysFont("Arial", 36)

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Opérations mathématiques possibles
operations = ['+', '-', '*', '/']

# Création de l'écran
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Math Quiz Game")
clock = pygame.time.Clock()

# Variables pour les questions et les réponses
question = ""
correct_answer = ""
correct_count = 0
question_count = 0

# Génère une nouvelle question aléatoire
def generate_question():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operation = random.choice(operations)

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    else:
        # Évite les divisions donnant des décimaux
        while num1 % num2 != 0:
            num1 = random.randint(1, 10)
            num2 = random.randint(1, 10)
        result = num1 // num2

    return f"{num1} {operation} {num2} =", str(result)

# Boucle principale
running = True
while running:
    screen.fill(WHITE)

    # Vérifie si le nombre de questions atteint 20
    if question_count >= 20:
        score_text = FONT.render(f"Score: {correct_count} / 20", True, BLACK)
        screen.blit(score_text, (WIDTH // 2 - 100, HEIGHT // 2))
    else:
        # Générer une nouvelle question si nécessaire
        if not question:
            question, correct_answer = generate_question()

        # Affichage de la question
        text = FONT.render(question, True, BLACK)
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
        screen.blit(text, text_rect)

        # Écoute des événements utilisateur
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if question_count < 20:
                        if question == correct_answer:
                            correct_count += 1
                        question_count += 1
                        question = ""
                elif event.key == pygame.K_BACKSPACE:
                    question = question[:-1]
                else:
                    question += event.unicode

        # Vérification de la réponse
        if question == correct_answer:
            pygame.draw.rect(screen, GREEN, (WIDTH // 2 - 100, HEIGHT // 2 + 50, 200, 50))
            text = FONT.render("Correct!", True, BLACK)
            text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 75))
            screen.blit(text, text_rect)

    pygame.display.flip()
    clock.tick(FPS)
