import pygame
import os

class combatAi(pygame.sprite.Sprite):
    def __init__(self, level):
        super().__init__()

        if(level == 1):
            self.image = pygame.image.load(os.path.join('images', 'moore.png'))
        elif(level == 2):
            self.image = pygame.image.load(os.path.join('images', 'moore.png'))
        elif(level == 3):
            self.image = pygame.image.load(os.path.join('images', 'moore.png'))
        elif(level == 4):
            self.image = pygame.image.load(os.path.join('images', 'moore.png'))
        self.w = 50
        self.h = 50
        self.image = pygame.transform.scale(self.image, (self.w, self.h))
    
        self.rect = self.image.get_rect()

        self.rect.x = 350
        self.rect.y = 0

    def getCoordinates(self):
        return([self.rect.x,self.rect.y])
