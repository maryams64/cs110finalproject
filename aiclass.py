import pygame

class combatAi(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
               
        self.image = pygame.image.load(os.path.join('images', image))
        self.w = 50
        self.h = 50
        self.image = pygame.transform.scale(self.image, (self.w, self.h))
    
        self.rect = self.image.get_rect()

        self.rect.x = 350
        self.rect.y = 0

    def getCoordinates(self):
        return([self.rect.x,self.rect.y])
