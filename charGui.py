import pygame
import os

class char(pygame.sprite.Sprite):
    "This class is the box"
    def __init__(self, name, image):
        super().__init__()
        self.name = name
        self.health = 100

        self.image = pygame.image.load(os.path.join('images', image))
        self.image = pygame.transform.scale(self.image, (150, 150))
        self.image = self.image.convert_alpha()
        self.image = self.image.subsurface(pygame.Rect(45,20,45,130))

        self.rect = self.image.get_rect()

        self.rect.x = 600
        self.rect.y = 400
        self.sp = 4
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

    def __str__(self):
        return('heip')
