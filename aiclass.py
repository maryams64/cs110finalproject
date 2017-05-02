import pygame
import os

class combatAi(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()

        self.image = pygame.image.load(os.path.join('images', image))
        self.w = 200
        self.h = 200
        self.image = pygame.transform.scale(self.image, (self.w, self.h))

        self.rect = self.image.get_rect()

        self.rect.x = 950
        self.rect.y = 300
        self.sp = 1
        

    #def update(self):
        #self.image.scroll(self.sp,self.sp)

    def getCoordinates(self):
        return([self.rect.x,self.rect.y])
