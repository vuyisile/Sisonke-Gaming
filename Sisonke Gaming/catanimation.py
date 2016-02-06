5import pygame, sys
from pygame.locals import *

pygame.init()

FPS = 30 # frames per second setting
fpsClock = pygame.time.Clock()

# set up the window
DISPLAYSURF = pygame.display.set_mode((900, 600), 0, 32)
pygame.display.set_caption('Animation')

PINK = (255, 105, 180)
catgirlImg = pygame.image.load('catgirl.png')
catgirlx = 10
catgirly = 10
direction = 'right' 'left'

while True: # the main game loop
    DISPLAYSURF.fill(PINK)

    if direction == 'right':
        catgirlx += 5
        if catgirlx == 280:
            direction = 'down'
    elif direction == 'down':
        catgirly += 5
        if catgirly == 220:
            direction = 'left'
    elif direction == 'left':
        catgirlx -= 5
        if catgirlx == 10:
            direction = 'up'
    elif direction == 'up':
        catgirly -= 5
        if catgirly == 10:
            direction = 'right'

    DISPLAYSURF.blit(catgirlImg, (catgirlx, catgirly))
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)
