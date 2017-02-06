import pygame
import sys
from pygame.locals import *
import random
import math
from settings import *
from ship import *

# initialize pygame
pygame.init()
pygame.font.init()




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

#middle of the screen
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
bg_game = pygame.image.load("canvas.png")
bg_game = pygame.transform.scale(bg_game, (display_width, display_height))
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

class game:
    def __init__(self):
        pygame.init()
        #resolution
        dis_width  = 1280
        dis_height = 720
        resolution = (dis_width,dis_height)

        self.screen = pygame.display.set_mode(resolution)

        self.largetext = pygame.font.Font('freesansbold.ttf', 115)
        self.mediumtext = pygame.font.Font('freesansbold.ttf', 60)
        self.smalltext = pygame.font.Font('freesansbold.ttf', 20)



#class boot:
#    def __init__(self,x,y,hp,width,length):
#        self.x = x
#        self.y = y
#        self.hp = hp
#        self.width = width
#        self.length = length
#        self.
#    def updoot:
#        action = pygame.mouse.get_pos()
#
#        if x + width > action[0] > x and y + length:


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

def board_gen(display_width,display_height):
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
    gameloop(display_width, display_height)


def draw_grid():
    gamedisplay.fill(aqua)

    for x in range(0, display_width, tilesize):
        pg.draw.line(gamedisplay, light_grey, (x, 0), (x, display_height))
    for y in range(0, display_height, tilesize):
        pg.draw.line(gamedisplay, light_grey, (0, y), (display_width, y))

    gamedisplay.blit(bg_game, (0, 0))
    Boat.draw(gamedisplay)

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            (mousex, mousey) = pygame.mouse.get_pos()

    pygame.display.update()
    gameloop(display_width, display_height)

def main_menu(display_width,display_height):
    in_main_menu = True
    while in_main_menu:
        gamedisplay.blit(bg_image,(0, 0))


        TextSurf, TextRect = text_objects("BattlePort", mediumText)
        TextRect.center = ((display_width/2), (display_height/2))
        gamedisplay.blit(TextSurf, TextRect)

        button("Play", display_width/6, display_height/1.6, display_width/6.4, display_height/6, blue, bright_blue, smallText)
        button("Quit", display_width/6*4, display_height/1.6, display_width/6.4, display_height/6, red, bright_red, smallText)
        button("Options", display_width/6*2.4, display_height/1.6, display_width/5.12, display_height/6, silver, dark_silver, smallText)

        mouse = pygame.mouse.get_pos()

        pygame.display.update()
        clock.tick(15)

        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if (display_width/6) + display_width/6.4 > mouse[0] > (display_width/6) and display_height/1.6 + display_height/6 > mouse[1] > display_height/1.6:
                    draw_grid()
                if (display_width/6*4) + display_width/6.4 > mouse[0] > (display_width/6*4) and display_height/1.6+display_height/6 > mouse[1] > display_height/1.6:
                    pygame.quit()
                    sys.exit()
                if (display_width/6*2.4) + display_width/5.12 > mouse[0] > (display_width/6*2.4) and display_height/1.6+ display_height/6 > mouse[1] > display_height/1.6:
                    options(display_width,display_height) # moet nog options menu makne

def paused(display_width,display_height):
    pause = True
    while pause:

        TextSurf, TextRect = text_objects("Pause", largeText)
        TextRect.center = ((display_width / 2), (display_height / 2))
        gamedisplay.blit(TextSurf, TextRect)

        button("Play", display_width / 6, display_height/1.6, display_width/6.4, display_height/6, blue, bright_blue, mediumText)
        button("Quit", display_width / 6 * 4, display_height/1.6 , display_width/6.4, display_height/6, red, bright_red, mediumText)
        button("Main menu", display_width / 6 * 2.21, display_height/1.6, display_width/3.87, display_height/6, silver, dark_silver, mediumText)

        mouse = pygame.mouse.get_pos()


        pygame.display.update()
        clock.tick(15)

        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if (display_width / 6) + 200 > mouse[0] > (display_width / 6) and display_height/1.6 + display_height/6 > mouse[1] > display_height/1.6:
                    draw_grid()
                if (display_width / 6 * 4) + 200 > mouse[0] > (display_width / 6 * 4) and display_height/1.6 + display_height/6 > mouse[1] > display_height/1.6:
                    pygame.quit()
                    sys.exit()
                if (display_width/6*2.4) + 200 > mouse[0] > (display_width/6*2.4) and display_height/1.6 + display_height/6 > mouse[1] > display_height/1.6:
                    main_menu(display_width,display_height)

