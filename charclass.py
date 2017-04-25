import pygame

class char(pygame.sprite.Sprite):
    "This class is the box"
    def __init__(self, name, image, health, alive):
        super().__init__()
        self.name = name
        self.health = 100
        self.alive = True
        self.image = pygame.image.load(os.path.join('images', image))
        self.image = pygame.transform.scale(self.image, (50, 50))

        self.rect = self.image.get_rect()
        
        self.rect.x = 350
        self.rect.y = 340
        '''self.lead_x_up = 0
        self.lead_x_down = 0
        self.lead_y_up = 0
        self.lead_y_down = 0'''
        self.sp = 2
        #pygame.draw.rect(gameDisplay, red, [self.lead_x,self.lead_y, 10,10])
    '''
    def condition():
        while running=True: #make variable called running that stays True until game ends
            #check if any collisions are happening
            if(collision=True):
                x='''pgspritecollideany.damage''' #returns collided sprite, in this case a bullet, and takes the damage attribute of bullet
                self.health=self.health-x                        
    '''
    
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
