import pygame
import charclass
import bulletclass2
import aiclass
import random


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 128, 0)
PURPLE = (128, 0, 128)
BROWN = (160, 82, 45)
totalBulletCount = 0
tickNum = 0
level = 1

easyColorList = [BLUE, BLUE, BLUE, BLUE, RED, RED, RED, GREEN, GREEN, PURPLE, BLACK, BROWN]
harderColorList = [BLUE, RED, RED, GREEN, PURPLE, PURPLE, PURPLE, BLACK, BLACK, BROWN]
veryHardColorList = [BLUE, RED, GREEN, PURPLE, PURPLE, BLACK, BLACK, BLACK, BROWN]
hardestColorList = [BLACK, BROWN, BROWN, BROWN, BROWN]


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

def makeBullet(count):
        if(count > 200):
                bullet = bulletclass2.Bullet(herald, random.choice(hardestColorList), stuf.rect.x, stuf.rect.y)
        elif(count > 150):
                bullet = bulletclass2.Bullet(herald, random.choice(veryHardColorList), stuf.rect.x, stuf.rect.y)
        elif(count > 70):
                bullet = bulletclass2.Bullet(herald, random.choice(harderColorList), stuf.rect.x, stuf.rect.y)
        else:
                bullet = bulletclass2.Bullet(herald, random.choice(easyColorList), stuf.rect.x, stuf.rect.y)
        return bullet

print(stuf.health)
while not done:
        if(tickNum % 10 == 0):
                bullet = makeBullet(totalBulletCount)
                totalBulletCount += 1
                bullet_list.add(bullet)
                all_sprites_list.add(bullet)
                
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if event.type == pygame.QUIT:
                done = True

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    stuf.left()
                elif event.key == pygame.K_RIGHT:
                    stuf.right()
                elif event.key == pygame.K_UP:
                    stuf.up()
                elif event.key == pygame.K_DOWN:
                    stuf.down()
                
        for bul in bullet_list:
                if(pygame.sprite.collide_rect(bul, stuf)):
                        stuf.health -= bul.damage
                        print("Health:", stuf.health)
                        all_sprites_list.remove(bul)
                        bullet_list.remove(bul)
                        if(stuf.health <= 0):
                                all_sprites_list.remove(stuf)
                                print("you suck")

        all_sprites_list.update()
        screen.fill(WHITE) 
        all_sprites_list.draw(screen)
        pygame.display.update()
        clock.tick(30)
        tickNum += level
        
pygame.quit()

