import pygame
import os
import random

class char(pygame.sprite.Sprite):
    "This class is the box"
    def __init__(self, name, image):
        super().__init__()
        self.name = name
        self.health = 100

        self.image = pygame.image.load(os.path.join('images', image))
        self.image = pygame.transform.scale(self.image, (200, 200))

        self.rect = self.image.get_rect()
        
        self.rect.x = 50
        self.rect.y = 300
        '''self.lead_x_up = 0
        self.lead_x_down = 0
        self.lead_y_up = 0
        self.lead_y_down = 0'''
        self.sp = 2
        #pygame.draw.rect(gameDisplay, red, [self.lead_x,self.lead_y, 10,10])


    def left(self):
        self.rect.x -= self.sp

    def right(self):
        self.rect.x += self.sp

    def up(self):
        self.rect.y -= self.sp

    def down(self):
        self.rect.y +=  self.sp

    def getCoordinates(self):
        return([self.rect.x,self.rect.y])

    def coll(self, gro):
        if pygame.sprite.spritecollide(self, gro, True):
            self.health -= random.randrange(1,11)
    
    def __str__(self):
        return('heip')
