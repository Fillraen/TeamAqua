import pygame
import sys
import random
from character import Character  # Importer la classe Character

# Initialisation de Pygame
pygame.init()

# Dimensions de la fenêtre
WIDTH, HEIGHT = 1000, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Défilement de tableau")

# Couleurs
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)  # Couleur pour le personnage
YELLOW = (255, 255, 0)  # Couleur pour la valeur 1
RED = (255, 0, 0)  # Couleur pour la valeur 2
BLACK = (0, 0, 0)

speed_increase_factor = 0.99  # Facteur de réduction de la vitesse
min_move_interval = 10  # Limite inférieure pour move_interval

# Dimensions du tableau
rows, cols = 200, 5  # Augmenter le nombre de lignes à 200

# Génération du tableau
tableau = [random.sample([0, 0, 0, 1, 2], cols) for _ in range(rows)]

# Création du personnage
player = Character("Héros", cols)  # Passer cols ici

# Vitesse de défilement
move_interval = 60  # Nombre de frames avant de descendre d'une ligne (augmenté pour ralentir)

# Compteur pour contrôler la fréquence de défilement
move_counter = 0

# Indice de la ligne actuelle à afficher
current_row_index = 0

# Variable pour contrôler le mouvement
can_move = True
next_move = None  # Variable pour stocker le mouvement prévu

# Boucle principale
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if can_move:  # Vérifier si le personnage peut se déplacer
                if event.key == pygame.K_LEFT:
                    next_move = 'left'  # Enregistrer le mouvement à gauche
                elif event.key == pygame.K_RIGHT:
                    next_move = 'right'  # Enregistrer le mouvement à droite

    # Effacer l'écran
    screen.fill(WHITE)

    # Mise à jour de la position du tableau
    move_counter += 1
    if move_counter >= move_interval:  # Vérifier si le tableau doit défiler
        # Interagir avec la case actuelle
        cell_value = tableau[current_row_index][player.currentColumn]  # On prend la case actuelle pour l'interaction
        player.interact(cell_value, tableau, current_row_index, player.currentColumn)  # Interagir avec la case

        # Vérifier si le personnage est mort
        if player.getHealth() <= 0:  # Si la vie est 0 ou moins
            # Afficher un message de fin de jeu
            font = pygame.font.Font(None, 74)
            end_text = font.render("Vous êtes mort!", True, BLACK)
            screen.blit(end_text, (WIDTH // 2 - end_text.get_width() // 2, HEIGHT // 2 - end_text.get_height() // 2))
            pygame.display.flip()
            pygame.time.wait(2000)  # Attendre 2 secondes avant de quitter
            pygame.quit()
            sys.exit()

        # Augmenter la vitesse de défilement
        move_interval = max(min_move_interval, move_interval * speed_increase_factor)  # Réduire move_interval

        current_row_index += 1  # Passer à la ligne suivante
        
        # Vérifier si le tableau est terminé
        if current_row_index >= rows:  # Si on atteint la fin du tableau
            # Afficher un message de fin de jeu
            font = pygame.font.Font(None, 74)
            end_text = font.render("Fin de la partie!", True, BLACK)
            screen.blit(end_text, (WIDTH // 2 - end_text.get_width() // 2, HEIGHT // 2 - end_text.get_height() // 2))
            pygame.display.flip()
            pygame.time.wait(2000)  # Attendre 2 secondes avant de quitter
            pygame.quit()
            sys.exit()

        move_counter = 0  # Réinitialiser le compteur
        
        # Déplacer le personnage selon le mouvement prévu
        if next_move == 'left':
            player.move_left()
        elif next_move == 'right':
            player.move_right()
        
        # Réinitialiser le mouvement prévu
        next_move = None
        can_move = True  # Réactiver le mouvement après le défilement

    # Affichage du tableau (carrés jaunes et rouges)
    for i in range(10):  # Afficher seulement 10 lignes visibles
        row_index = (current_row_index + i) % rows  # Calculer l'indice de la ligne à afficher
        for j in range(cols):
            cell_value = tableau[row_index][j]
            if cell_value == 1:
                pygame.draw.rect(screen, YELLOW, (50 + j * 100, 50 + (i * 60), 80, 30))  # Carré jaune
            elif cell_value == 2:
                pygame.draw.rect(screen, RED, (50 + j * 100, 50 + (i * 60), 80, 30))  # Carré rouge

    # Affichage du personnage (carré bleu, positionné selon la colonne actuelle)
    pygame.draw.rect(screen, BLUE, (50 + player.currentColumn * 100, 50 + (0 * 60), 80, 30))  # Personnage en bleu

    # Affichage des données (score et vie)
    font = pygame.font.Font(None, 36)  # Police par défaut
    score_text = font.render(f"Score: {player.getScore()}", True, BLACK)
    health_text = font.render(f"Vie: {player .getHealth()}", True, BLACK)
    screen.blit(score_text, (WIDTH - 200, 20))  # Afficher le score en haut à droite
    screen.blit(health_text, (WIDTH - 200, 60))  # Afficher la vie en dessous du score

    # Mettre à jour l'affichage
    pygame.display.flip()
    clock.tick(60)  # Limiter à 60 FPS