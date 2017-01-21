import pygame
import sys
from pygame.locals import *
import random

pygame.init()
pygame.font.init()

display_width = 1280
display_height = 720

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

ox = int(display_width/2)
oy = int(display_height/2)

gamedisplay = pygame.display.set_mode((display_width,display_height))

pygame.display.set_caption('pygame test')

clock = pygame.time.Clock()
# een boot class hebben we het liefst, maar dat kreeg ik niet voor elkaar.

'''
class object:
    def __init__(self,hp,length,ox,oy):
        self.hp = hp
        self.length = length
        self.dis = pygame.draw.circle(gamedisplay,black,(ox,oy),10,0)
    def move_up(self):
        self.oy = self.oy - 50
    def move_down(self):
        self.oy = self.oy + 50
    def move_right(self):
        self.ox = self.ox + 50
    def move_left(self):
        self.ox = self.ox - 50
'''
'''
class button:
    def __init__(self,color,bxpos,bypos):
        self.color = color
        self.bx = bxpos
        self.by = bypos
    def draw(self):
'''
"""
def obj_(len):
     pygame.image.load('bootje.png')
    if len == 1:
        pygam

    pygame.draw.circle(gamedisplay,black,(ox,oy),10,0)"""

def yo_movement(oy,ox):
    for event in pygame.event.get():
        while pygame.event.EventType == pygame.KEYDOWN:
            if event.key == pygame.K_273:
                oy = oy + 50
            if event.key == pygame.K_274:
                oy = oy + 50
            if event.key == pygame.K_276:
                ox = ox - 50
            if event.key == pygame.K_275:
                ox = ox + 50
            pygame.display.update()


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def board_gen():
    t = 0
    x = display_width/5
    y = 0
    gamedisplay.fill((black))
    # obj_()
    while y <= display_height:
        while x < (display_width/5)*4:
            if t % 2 == 0:
                gamedisplay.fill(red,(x,y,display_width/33,display_height/20))
                t += 1
                x = x + (display_width/33)
            else:
                gamedisplay.fill(white,(x,y,display_width/33,display_height/20))
                t += 1
                x = x + (display_width/33)
        else:
            t += 1
            y = y +(display_height/20)
            x = display_width /5
            pygame.display.update()
    gameloop()

def main_menu():
        gamedisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf',115)
        TextSurf, TextRect = text_objects("BattlePort", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gamedisplay.blit(TextSurf, TextRect)

        pygame.draw.rect(gamedisplay,blue,(display_width/6,450,200,120))
        pygame.draw.rect(gamedisplay,red,(display_width/6*4,450,200,120))
        pygame.display.update()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN or event.type == MOUSEBUTTONDOWN:
                        board_gen()



def gameloop():
    crashed = False

    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            yo_movement(display_width/2,display_height/2)
            print(event)
            pygame.display.update()
    clock.tick(5)


main_menu()
