import pygame

class char(pygame.sprite.Sprite):
    "This class is the box"
    def __init__(self, name, color):
        super().__init__()
        self.name = name

        self.image = pygame.Surface([4,5])
        self.image.fill(color)

        self.rect = self.image.get_rect()
        
        self.rect.x = 350
        self.rect.y = 340
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
    
    def __str__(self):
        return('heip')

'''pygame.init()
gameDisplay = pygame.display.set_mode((gameWidth,gameLength))
pygame.display.set_caption("person")
pygame.display.update()

all_sprites_list = pygame.sprite.Group()
gameExit = False
clock = pygame.time.Clock()
stuf = char('bynn')
all_sprites_list.add(stuf)
while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                stuf.left()
            elif event.key == pygame.K_RIGHT:
                stuf.right()
            elif event.key == pygame.K_UP:
                stuf.up()
            elif event.key == pygame.K_DOWN:
                stuf.down()
        #------NONFUNCTIONAL CODE-------
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                stuf.rect.x = 0
                stuf.lead_x_down = 0
            elif event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                stuf.lead_y_up = 0
                stuf.lead_y_down = 0

    if stuf.lead_x >= gameWidth - 50:
        stuf.lead_x_up = 0
    if stuf.lead_x <= 50:
        stuf.lead_x_down = 0
    if stuf.lead_y >= gameLength - 50:
        stuf.lead_y_down = 0
    if stuf.lead_y <= 50:
        stuf.lead_y_up = 0

    stuf.lead_x += stuf.lead_x_up - stuf.lead_x_down
    stuf.lead_y += stuf.lead_y_down - stuf.lead_y_up
    #-------END OF NONFUNCTIONAL CODE---------

    gameDisplay.fill(black)
    all_sprites_list.draw(gameDisplay)
    
    pygame.display.update()
    clock.tick(fps)'''
pygame.quit()
