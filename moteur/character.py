class Character:
    def __init__(self, name, cols):
        self.name = name
        self.health = 3
        self.score = 0
        self.currentColumn = 0  # Position (colonne) dans le tableau
        self.cols = cols  # Stocker cols comme un attribut de l'instance

    def move_left(self):
        # Déplace le personnage à gauche
        if self.currentColumn > 0:
            self.currentColumn -= 1

    def move_right(self):
        # Déplace le personnage à droite
        if self.currentColumn < self.cols - 1:  # Utiliser self.cols
            self.currentColumn += 1

    def interact(self, cell_value, tableau, row, col):
        # Interagit avec la case actuelle
        if cell_value == 2:
            self.health -= 1  # Perdre une vie
            print(f"{self.name} a perdu une vie! Santé actuelle: {self.health}")
        elif cell_value == 1:
            self.score += 1  # Gagner un point
            print(f"{self.name} a gagné un point! Score actuel: {self.score}")
        
        # Faire disparaître la case
        tableau[row][col] = 0  # Remplacer la valeur par 0 pour la faire disparaître

    def getHealth(self):
        return self.health

    def getScore(self):
        return self.score