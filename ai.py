import pygame
import os
import random

class combatAi(pygame.sprite.Sprite):
    def __init__(self, level):
        super().__init__()

        if(level == 1):
            self.image = pygame.image.load(os.path.join('images', 'bean.png'))
        elif(level == 2):
            self.image = pygame.image.load(os.path.join('images', 'zach.png'))
        self.w = 100
        self.h = 100
        self.image = pygame.transform.scale(self.image, (self.w, self.h))
        self.image = self.image.convert_alpha()


        self.rect = self.image.get_rect()

        self.rect.x = random.randint(200,1000)
        self.rect.y = 0

    def getCoordinates(self):
        return([self.rect.x,self.rect.y])
