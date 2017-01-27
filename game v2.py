#import required modules
import pygame
import time
import sys
#define colors
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
black = (0,0,0)

#grootte van het scherm
width = 800
heigth = 600
size = (width,heigth)


class Game:
    def __init__(self):
        pygame.init()
        self.gameExit = False
        self.screen = pygame.display.set_mode((size),pygame.FULLSCREEN)
        pygame.display.set_caption("Battleport beta")
        self.intro_game = IntroGame(self)
        self.game_main= GameMain(self)
        self.pause_menu = PauseMenu(self)
        self.state = self.intro_game

    def set_state(self, state):
        self.state = state

    def draw(self):
        self.state.draw(self.screen)
        pygame.display.flip()


    #loop voor het laten runnen van het spel
    def loop_of_game(self):
        while not self.gameExit:
            self.draw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
            #self.state = self.state.update(...)



#Beginscherm
class IntroGame:
    def __init__(self, game):
        # sprites
        self.game = game
        self.bg = pygame.image.load("check.png")
        self.bg = pygame.transform.scale(self.bg, size)
        self.pbuttom = pygame.image.load("Pl.png")
        self.pbuttom = pygame.transform.scale(self.pbuttom, [150, 50])
        self.hbuttom = pygame.image.load("hscore.png")
        self.hbuttom = pygame.transform.scale(self.hbuttom, [150, 50])
        self.rbuttom = pygame.image.load("Ins.png")
        self.rbuttom = pygame.transform.scale(self.rbuttom, [150, 50])
        self.title = pygame.image.load("titel.png")
        self.title = pygame.transform.scale(self.title,[471,78])
        self.hoover = pygame.image.load("arrow.png")
        self.hoover = pygame.transform.scale(self.hoover, [155, 45])
        self.hoover1 = pygame.image.load("arrow.png")
        self.hoover1 = pygame.transform.scale(self.hoover, [155, 45])

    def draw(self,screen):
        screen.blit(self.bg,[0,0])
        screen.blit(self.title,(width/5,width/8))
        mouse_button_pressed(600, 400, 130, 30, screen, self.pbuttom, self.hoover, lambda: self.game.set_state(self.game.game_main))
        mouse_button_pressed(600, 450, 130, 30, screen, self.hbuttom, self.hoover1)
        mouse_button_pressed(600, 500, 130, 30, screen, self.rbuttom, self.hoover1)

#Scherm na op start the hebben gedrukt
class GameMain:
    def __init__(self, game):
        self.game = game
        self.side = pygame.image.load("menu2.png")
        self.side = pygame.transform.scale(self.side,size)
        self.board = pygame.image.load("gamemap.png")
        self.board = pygame.transform.scale(self.board, [480,480])
        self.pbutton = pygame.image.load("menu.png")
        self.pbutton = pygame.transform.scale(self.pbutton, [50, 50])
        self.hoover = pygame.image.load("circle.png")
        self.hoover = pygame.transform.scale(self.hoover, [50, 50])


    def draw(self,screen):
        screen.blit(self.side,[0,0])
        screen.blit(self.board,[width/5,heigth/10])
        mouse_button_pressed(100, 100, 50, 50, screen, self.pbutton, self.hoover,lambda: self.game.set_state(self.game.pause_menu))


class Higscorelist:
    def __init__(self):
        # sprites
        pass

class GamerulesList:
    def __init__(self):
        # sprites
        pass

class PauseMenu:
    def __init__(self, game):
        # sprites
        self.game = game
        self.bg = pygame.image.load("pauze.png")
        self.bg = pygame.transform.scale(self.bg, size)
        self.pbuttom = pygame.image.load("cont.png")
        self.pbuttom = pygame.transform.scale(self.pbuttom, [240, 120])
        self.hbuttom = pygame.image.load("hscore.png")
        self.hbuttom = pygame.transform.scale(self.hbuttom, [150, 50])
        self.rbuttom = pygame.image.load("Ins.png")
        self.rbuttom = pygame.transform.scale(self.rbuttom, [150, 50])
        self.title = pygame.image.load("pauzet.png")
        self.title = pygame.transform.scale(self.title,[471,78])
        self.hoover = pygame.image.load("contb.png")
        self.hoover = pygame.transform.scale(self.hoover, [280, 90])        
        self.hoover1 = pygame.image.load("arrow.png")
        self.hoover1 = pygame.transform.scale(self.hoover, [155, 45])

    def draw(self,screen):
        screen.blit(self.bg,[0,0])
        screen.blit(self.title,(width/5,width/8))
        mouse_button_pressed(275, 200, 240, 120, screen, self.pbuttom, self.hoover, lambda: self.game.set_state(self.game.game_main))
        mouse_button_pressed(325, 300, 150, 50, screen, self.hbuttom, self.hoover1, lambda :self.game.set_state(self.game.intro_game))
        mouse_button_pressed(325, 350, 150, 50, screen, self.rbuttom, self.hoover1)

def mouse_button_pressed(x,y,w,h,screen,image_original,image_hover,action=None):
    click=pygame.mouse.get_pressed()
    mouse = pygame.mouse.get_pos()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        screen.blit(image_original, [x, y])
        screen.blit(image_hover,[x,y])
        if click[0]==1 and action != None:
            action()
    else:
        screen.blit(image_original,[x,y])

def text_objects(text,font):
    textSurface = font.render (text,True, black)
    return textSurface, textSurface.get_rect()

def message_to_screen(text):
    largeText = pygame.font.Font("freesansbold.ttf",50)
    textsuf , textrect = text_objects(text,largeText)
    textrect.center = ((width/2),(heigth/2))

#sluiten van game via kruisje


def run ():
    game = Game()
    game.loop_of_game()

run()
