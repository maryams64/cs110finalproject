import pygame
import charGui
import bullet
import ai
import random
import sys
import os
import json


#Runs the main game loop as well as defines the functions needed for the game loop
#Individual Program Units coded by M, Z, B; Put Together by Z; Debugged by B; Reorganized by M
def main():

    #Reads exposition for story from a JSON file--DATA PERMANENCE
    #Exposition Written + Initial Non-JSON Code by M, Rewritten into JSON by B
    def story(file):
      with open(file) as data_file:
        data = json.load(data_file)
      storyList = []
      for i in data:
        storyList.append(data[i])
      return storyList

    #Pulls the background for the level
    #Coded by Z
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

    #Creates bullets of various different colors to deal different damages. Frequency of damages various on specified count
    #Coded by Z
    def makeBullet(count):

      easyColorList = [(0, 0, 225), (0, 0, 225), (0, 0, 225), (0, 0, 225), (225, 0, 0), (225, 0, 0), (225, 0, 0), (0, 128, 0), (0, 128, 0), (128, 0, 128), (0, 0, 0), (160, 82, 45)]
      harderColorList = [(0, 0, 225), (225, 0, 0), (225, 0, 0), (0, 128, 0), (128, 0, 128), (128, 0, 128), (128, 0, 128), (0, 0, 0), (0, 0, 0), (160, 82, 45)]
      veryHardColorList = [(0, 0, 225), (225, 0, 0), (0, 128, 0), (128, 0, 128), (128, 0, 128), (0, 0, 0), (0, 0, 0), (0, 0, 0), (160, 82, 45)]
      hardestColorList = [(0, 0, 0), (160, 82, 45), (160, 82, 45), (160, 82, 45), (160, 82, 45)]

      if(count > 75):
        bul = bullet.Bullet(villain, random.choice(hardestColorList), player.rect.x, player.rect.y)
      elif(count > 50):
        bul = bullet.Bullet(villain, random.choice(veryHardColorList), player.rect.x, player.rect.y)
      elif(count > 25):
        bul = bullet.Bullet(villain, random.choice(harderColorList), player.rect.x, player.rect.y)
      else:
        bul = bullet.Bullet(villain, random.choice(easyColorList), player.rect.x, player.rect.y)
      return bul

    #Delete bullets from bullet_list effectively removing them from the screen
    #Coded by Z
    def deleteBullets():
      for bul in bullet_list:
        all_sprites_list.remove(bul)
        bullet_list.remove(bul)

    #Receives Boolen from get_pressed to determine whether a key is held down or not so that the user may move holding the key down
    #Coded by B
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

    #Loop Variables to initialize game loop
    storyList = story('story.json')
    totalBulletCount = 0
    tickNum = 0
    level = 0
    score = 0
    space = False

    #screen is initialized and the sprites are put into organized list so that specific lists can be updated
    #Clock begins for score purposes
    #Coded by M, Edited (Added as Necessary) by B and Z
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

    #Sets variable as False so that program may trigger Game Over and Leaving events
    #Coded by Z
    gameOver = False
    wantToLeave = False

    #Sets font for game
    #Coded by M
    font = pygame.font.SysFont('Arial Black', 16)


    #Progresses through exposition for plot
    #Coded by M; Debugged by B
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

    #Initializes levels with background and bullets and contains code to be used to advance levels
    #Coded by Z
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

      #Proceeds to next level after 100 bullets but also contains code for when dead
      #Main game play is coded here. Bullets are spawned and character movement code is here
      #Coded by Z, B and M
      while totalBulletCount < 101 and not wantToLeave:
        if(gameOver and not wantToLeave):
            while(gameOver and not wantToLeave):
              #character movement
              #Coded by B
              for event in pygame.event.get():
                keys = pygame.key.get_pressed()
              #Advances Level
              #Restarts level and calls new GUIs
              #Coded by Z and B
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

              #If 'X' Button is clicked, changes wantToLeave to True
              #Coded by Z
              elif event.type == pygame.QUIT:
                wantToLeave = True

              #Prints Game Over message if user dies
              #Coded by M
              message = font.render("GAME OVER. Press spacebar to try again...", 1, (0, 0, 0))
              screen.blit(message, (400, 300))
              pygame.display.flip()

        #Beginning of Loop for if Char Death Occurs
        #Character movement coded by B
        for event in pygame.event.get():
          keys = pygame.key.get_pressed()

          #if 'X' is closed changes appropriate variables to True to trigger events
          #Coded by Z and B
          if event.type == pygame.QUIT:
            wantToLeave = True
            gameOver = True

        #Automatically shoots bullets according to timer
        #Coded by B
        if(tickNum % 12 == 0):
          bul = makeBullet(totalBulletCount)
          totalBulletCount += 1
          bullet_list.add(bul)
          all_sprites_list.add(bul)

        #If bullet collides with player, health is decreased by bullet damage
        #Coded by Z, Debugged by B and M
        for bul in bullet_list:
          if(pygame.sprite.collide_rect(bul, player)):
            player.health -= bul.damage
            all_sprites_list.remove(bul)
            bullet_list.remove(bul)

            #Triggers Game Over event if Health reaches 0
            if(player.health <= 0):
              gameOver = True

        #Draws everything to screen and updates live as gameplay progresses
        #Coded by Z and M
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

    #If User won triggers winning text
    #Coded by Z
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


    #Quits game if 'X' is pressed
    pygame.quit()

main()
