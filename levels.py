import pygame
import os
import charclass

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 128, 0)
PURPLE = (128, 0, 128)
BROWN = (160, 82, 45)

class Level(object):
  def __init__(self):
    self.background = None
    self.all_sprites_list = pygame.sprite.Group()
    self.bullet_list = pygame.sprite.Group()
    self.char_list = pygame.sprite.Group()
    self.player = None
    self.ai = None
    self.test = True



  def append(self, sprite):
    self.all_sprites_list.add(sprite)

  def update(self):
    self.all_sprites_list.update()
    self.bullet_list.update()

  def draw(self, screen, size):
    screen.fill(WHITE)
    self.background = pygame.transform.scale(self.background, size)
    self.rect = self.background.get_rect()
    screen.blit(self.background, size)

    self.all_sprites_list.draw(screen)
    self.bullet_list.draw(screen)

  def __str__(self):
      return str(self.all_sprites_list)

class Level1(Level):
  def __init__(self, char, ai, img):
    Level.__init__(self)
    self.background = pygame.image.load(os.path.join('images', img)).convert_alpha()
    self.player = char
    self.ai = ai
    self.test = False

  def __str__(self):
    return str(self.all_sprites_list)

    #Level.append(char)


class Level2(Level):
  def __init__(self, char, ai, img):
    Level.__init__(self)
    self.background = pygame.image.load(os.path.join('images', img)).convert_alpha()
    self.player = char
    self.ai = ai
