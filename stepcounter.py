import sys
import pygame
from pygame.locals import *

pygame.init()

size = width, height = 800,600

screen = pygame.display.set_mode(size)
pygame.display.set_caption("dammit man")
myfont = pygame.font.SysFont("monospace", 16)
WHITE = (255,255,255)



def step_counter():
    steps = 4

    while steps > 0:
        pygame.display.flip()

        randomtext  = myfont.render("Dammit man", 1, (0,0,0))
    screen.blit(randomtext, (5, 550))

    text = myfont.render("steps {0}".format(steps), 1, (0, 0, 0))
    screen.blit(text, (5, 10))

    for event in pygame.event.get():
            # I remove the timer just for my testing
        if event.type == pygame.QUIT: sys.exit()

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

sys.exit()