import pygame
import math
import random

class Bullet(pygame.sprite.Sprite):
    __count = 0
    damage = 1
    x = 0
    y = 0
    varx = 0
    vary = 0
    randx = (1 + random.random() - .5)
    randy = (1 + random.random() - .5)
    
    def count(cls):
        Bullet.__count += 1
        return Bullet.__count
        
    def __init__(self, ai, color, userX, userY):

        BLACK = (0, 0, 0)
        RED = (255, 0, 0)
        BLUE = (0, 0, 255)
        GREEN = (0, 128, 0)
        PURPLE = (128, 0, 128)
        BROWN = (160, 82, 45)

        if(color == RED):
            self.damage = 3
        elif(color == GREEN):
            self.damage = 5
        elif(color == PURPLE):
            self.damage = 7
        elif(color == BLACK):
            self.damage = 50
        elif(color == BROWN):
            self.damage = 100

        self.x = userX
        self.y = userY
        self.varx = ai.rect.x
        self.vary = ai.rect.y
        
        super().__init__()
        
        self.image = pygame.Surface([4,5])
        self.image.fill(color)

        self.rect = self.image.get_rect()

        self.rect.x = ai.rect.x
        self.rect.y = ai.rect.y
        
    def getCoordinates(self):
        return([self.rect.x,self.rect.y])


    def update(self):
        distx = self.randx * self.x - self.varx
        disty = self.randy * self.y - self.vary
        dist = math.hypot(distx, disty)
        self.rect.y += 2 * (disty / dist)
        self.rect.x += 2 * (distx / dist)
