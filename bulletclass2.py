import pygame

class Bullet(pygame.sprite.Sprite):
    __count = 0
    
    def count(cls):
        Bullet.__count += 1
        return Bullet.__count
        
    def __init__(self, ai, color):
        super().__init__()
        
        self.image = pygame.Surface([4,5])
        self.image.fill(color)

        self.rect = self.image.get_rect()

        self.rect.x = ai.rect.x
        self.rect.y = ai.rect.y
        
    def getCoordinates(self):
        return([self.rect.x,self.rect.y])


    def update(self):
        self.rect.y += 3
