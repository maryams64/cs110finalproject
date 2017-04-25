import pygame

class combatAi(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
               
        self.image = pygame.image.load(os.path.join('images', image))
        self.image = pygame.transform.scale(self.image, (50, 50))
    
        self.rect = self.image.get_rect()

        self.rect.x = 350
        self.rect.y = 0

    def getCoordinates(self):
        return([self.rect.x,self.rect.y])
