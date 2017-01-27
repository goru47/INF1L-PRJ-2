import pygame as pg
import random
import sys
from settings import *
from pygame.locals import *

class Game:
    def __init__(self):
        # initialize game window, etc
        pg.init()
        pg.font.init()
        pg.mixer.init()

        self.screen = pg.display.set_mode((width, height), pg.FULLSCREEN)
        pg.display.set_caption(Title)
        self.clock = pg.time.Clock()
        self.running = True

    def load_state(self):
        pass

    def new(self):
        # start a new game
        self.all_sprites = pg.sprite.Group()
        self.ship = Ship(self, 10, 10)
        self.paused = False
        self.run()

    def run(self):
        # Game loop
        self.playing = True
        while self.playing:
            self.clock.tick(fps)
            self.events()
            if not self.paused:
                self.update()
            self.draw()

    def button(self, naam1, naam2, x, y, w, h):
        # image, image highlight, x pos, y pos, width, height
        mouse = pg.mouse.get_pos()

        # als x pos + width groter
        if x + w > mouse[0] > x and y + h > mouse[1] > y:
            self.screen.blit(naam1, (x, y))
            self.screen.blit(naam2, (x, y))
        else:
            self.screen.blit(naam1, (x, y))

    def quit(self):
        pg.quit()
        sys.exit()

    def update(self):
        # Game loop - Update
        self.all_sprites.update()

    def instructions(self):
        self.screen.blit(instbg_image, (0, 0))


        pg.display.update()

    def board_gen(self):
        t = 0
        x = width / 5
        y = 0
        self.screen.fill(black)
        # obj_()
        while y <= height\
                :
            while x < (width / 5) * 4:
                if t % 2 == 0:
                    self.screen.fill(red, (x, y, width / 33, height
                                           / 20))
                    t += 1
                    x += (width / 33)
                else:
                    self.screen.fill(white, (x, y, width / 33, height
                                             / 20))
                    t += 1
                    x += (width / 33)
            else:
                t += 1
                y += (height
                      / 20)
                x = width / 5

        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN:
                (mousex, mousey) = pg.mouse.get_pos()

        pg.display.update()
        self.events()

    def draw_grid(self):
        for x in range(0, width, tilesize):
            pg.draw.line(self.screen, light_grey, (x, 0), (x, height))
        for y in range(0, height, tilesize):
            pg.draw.line(self.screen, light_grey, (0, y), (width, y))

        self.screen.blit(board_image, (0, 0))
        self.screen.blit(map_image, (width / 5, height / 10))
        self.button(menu1_image, menu2_image, 170, 10, 50, 50)
        self.screen.blit(kaartn_image, (20, 20))
        self.screen.blit(kaarts_image, (665, 20))
        self.screen.blit(boot3, (244, 250))
        self.screen.blit(boot2, (294, 300))
        self.screen.blit(boot1, (244, 350))
        
        mouse = pg.mouse.get_pos()
        if 700 + 80 > mouse[0] > 700 and 20 + 160 > mouse[1] > 20:
            self.screen.blit(kaart1, (600, 20))
        if 20 + 80 > mouse[0] > 20 and 20 + 160 > mouse[1] > 20:
            self.screen.blit(kaart2, (70, 20))



        mouse = pg.mouse.get_pos()
        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN:
                if 170 + 50 > mouse[0] > 170 and 10 + 50 > mouse[1] > 10:
                    game.main_menu()




    def draw(self):
        # Game loop - draw
        self.draw_grid()
        self.all_sprites.draw(self.screen)
        if self.paused:
            self.screen.blit(pause_image, (0, 0))
            self.screen.blit(pauzet_image, (width / 5, width / 8))
            self.button(help1_image, help2_image, 600, 450, 150, 50)
            mouse = pg.mouse.get_pos()
            if 600 + 130 > mouse[0] > 600 and 450 + 50 > mouse[1] > 50:
                self.screen.blit(instbg_image, (0, 0))
                self.screen.blit(inst1_image, (100, 0))

        pg.display.update()

    def options(self):
            self.screen.fill(aqua)
            TextSurf, TextRect = text_objects("options", pg.font.Font('freesansbold.ttf', 60))
            TextRect.center = ((width / 2), (height / 10))
            self.screen.blit(TextSurf, TextRect)

            self.button("resolution", width / 24, height / 6, width / 6, height / 6, red,red, pg.font.Font('freesansbold.ttf', 20))
            self.button("480p", width / 8 * 2, height / 6, width / 6, height / 6, silver,dark_silver, pg.font.Font('freesansbold.ttf', 20))
            self.button("720p", width / 8 * 4, height / 6, width / 6, height / 6, silver,dark_silver, pg.font.Font('freesansbold.ttf', 20))
            self.button("1080p", width / 8 * 6, height / 6, width / 6, height / 6, silver,dark_silver, pg.font.Font('freesansbold.ttf', 20))

            self.button("sound", width / 24, height
                        / 6 * 2.5, width / 6, height
                        / 6, red,red, pg.font.Font('freesansbold.ttf', 20))
            self.button("off", width / 8 * 2, height
                        / 6 * 2.5, width / 6, height
                        / 6,silver, dark_silver, pg.font.Font('freesansbold.ttf', 20))
            self.button("50%", width / 8 * 4, height
                        / 6 * 2.5, width / 6, height
                        / 6,silver, dark_silver, pg.font.Font('freesansbold.ttf', 20))
            self.button("100%", width / 8 * 6, height
                        / 6 * 2.5, width / 6, height
                        / 6,silver, dark_silver, pg.font.Font('freesansbold.ttf', 20))

            self.button("window/full", width / 8, height
                        / 6 * 4, width / 4, height
                        / 6,silver, dark_silver, pg.font.Font('freesansbold.ttf', 20))
            self.button("main menu", width / 8 * 3, height
                        / 6 * 4, width / 4, height
                        / 6,silver, dark_silver, pg.font.Font('freesansbold.ttf', 20))
            self.button("exit", width / 8 * 5, height
                        / 6 * 4, width / 4, height
                        / 6, silver,dark_silver, pg.font.Font('freesansbold.ttf', 20))

            mouse = pg.mouse.get_pos()
            pg.display.update()
            self.clock.tick(30)

            for event in pg.event.get():
                if event.type == pg.MOUSEBUTTONDOWN:
                    if (width / 8 * 2) + width / 6 > mouse[0] > (width / 8 * 2) and height\
                            / 6 + height\
                            / 6 > mouse[1] > height\
                            / 6:
                        pg.transform.scale(self.screen, (640, 480))
                        pg.display.set_mode((640, 480))
                        height\
                            = 480
                        width = 640
                    if (width / 8 * 4) + width / 6 > mouse[0] > (width / 8 * 4) and height\
                            / 6 + height\
                            / 6 > mouse[1] > height\
                            / 6:
                        pg.display.set_mode((1280, 720))
                        pg.transform.scale(self.screen, (1280, 720))
                        width = 1280
                        height\
                            = 720
                    if (width / 8 * 6) + width / 6 > mouse[0] > (width / 8 * 6) and height\
                            / 6 + height\
                            / 6 > mouse[1] > height\
                            / 6:
                        pg.display.set_mode((1920, 1080))
                        pg.transform.scale(self.screen, (1920, 1080))
                        width = 1920
                        height\
                            = 1080
                    if (width / 8 * 2) + width / 6 > mouse[0] > (width / 8 * 2) and height\
                            / 6 * 2.5 + height\
                            / 6 > mouse[1] > height\
                            / 6 * 2.5:
                        pass  # Sounds options worden later toegevoegd
                    if (width / 8 * 4) + width / 6 > mouse[0] > (width / 8 * 4) and height\
                            / 6 * 2.5 + height\
                            / 6 > mouse[1] > height\
                            / 6 * 2.5:
                        pass  # Sounds options worden later toegevoegd
                    if (width / 8 * 6) + width / 6 > mouse[0] > (width / 8 * 6) and height\
                            / 6 * 2.5 + height\
                            / 6 > mouse[1] > height\
                            / 6 * 2.5:
                        pass  # Sounds options worden later toegevoegd
                    if (width / 8) + width / 4 > mouse[0] > (width / 8) and height\
                            / 6 * 4 + height\
                            / 6 > mouse[1] > height\
                            / 6 * 4:
                        pg.display.set_mode(FULLSCREEN)
                    if (width / 8 * 3) + width / 4 > mouse[0] > (width / 8 * 3) and height\
                            / 6 * 4 + height\
                            / 6 > mouse[1] > height\
                            / 6 * 4:
                        self.main_menu()
                    if (width / 8 * 5) + width / 4 > mouse[0] > (width / 8 * 5) and height\
                            / 6 * 4 + height\
                            / 6 > mouse[1] > height\
                            / 6 * 4:
                        pg.quit()

    def events(self):
        # Game loop - events
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()
                if event.key == pg.K_p:
                    self.paused = not self.paused
                # boot movement
                if event.key == pg.K_LEFT:
                    self.ship.move(dx=-1)
                if event.key == pg.K_RIGHT:
                    self.ship.move(dx=1)
                if event.key == pg.K_DOWN:
                    self.ship.move(dy=1)
                if event.key == pg.K_UP:
                    self.ship.move(dy=-1)

    def main_menu(self):
        # while in mainmenu
        in_main_menu = True
        while in_main_menu:
            self.screen.blit(bg_image, (0, 0))
            self.screen.blit(title_image, (width/5, width/8))

            self.button(start_image1, start_image2, 600, 400, 150, 50)
            self.button(score1_image, score2_image, 600, 500, 150, 50)
            self.button(help1_image, help2_image, 600, 450, 150, 50)

            mouse = pg.mouse.get_pos()

            pg.display.update()
            self.clock.tick(15)

            for event in pg.event.get():
                if event.type == MOUSEBUTTONDOWN:
                    if 600 + 150 > mouse[0] > 600 and 400 + 50 > mouse[1] > 150:
                        game.new()
                    if 600 + 150 > mouse[0] > 600 and 500 + 50 > mouse[1] > 150:
                        pass        # options
                    if 600 + 150 > mouse[0] > 600 and 450 + 50 > mouse[1] > 150:
                        game.instructions()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        game.quit()


    def show_go_screen(self):
        # game over/continue
        pass

    def Score(self):
        pass

game = Game()
game.main_menu()
while game.running:
    game.new()
    game.main_menu()

pg.quit()
