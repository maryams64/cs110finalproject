import pygame
import charGui
import bullet
import ai
import background
import random
import sys

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 128, 0)
PURPLE = (128, 0, 128)
BROWN = (160, 82, 45)
totalBulletCount = 0
tickNum = 0
level = 0

easyColorList = [BLUE, BLUE, BLUE, BLUE, RED, RED, RED, GREEN, GREEN, PURPLE, BLACK, BROWN]
harderColorList = [BLUE, RED, RED, GREEN, PURPLE, PURPLE, PURPLE, BLACK, BLACK, BROWN]
veryHardColorList = [BLUE, RED, GREEN, PURPLE, PURPLE, BLACK, BLACK, BLACK, BROWN]
hardestColorList = [BLACK, BROWN, BROWN, BROWN, BROWN]


pygame.init()
clock = pygame.time.Clock()
screen_width = 1200
screen_height = 600
screen = pygame.display.set_mode([screen_width,screen_height])
pygame.display.update()
myfont = pygame.font.SysFont('Arial Black', 16)
all_sprites_list = pygame.sprite.Group()
bullet_list = pygame.sprite.Group()
player = charGui.char('moore', 'moore.png')
all_sprites_list.add(player)
gameOver = False

def makeBullet(count):
  if(count > 75):
    bul = bullet.Bullet(villain, random.choice(hardestColorList), player.rect.x, player.rect.y)
  elif(count > 50):
    bul = bullet.Bullet(villain, random.choice(veryHardColorList), player.rect.x, player.rect.y)
  elif(count > 25):
    bul = bullet.Bullet(villain, random.choice(harderColorList), player.rect.x, player.rect.y)
  else:
    bul = bullet.Bullet(villain, random.choice(easyColorList), player.rect.x, player.rect.y)
  return bul

def move(character):
  keys = pygame.key.get_pressed()
  if keys[pygame.K_LEFT]:
    player.left()
  elif keys[pygame.K_RIGHT]:
    player.right()
  elif keys[pygame.K_UP]:
    player.up()
  elif keys[pygame.K_DOWN]:
    player.down()
                  
for i in range(4):
  level = i + 1
  print("Level", i + 1)
  totalBulletCount = 0
  tickNum = 0
  villain = ai.combatAi(level)
  all_sprites_list.add(villain)
  while totalBulletCount < 101 and not gameOver:
    for event in pygame.event.get():
      keys = pygame.key.get_pressed()
      
    if event.type == pygame.QUIT:
      gameOver = True
                        
    if(tickNum % 12 == 0):
      bul = makeBullet(totalBulletCount)
      totalBulletCount += 1
      bullet_list.add(bul)
      all_sprites_list.add(bul)
                
    for bul in bullet_list:
      if(pygame.sprite.collide_rect(bul, player)):
        player.health -= bul.damage
        all_sprites_list.remove(bul)
        bullet_list.remove(bul)
        if(player.health <= 0):
          all_sprites_list.remove(player)
          gameOver = True
                                        
    move(player)
    all_sprites_list.update()
    screen.fill(WHITE) 
    all_sprites_list.draw(screen)
    pygame.display.update()
    clock.tick(30)
    tickNum += level
    if(gameOver):
      read = myfont.render("GAME OVER", 1, BLACK)
      screen.blit(read, [(screen_x/2), (screen_y/2)])
       
pygame.quit()

