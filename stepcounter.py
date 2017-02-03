import sys
import pygame
from pygame.locals import *

pygame.init()
size = width, height = 800,600
screen = pygame.display.set_mode(size)
pygame.display.set_caption("testing")
myfont = pygame.font.SysFont("monospace", 16)
WHITE = (255,255,255)

steps = 4

while True:
    pygame.display.flip()
    for event in pygame.event.get():
        # I remove the timer just for my testing
        if event.type == pygame.QUIT: sys.exit()

    screen.fill(WHITE)

    disclaimertext = myfont.render("Bonobo", 1, (0,0,0))
    screen.blit(disclaimertext, (5, 580))

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                steps -= 1
            if event.key == pygame.K_RIGHT:
                steps -= 1
            if event.key == pygame.K_UP:
                steps -= 1
            if event.key == pygame.K_DOWN:
                steps -= 1
                break

    text = myfont.render("steps {0}".format(steps), 0, (0,0,0))
    screen.blit(text, (700, 0))
    steps -= 1