def options(display_width,display_height):
    options = True
    while options:
        gamedisplay.fill(aqua)
        TextSurf, TextRect = text_objects("options", mediumText)
        TextRect.center = ((display_width / 2), (display_height / 10))
        gamedisplay.blit(TextSurf, TextRect)

        button("resolution", display_width/24, display_height/6, display_width/6, display_height/6, red, red, smallText)
        button("480p", display_width/8*2, display_height/6, display_width/6, display_height/6, silver, dark_silver, smallText)
        button("720p", display_width/8*4, display_height/6, display_width/6, display_height/6, silver, dark_silver, smallText)
        button("1080p", display_width/8*6,display_height/6, display_width/6, display_height/6, silver, dark_silver, smallText)

        button("sound", display_width/24, display_height/6*2.5, display_width/6, display_height/6, red, red, smallText)
        button("off", display_width/8*2, display_height/6*2.5, display_width/6, display_height/6, silver, dark_silver, smallText)
        button("50%", display_width/8*4, display_height/6*2.5, display_width/6, display_height/6, silver, dark_silver, smallText)
        button("100%", display_width/8*6,display_height/6*2.5, display_width/6, display_height/6, silver, dark_silver, smallText)

        button("window/full", display_width/8, display_height/6*4, display_width/4, display_height/6, silver, dark_silver, smallText)
        button("main menu", display_width/8*3, display_height/6*4, display_width/4, display_height/6, silver, dark_silver, smallText)
        button("exit", display_width/8*5,display_height/6*4, display_width/4, display_height/6, silver, dark_silver, smallText)



        mouse = pygame.mouse.get_pos()
        pygame.display.update()
        clock.tick(15)

        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if (display_width/8*2)+display_width/6 > mouse[0] > (display_width/8*2) and display_height/6 + display_height/6 > mouse[1] > display_height/6:
                    pygame.transform.scale(gamedisplay,(640,480))
                    pygame.display.set_mode((640,480))
                    display_height= 480
                    display_width = 640
                if (display_width/8*4)+display_width/6 > mouse[0] > (display_width/8*4) and display_height/6 + display_height/6 > mouse[1] > display_height/6:
                    pygame.display.set_mode((1280,720))
                    pygame.transform.scale(gamedisplay,(1280,720))
                    display_width = 1280
                    display_height = 720
                if (display_width/8*6)+display_width/6 > mouse[0] > (display_width/8*6) and display_height/6 + display_height/6 > mouse[1] > display_height/6:
                    pygame.display.set_mode((1920,1080))
                    pygame.transform.scale(gamedisplay,(1920,1080))
                    display_width = 1920
                    display_height = 1080
                if (display_width/8*2)+display_width/6 > mouse[0] > (display_width/8*2) and display_height/6*2.5 + display_height/6 > mouse[1] > display_height/6*2.5:
                    pass # Sounds options worden later toegevoegd
                if (display_width/8*4)+display_width/6 > mouse[0] > (display_width/8*4) and display_height/6*2.5 + display_height/6 > mouse[1] > display_height/6*2.5:
                    pass # Sounds options worden later toegevoegd
                if (display_width/8*6)+display_width/6 > mouse[0] > (display_width/8*6) and display_height/6*2.5 + display_height/6 > mouse[1] > display_height/6*2.5:
                    pass # Sounds options worden later toegevoegd
                if (display_width/8)+display_width/4 > mouse[0] > (display_width/8) and display_height/6*4 + display_height/6 > mouse[1] > display_height/6*4:
                    pygame.display.set_mode(fullscreen)
                if (display_width/8*3)+display_width/4 > mouse[0] > (display_width/8*3) and display_height/6*4 + display_height/6 > mouse[1] > display_height/6*4:
                    main_menu(display_width,display_height)
                if (display_width/8*5)+display_width/4 > mouse[0] > (display_width/8*5) and display_height/6*4 + display_height/6 > mouse[1] > display_height/6*4:
                    pygame.quit()

def gameloop(display_width,display_height):
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
                    paused(display_width, display_height)
            yo_movement(display_width/2, display_height/2)
            print(event)
            pygame.display.update()
    clock.tick(5)


main_menu(display_width,display_height)