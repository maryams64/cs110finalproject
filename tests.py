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
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            bullet = makeBullet(totalBulletCount)
            totalBulletCount += 1
            bullet_list.add(bullet)
            all_sprites_list.add(bullet)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        stuf.left()
        print('Left: ' +str(stuf.getCoordinates()))
    elif keys[pygame.K_RIGHT]:
        stuf.right()
        print('Right: ' +str(stuf.getCoordinates()))
    elif keys[pygame.K_UP]:
        stuf.up()
        print('Up: ' +str(stuf.getCoordinates()))
    elif keys[pygame.K_DOWN]:
        stuf.down()
        print('Down: ' + str(stuf.getCoordinates()))
        # for bul in bullet_list:
        #         if(pygame.sprite.collide_rect(bul, stuf)):
        #                 stuf.health -= bul.damage
        #                 print("Health:", stuf.health)
        #                 all_sprites_list.remove(bul)
        #                 bullet_list.remove(bul)
        #                 if(stuf.health <= 0):
        #                         all_sprites_list.remove(stuf)
        #                         print("you suck")


    all_sprites_list.update()
    screen.fill(WHITE)
    all_sprites_list.draw(screen)
    pygame.display.update()

    clock.tick(30)

pygame.quit()
