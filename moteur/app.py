import pygame
import sys
import random
# Initialisation de Pygame
pygame.init()

# Dimensions de la fenêtre
WIDTH, HEIGHT = 1000, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Dimensions du tableau
rows, cols = 10, 5

# Génération du tableau
tableau = [random.sample([0,0,0, 1, 2], cols) for _ in range(rows)]

# Affichage du tableau
for ligne in tableau:
    print(ligne)

# Boucle principale
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
