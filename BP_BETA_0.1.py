import pygame
import sys
from pygame.locals import *
import random

# initialize pygame
pygame.init()
pygame.font.init()

#   set up resolution
display_width = 1280
display_height = 720

#   Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (200, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 200)
aqua = (0, 255, 255)
silver = (192, 192, 192)
dark_silver = (220, 220, 220)
bright_red = (255, 0, 0)
bright_blue = (0, 0, 255)

#   text font sizes
largeText = pygame.font.Font('freesansbold.ttf', 115)
mediumText = pygame.font.Font('freesansbold.ttf', 60)
smallText = pygame.font.Font('freesansbold.ttf', 20)

ox = int(display_width/2)
oy = int(display_height/2)

#   display screen
gamedisplay = pygame.display.set_mode((display_width, display_height))

#   name when game is running
pygame.display.set_caption('pygame test')

clock = pygame.time.Clock()

#   loading images and setting the right resolution
bg_image = pygame.image.load("bg1.jpg")
bg_image = pygame.transform.scale(bg_image, (display_width, display_height))
ship_img = pygame.image.load("boot4.png")


# een boot class hebben we het liefst, maar dat kreeg ik niet voor elkaar.

"""
def ship(x, y):
    gamedisplay.blit(ship_img(x, y))

    if mousbutton_pressed == [1]
        Posx = Pygame.get.mousepos(x)
        Posy = pygame.get.mouse_pos(y)
        Self.x = posx
        Self.y = posy

x = (display_width * 0.45)
y = (display_height * 0.8)
"""



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

#   function to display button an make them interactive
#   (message, x pos, y pos, width, height, inactive color, active color, textsize)
def button(msg, x, y, w, h, ic, ac, ts):
    mouse = pygame.mouse.get_pos()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gamedisplay, ac, (x, y, w, h))
    else:
        pygame.draw.rect(gamedisplay, ic, (x, y, w, h))

    TextSurf, TextRect = text_objects(msg, ts)
    TextRect.center = (((x + (w / 2))), (y + (h / 2)))
    gamedisplay.blit(TextSurf, TextRect)

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
    gamedisplay.fill(black)
    # obj_()
    while y <= display_height:
        while x < (display_width/5)*4:
            if t % 2 == 0:
                gamedisplay.fill(red, (x, y, display_width/33, display_height/20))
                t += 1
                x += (display_width/33)
            else:
                gamedisplay.fill(white, (x, y, display_width/33, display_height/20))
                t += 1
                x += (display_width/33)
        else:
            t += 1
            y += (display_height/20)
            x = display_width / 5


    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            (mousex, mousey) = pygame.mouse.get_pos()

    pygame.display.update()
    gameloop()


def main_menu():
    in_main_menu = True
    while in_main_menu:
        gamedisplay.blit(bg_image,(0, 0))


        TextSurf, TextRect = text_objects("BattlePort", largeText)
        TextRect.center = ((display_width/2), (display_height/2))
        gamedisplay.blit(TextSurf, TextRect)

        button("Play", display_width/6, 450, 200, 120, blue, bright_blue, mediumText)
        button("Quit", display_width/6*4, 450, 200, 120, red, bright_red, mediumText)
        button("Options", display_width/6*2.4, 450, 250, 120, silver, dark_silver, mediumText)

        mouse = pygame.mouse.get_pos()

        pygame.display.update()
        clock.tick(15)

        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if (display_width/6) + 200 > mouse[0] > (display_width/6) and 450 + 120 > mouse[1] > 450:
                    board_gen()
                if (display_width/6*4) + 200 > mouse[0] > (display_width/6*4) and 450+120 > mouse[1] > 450:
                    pygame.quit()
                    sys.exit()
                if (display_width/6*2.4) + 200 > mouse[0] > (display_width/6*2.4) and 450 + 120 > mouse[1] > 450:
                    options() # moet nog options menu makne

def paused():
    pause = True
    while pause:

        TextSurf, TextRect = text_objects("Pause", largeText)
        TextRect.center = ((display_width / 2), (display_height / 2))
        gamedisplay.blit(TextSurf, TextRect)

        button("Play", display_width / 6, 450, 200, 120, blue, bright_blue, mediumText)
        button("Quit", display_width / 6 * 4, 450, 200, 120, red, bright_red, mediumText)
        button("Main menu", display_width / 6 * 2.21, 450, 330, 120, silver, dark_silver, mediumText)

        mouse = pygame.mouse.get_pos()


        pygame.display.update()
        clock.tick(15)

        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if (display_width / 6) + 200 > mouse[0] > (display_width / 6) and 450 + 120 > mouse[1] > 450:
                    board_gen()
                if (display_width / 6 * 4) + 200 > mouse[0] > (display_width / 6 * 4) and 450 + 120 > mouse[1] > 450:
                    pygame.quit()
                    sys.exit()
                if (display_width/6*2.4) + 200 > mouse[0] > (display_width/6*2.4) and 450 + 120 > mouse[1] > 450:
                    main_menu()

def options():
    options = True
    while options:

        gamedisplay.blit(gamedisplay,(0,0,0,200))
        TextSurf, TextRect = text_objects("options", largeText)
        TextRect.center = ((display_width / 2), (display_height / 10))
        gamedisplay.blit(TextSurf, TextRect)

        button("480p", display_width/6, display_height/6, display_width/10.66, display_height/6, red, bright_red, mediumText)
        button("720p", display_width/6*3, display_height/6, display_width/10.66, display_height/6, red, bright_red, mediumText)
        button("1080p", display_width/6*5,display_height/6, display_width/10.66, display_height/6, red, bright_red, mediumText)

        mouse = pygame.mouse.get_pos()

        pygame.display.update()
        clock.tick(15)

def gameloop():
    crashed = False

    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_p:
                    paused()
            yo_movement(display_width/2, display_height/2)
            print(event)
            pygame.display.update()
    clock.tick(5)


main_menu()
