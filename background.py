import pygame
import os

class Background():
    def __init__(self, image, w, h):
               
        self.image = pygame.image.load(os.path.join('images', image))
        self.size = [w, h]
        self.image = pygame.transform.scale(self.image, self.size)
    
        self.rect = self.image.get_rect()
