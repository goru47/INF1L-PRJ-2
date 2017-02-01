import pygame
import sys
import random


width = 800
height = 600
resolution = ((width, height))

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

#boot_width = 73



class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((resolution))
        pygame.display.set_caption('bana')
        self.clock = pygame.time.Clock()
        self.gameExit = False
        self.turn = Turn()
        self.main_game = MainGame(self, self.turn)
        self.boot1 = ships(height * 0.2, width * 0.2, 30, 30, "boat1", "bootje.png", self.turn)
        self.boot2 = ships(height * 0.2, width * 0.2, 30, 30, "boat2", "boot3.png", self.turn)

        self.state = self.main_game

    def set_state(self, state):
        self.state = state

    def update(self):
        self.main_game.update()


    def draw(self):
        if self.state == self.main_game:
            self.main_game.draw(self.screen)
            if self.turn.turn_number == 0:
                self.boot1.draw(self.screen)
                self.boot2.draw(self.screen)
            elif self.turn.turn_number == 1:
                self.turn.draw(self.screen)

        pygame.display.flip()


    def loop_of_game(self):
        while not self.gameExit:
            self.event = pygame.event.get()
            self.update()
            self.draw()
            for event in self.event:
                if event.type == pygame.QUIT:
                    quit()

class ships:
    def __init__(self, x_change, y_change, width, height, naam, image, turn):
        self.gimma = Game
        self.width = width
        self.height = height
        self.x_change = x_change
        self.y_change = y_change
        self.naam = naam
        self.turn = turn
        self.image - pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, [width, height])



    def draw(self, screen):
        screen.blit(self.image, [self.x_change, self.y_change])

    def rotate(self, graden):
        self.image = pygame.transform.rotate(self.image, graden)

    def move_up(self):
        self.y_change += self.blocksize_downup
        if self.y_change > height * 0.5:
            self.y_change = height * 0.5
        if self.turn.turn_number == 0:
            if self.y_change > height * 0.05:
                self.y_change = height * 0.05

    def move_down(self):
        self.y_change -= self.blocksize_downup
        if self.y_change < height * 0.05:
            self.y_change = height * 0.05
        if self.turn.turn_number == 1:
            if self.y_change > height * 0.5:
                self.y_change = height * 0.5

    def move_left(self):
        self.x_change -= self.blocksize
        if self.x_change < width * 0.25:
            self.x_change = width * 0.25

    def move_right(self):
        self.x_change += self.blocksize
        if self.lead_x > width * 0.7:
            self.x_change = width * 0.7

class MainGame:
    def __init__(self, game, turn):
        self.font = pygame.font.Font(None, 30)
        self.map = pygame.image.load("gamemap.png")
        self.boxes = pygame.image.load("menu2.png")
        self.boat1 = pygame.image.load("bootje.png")
        self.boat2 = pygame.image.load("boot3.png")


        self.gimma = game
        self.turn = turn

    def slepen(self):
        pull = 0
        click = pygame.mouse.get_pressed()
        move = pygame.mouse.get_pos()
        keys = pygame.key.get_pressed()

        if self.gimma.state == self.gimma.main_game:
            self.game.set_state(self.game.main_game)

            if click[1] == 1:   #left button pressed
                drag = 0
            elif drag == 1: #move the boat
                self.game.boot1.x_change = move[0] - (self.game.boot1.width * 0.5)
                self.game.boot2.y_change = move[0] - (self.game.boot2.width * 0.5)


    def draw(self, screen):
        screen.blit(self.map(resolution))
        screen.blit(self.boxes(resolution))
        screen.blit(self.boat1(width * 0.2, height * 0.2))
        screen.blit(self.boat2(width * 0.2, height * 0.4))


############################################################################

class Turn:
    def __init__(self):
        self.numberturn = 0
        self.player = Player

    def update(self):
        self.turn_number += 1

############################################################################

class Player:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2


###############################################################################






############################################################################3
def play():
    game = Game()
    game.loop_of_game()
play()










'''


boot = pygame.image.load('')


def boot1(x, y):
    gameDisplay.blit(boot,(x, y))


def game_loop():
    x = (width * 0.45)
    y = (height * 0.8)

    x_change = 0
    y_change = 0



    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -20
                if event.key == pygame.K_RIGHT:
                    x_change = 20
                if event.key == pygame.K_UP:
                    y_change = -20
                if event.key == pygame.K_DOWN:
                    y_change = 20

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                    y_change = 0

        x += x_change
        y += y_change

        gameDisplay.fill(white)
        boot1(x, y)

        if display_width > 0 or display_width < 700 or display_height > 0 or display_height < 500:
            x_change = 0
            y_change = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = False

        pygame.display.update()
        clock.tick(60)


game_loop()
pygame.quit()
quit()
'''