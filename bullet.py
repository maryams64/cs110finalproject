import pygame
import math
import random

class Bullet(pygame.sprite.Sprite):

    randMoveX = 1
    randMoveY = 1
    damage = 1
    xU = 0
    yU = 0
    varx = 0
    vary = 0
    randx = 1
    randy = 1

    def __init__(self, ai, color, userX, userY):


        if(color == (0, 128, 0)):
            self.damage = 3
        elif(color == (128, 0, 128)):
            self.damage = 5
        elif(color == (225, 0, 0)):
            self.damage = 7
        elif(color == (160, 82, 45)):
            self.damage = 10
        elif(color == (0, 0, 0)):
            self.damage = 15

        self.xU = userX
        self.yU = userY
        self.originx = ai.rect.x
        self.originy = ai.rect.y

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
