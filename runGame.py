import pygame
import charGui
import bullet
import ai
import random
import sys
import os
import json


def story(file):
    with open(file) as data_file:
        data = json.load(data_file)
    storyList = []
    for i in data:
        storyList.append(data[i])
    return storyList


storyList = story('story.json')
totalBulletCount = 0
tickNum = 0
level = 0
score = 0
space = False

easyColorList = [(0, 0, 225), (0, 0, 225), (0, 0, 225), (0, 0, 225), (225, 0, 0), (225, 0, 0), (225, 0, 0), (0, 128, 0), (0, 128, 0), (128, 0, 128), (0, 0, 0), (160, 82, 45)]
harderColorList = [(0, 0, 225), (225, 0, 0), (225, 0, 0), (0, 128, 0), (128, 0, 128), (128, 0, 128), (128, 0, 128), (0, 0, 0), (0, 0, 0), (160, 82, 45)]
veryHardColorList = [(0, 0, 225), (225, 0, 0), (0, 128, 0), (128, 0, 128), (128, 0, 128), (0, 0, 0), (0, 0, 0), (0, 0, 0), (160, 82, 45)]
hardestColorList = [(0, 0, 0), (160, 82, 45), (160, 82, 45), (160, 82, 45), (160, 82, 45)]


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

for i in range(12):
  space = False
  story = font.render(storyList[i], 1, ((255, 255, 255)))
  while(not space):
      screen.blit(story, (20, 200))
      pygame.display.flip()
      for event in pygame.event.get():
          keys = pygame.key.get_pressed()
          if(keys[pygame.K_SPACE]):
            screen.fill((0, 0, 0))
            pygame.display.flip()
            space = True

for i in range(2):
  level = i + 1
  lvlPrnt = font.render("Level " + str(level), 1, (0, 0, 0))
  background = getBackground(level)
  totalBulletCount = 0
  tickNum = 0
  if(level > 1):
    all_sprites_list.remove(villain)
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
            lvlPrnt = font.render("Level " + str(level), 1, (0, 0, 0))
            background = getBackground(level)
            totalBulletCount = 0
            tickNum = 0
            all_sprites_list.remove(villain)
            villain = ai.combatAi(level)
            all_sprites_list.add(villain)
            player.health = 100
            score = 0
            deleteBullets()
          elif event.type == pygame.QUIT:
            wantToLeave = True

          message = font.render("GAME OVER. Press spacebar to try again...", 1, (0, 0, 0))
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

    scoretext = font.render("Health: "+str(player.health), 1, ((0, 0, 0)))
    screen.blit(background, (0, 0))
    screen.blit(scoretext, (100, 150))
    screen.blit(lvlPrnt, (100, 100))
    scrPrnt = font.render("Score: " + str(score), 1, (0, 0, 0))
    screen.blit(scrPrnt, (100, 200))
    move(player)
    all_sprites_list.update()
    all_sprites_list.draw(screen)
    clock.tick(30)
    tickNum += level
    score += level
    pygame.display.flip()
if(not wantToLeave and level == 2):
  while(not wantToLeave):
        win = font.render("You Won!", 1, (0,0,0))
        screen.blit(win, (300, 100))
        pygame.display.flip()
        for event in pygame.event.get():
          keys = pygame.key.get_pressed()
          if event.type == pygame.QUIT:
            wantToLeave = True
            gameOver = True


pygame.quit()
