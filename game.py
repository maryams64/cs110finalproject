import pygame
pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
gameWidth = 800
gameLength = 600


gameDisplay = pygame.display.set_mode((gameWidth,gameLength))
pygame.display.set_caption("person")
pygame.display.update()

gameExit = False


sp = 2
lead_x = gameWidth//2
lead_y = gameLength - 60
lead_x_up = 0
lead_x_down = 0
lead_y_up = 0
lead_y_down = 0
clock = pygame.time.Clock()
fps = 60

while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                lead_x_down += sp
            if event.key == pygame.K_RIGHT:
                lead_x_up += sp
            if event.key == pygame.K_UP:
                lead_y_up += sp
            if event.key == pygame.K_DOWN:
                lead_y_down += sp
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                lead_x_up = 0
                lead_x_down = 0
            if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                lead_y_up = 0
                lead_y_down = 0
    #while gameExit:
        #if pygame.sprite.spritecollideany(sprite, group, collided = None) != None:            
    if lead_x >= gameWidth - 50:
        lead_x_up = 0
    if lead_x <= 50:
        lead_x_down = 0
    if lead_y >= gameLength - 50:
        lead_y_down = 0
    if lead_y <= 50:
        lead_y_up = 0

    lead_x += lead_x_up - lead_x_down
    lead_y += lead_y_down - lead_y_up





    gameDisplay.fill(white)
    pygame.draw.rect(gameDisplay, black, [lead_x,lead_y, 10,10])
    pygame.display.update()
    clock.tick(fps)


pygame.quit()
quit()
