import pygame
import charGui
import bullet
import ai
import random
import sys
import os

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
score = 0

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
all_sprites_list = pygame.sprite.Group()
bullet_list = pygame.sprite.Group()
player = charGui.char('moore', 'moore.png')
all_sprites_list.add(player)
gameOver = False
wantToLeave = False

def getBackground(level):
  if(level == 1):
    bg = pygame.image.load(os.path.join('images', 'arch.jpg'))
  elif(level == 2):
    bg = pygame.image.load(os.path.join('images', 'patio.jpg'))
  elif(level == 3):
    bg = pygame.image.load(os.path.join('images', 'stone.jpg'))
  elif(level == 4):
    bg = pygame.image.load(os.path.join('images', 'tower.jpg'))
  bg = pygame.transform.scale(bg, (screen_width, screen_height))
  return bg

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

def deleteBullets():
  for bul in bullet_list:
    all_sprites_list.remove(bul)
    bullet_list.remove(bul)

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

font = pygame.font.SysFont('Arial Black', 16)
       
for i in range(2):
  level = i + 1
  lvlPrnt = font.render("Level " + str(level), 1, BLACK)
  background = getBackground(level)
  totalBulletCount = 0
  tickNum = 0
  villain = ai.combatAi(level)
  all_sprites_list.add(villain)
  
  while totalBulletCount < 101 and not wantToLeave:
    if(gameOver and not wantToLeave):
        while(gameOver and not wantToLeave):
        #save score
          for event in pygame.event.get():
            keys = pygame.key.get_pressed()
          if(keys[pygame.K_SPACE] and gameOver):
            gameOver = False
            level = 1
            lvlPrnt = font.render("Level " + str(level), 1, BLACK)
            background = getBackground(level)
            totalBulletCount = 0
            tickNum = 0
            villain = ai.combatAi(level)
            all_sprites_list.add(villain)
            player.health = 100
            score = 0
            deleteBullets()
          elif event.type == pygame.QUIT:
            wantToLeave = True
          
          message = font.render("GAME OVER. Press spacebar to try again...", 1, BLACK)
          screen.blit(message, (400, 300))
          pygame.display.flip()
          
    for event in pygame.event.get():
      keys = pygame.key.get_pressed()

      if event.type == pygame.QUIT:
        wantToLeave = True
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
          gameOver = True

    scoretext = font.render("Health: "+str(player.health), 1, (BLACK))                                    
    screen.blit(background, (0, 0))
    screen.blit(scoretext, (100, 150))
    screen.blit(lvlPrnt, (100, 100))
    scrPrnt = font.render("Score: " + str(score), 1, BLACK)
    screen.blit(scrPrnt, (100, 200))
    move(player)
    all_sprites_list.update()
    all_sprites_list.draw(screen)
    clock.tick(30)
    tickNum += level
    score += level
    pygame.display.flip()

if(player.health > 0 and level == 2):
  while(not wantToLeave):
    for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        if event.type == pygame.QUIT:
          wantToLeave = True
        
    if(player.health > 0 and level == 2):
      win = font.render("You Won!", 1, (BLACK))                                    
      screen.blit(win, (600, 50))
      pygame.display.flip()

pygame.quit()







