import pygame
import charclass
import bulletclass2
import aiclass



WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

pygame.init()

clock = pygame.time.Clock()

screen_width = 700
screen_height = 400
 
screen = pygame.display.set_mode([screen_width,screen_height])


pygame.display.update()

all_sprites_list = pygame.sprite.Group()
bullet_list = pygame.sprite.Group()

stuf = charclass.char('bynn', RED)
all_sprites_list.add(stuf)

herald = aiclass.combatAi()
all_sprites_list.add(herald)
print('Herald Coordinates: ' +str(herald.getCoordinates()))

done = False

while not done:
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                bullet = bulletclass2.Bullet(herald, BLACK)
                bullet_list.add(bullet)
                all_sprites_list.add(bullet)
                print('Bullet Count: ' +str(bullet.count()))

            
                if bullet.rect.y > 400:
                    bullet_list.remove(bullet)
                    
            '''elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    stuf.left()
                    print('Left: ' +str(stuf.getCoordinates()))
                elif event.key == pygame.K_RIGHT:
                    stuf.right()
                    print('Right: ' +str(stuf.getCoordinates()))
                elif event.key == pygame.K_UP:
                    stuf.up()
                    print('Up: ' +str(stuf.getCoordinates()))
                elif event.key == pygame.K_DOWN:
                    stuf.down()
                    print('Down: ' + str(stuf.getCoordinates()))'''
            elif keys[pygame.K_UP]:
                stuf.up()
                    
        all_sprites_list.update()
        screen.fill(WHITE) 
        all_sprites_list.draw(screen)
        pygame.display.update()

        clock.tick(30) 
        
pygame.quit()
