import pygame
import charclassgui
import bulletclass2
import aiclass
import screenclass
import random
import levels
import sys


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 128, 0)
PURPLE = (128, 0, 128)
BROWN = (160, 82, 45)
totalBulletCount = 0

easyColorList = [BLUE, BLUE, BLUE, BLUE, RED, RED, RED, GREEN, GREEN, PURPLE, BLACK, BROWN]
harderColorList = [BLUE, RED, RED, GREEN, PURPLE, PURPLE, PURPLE, BLACK, BLACK, BROWN]
veryHardColorList = [BLUE, RED, GREEN, PURPLE, PURPLE, BLACK, BLACK, BLACK, BROWN]
hardestColorList = [BLACK, BROWN, BROWN, BROWN, BROWN]

def process(char):
          keys = pygame.key.get_pressed()
          if keys[pygame.K_LEFT]:
                  char.left()
                  print('Left: ' +str(char.getCoordinates()))
          elif keys[pygame.K_RIGHT]:
                  char.right()
                  print('Right: ' +str(char.getCoordinates()))
          elif keys[pygame.K_UP]:
                  char.up()
                  print('Up: ' +str(char.getCoordinates()))
          elif keys[pygame.K_DOWN]:
                  char.down()
                  print('Down: ' + str(char.getCoordinates()))

# def makeBullet(num, ai, lv):
#         count = 0
#         while count < num:
#             if(count > 200):
#                     lv.bullet_list.add(bulletclass2.Bullet(ai, random.choice(hardestColorList)))
#                     lv.all_sprites_list.add(bulletclass2.Bullet(ai, random.choice(hardestColorList)))
#                     num += 1
#                     lv.bullet_list.update()
#             elif(200 > count > 150):
#                     lv.bullet_list.add(bulletclass2.Bullet(ai, random.choice(veryHardColorList)))
#                     lv.all_sprites_list.add(bulletclass2.Bullet(ai, random.choice(veryHardColorList)))
#                     num += 1
#                     lv.bullet_list.update()
#             elif(150 > count > 70):
#                     lv.bullet_list.add(bulletclass2.Bullet(ai, random.choice(harderColorList)))
#                     lv.all_sprites_list.add(bulletclass2.Bullet(ai, random.choice(harderColorList)))
#                     num += 1
#                     lv.bullet_list.update()
#             else:
#                     lv.bullet_list.add(bulletclass2.Bullet(ai, random.choice(easyColorList)))
#                     lv.all_sprites_list.add(bulletclass2.Bullet(ai, random.choice(easyColorList)))
#                     num += 1
#                     lv.bullet_list.update()
        #return lv.bullet_list


#print('Health: ' + str(stuf.health))

def main():
  pygame.init()

  clock = pygame.time.Clock()


  screen_x = 1200
  screen_y = 600

  size = (screen_x, screen_y)
  screen = pygame.display.set_mode(size)

  pygame.display.update()

  '''all_sprites_list = pygame.sprite.Group()
  bullet_list = pygame.sprite.Group()'''

  myfont = pygame.font.SysFont('Arial Black', 16)

  stuf = charclassgui.char('moore', 'moore.png')
  bean = aiclass.combatAi('bean.png')
  test = aiclass.combatAi('basketball.png')


  level_list = []
  pls = levels.Level1(stuf, bean, 'patio.jpg')
  level_list.append(pls)

  level_list.append(levels.Level2(stuf, test, 'arch.jpg'))

  level_list[0].all_sprites_list.add(stuf)
  level_list[0].char_list.add(stuf)
  print(level_list[0])
  level_list[0].all_sprites_list.add(bean)
  level_list[1].all_sprites_list.add(test)
  level_list[1].char_list.add(stuf)

  current_level_no = 0
  current_level = level_list[current_level_no]

  done = False
  game_over = False
  delay = 250

  max_bul = 100
  count = 0



  print(current_level.bullet_list)
  while not done:
          now = pygame.time.get_ticks()
          for event in pygame.event.get():
                keys = pygame.key.get_pressed()
                if event.type == pygame.QUIT:
                          done = True
          while count < max_bul:
              var = bulletclass2.Bullet(bean,RED)
              current_level.all_sprites_list.add(var)
              current_level.bullet_list.add(var)
              count += 1
              current_level.bullet_list.update()
          #makeBullet(100, bean, current_level)




        #   while len(makeBullet(10, bean, current_level)) < max_bul:
        #       print (len(makeBullet(10, bean, current_level)))
        #   while  i <= len(current_level.bullet_list):
        #         if now - lastshot > bean.delay:
        #             for bul in current_level.bullet_list:
        #                 bul.update()

                    #i += 1

                  #elif event.type == pygame.MOUSEBUTTONDOWN:

                          #bullet_list = makeBullet(75, bean, current_level)
                          #for bul in current_level.bullet_list:
                           # bul.update()
                            #print('Bullet Count: ' +str(bullet.count()))
          for i in current_level.char_list:
                i.coll(current_level.bullet_list)
                scoretext = myfont.render("Health: "+str(stuf.health), 1, (BLACK))
                print("Health:", stuf.health)
                if(stuf.health <= 0):
                        current_level.all_sprites_list.remove(stuf)
                        game_over = True
                        if game_over:
                            read = myfont.render("GAME OVER", 1, BLACK)







                '''if bullet.rect.y > 400:
                      bullet_list.remove(bullet)

                for bul in current_level.bullet_list:
                          if(pygame.sprite.collide_rect(bul, stuf)):
                                  stuf.health -= bul.damage
                                  print("Health:", stuf.health)
                                  current_level.all_sprites_list.remove(bul)
                                  current_level.bullet_list.remove(bul)
                                  if(stuf.health <= 0):
                                          current_level.all_sprites_list.remove(stuf)
                                          print("you suck")
                           if bullet.count() == len(bullet_list):
                            print('Congratulations! You completed the level!')
                            current_level_no += 1
                            current_level = level_list[current_level_no]'''

          #bean.update()
          process(stuf)
          current_level.all_sprites_list.update()
          current_level.draw(screen, size)
          screen.blit(scoretext, (100, 100))
          #screen.blit(read, [(screen_x/2), -(screen_y/2)])
          pygame.display.flip()

          clock.tick(60)

  pygame.quit()

main()
