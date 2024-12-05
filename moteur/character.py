class character:
    def __init__(self, name):
        self.name = name
        self.health = 3
        self.currentPosition = (0, 0)
                
    def move(self):
        print(f"{self.name} is moving")
        
    def setHealth(self, health):
        self.health = health
        
    def getHealth(self):
        return self.health
