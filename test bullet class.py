import pygame
import random

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, mouse):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([4,5])
        self.image.fill(WHITE)

        self.mouse_x, self.mouse_y = mouse[0], mouse[1]

        #self.rect = self.image.get_rect()

    def speed(self):
        
        sp = 3
        
    def update(self):
        
        self.mouse_y += 5

#instant variables to keep track of position
#keep track of speed
#keep track of bullet number
    
pygame.init()

clock = pygame.time.Clock()

screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width,screen_height])
pygame.display.update()

bullet_list = pygame.sprite.Group()

done = False
pos = pygame.mouse.get_pos()
while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                bullet = Bullet(pos)
                #bullet_list.add(bullet)
                
                bullet.update()
                #bullet_list.update()

            
                if bullet.mouse_y > 400:
                    #bullet_list.remove(bullet)
                    del bullet

        bullet_list.draw(screen)
        pygame.display.flip()
        clock.tick(30) 
        
pygame.quit()

