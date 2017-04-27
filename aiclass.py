import pygame

class combatAi(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
               
        self.image = pygame.Surface([4,5])
    
        self.rect = self.image.get_rect()

        self.rect.x = 350
        self.rect.y = 0

    def getCoordinates(self):
        return([self.rect.x,self.rect.y])
