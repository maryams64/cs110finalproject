import pygame
import math
import random

class Bullet(pygame.sprite.Sprite):
    
    damage = 1
    xU = 0
    yU = 0
    varx = 0
    vary = 0
    randx = math.sqrt(random.random() + .5)
    randy = math.sqrt(random.random() + .5)
        
    def __init__(self, ai, color, userX, userY):

        BLACK = (0, 0, 0)
        RED = (255, 0, 0)
        BLUE = (0, 0, 255)
        GREEN = (0, 128, 0)
        PURPLE = (128, 0, 128)
        BROWN = (160, 82, 45)

        if(color == GREEN):
            self.damage = 3
        elif(color == PURPLE):
            self.damage = 5
        elif(color == RED):
            self.damage = 7
        elif(color == BROWN):
            self.damage = 10
        elif(color == BLACK):
            self.damage = 15

        self.xU = userX
        self.yU = userY
        self.originx = ai.rect.x
        self.originy = ai.rect.y
        self.randMoveX = random.random() * 8 - 4
        self.randMoveY = random.random() * 8 - 4
        super().__init__()
        
        self.image = pygame.Surface([4,5])
        self.image.fill(color)

        self.rect = self.image.get_rect()

        self.rect.x = ai.rect.x
        self.rect.y = ai.rect.y
        
    def getCoordinates(self):
        return([self.rect.x,self.rect.y])


    def update(self):
        distx = (self.randx * self.xU) - self.originx
        disty = (self.randy * self.yU) - self.originy
        self.bullety = (disty / 100.0)
        self.bulletx = (distx / 100.0)
        self.rect.y += round(self.bullety)
        self.rect.x += round(self.bulletx)

        
