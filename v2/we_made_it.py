import pygame as pg
import sys
import random
from settings import *
from ship import *

class Game:
    def __init__(self):
        pg.init()
        pg.font.init()
        pg.mixer.init()

        self.screen = pg.display.set_mode((width, height))
        pg.display.set_caption(Title)
        self.clock = pg.time.Clock()
        pg.key.set_repeat(500, 100)
        self.load_data()
        self.running= True

    def load_data(self):
        pass

    def new(self):
        # initialize all variables and do all the setup for a new game
        self.all_sprites = pg.sprite.Group()
        self.player_sprites = pg.sprite.Group()
        self.wall = pg.sprite.Group()
        self.player_counter = 1
        self.player1 = Player(self, 10, 10,4)
        self.player2 = Boat(self, 11, 10,4)
        self.boat = Boat(self, 11, 5,4)
        for x in range(5, 27):
            Wall(self, x, 1) and Wall(self, x, 22)
        for y in range(1, 22):
            Wall(self, 5, y) and Wall(self, 26, y)
        self.paused = False
        self.run()

    def run(self):
        # game loop - set self.playing = False to end the game
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(fps) / 1000
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
        # update portion of the game loop
        self.all_sprites.update()
        self.player_sprites.update()

    def instructions(self):
        self.screen.blit(instbg_image, (0, 0))


        pg.display.update()

    def draw_grid(self):
        for x in range(6 * tilesize, width - 5 * tilesize, tilesize):
            pg.draw.line(self.screen, light_grey, (x, 2 * tilesize), (x, height - 2 * tilesize))
        for y in range(2 * tilesize, height - 1 * tilesize, tilesize):
            pg.draw.line(self.screen, light_grey, (6 * tilesize, y), (width - 6 * tilesize, y))

        """self.screen.blit(board_image, (0, 0))
        self.screen.blit(map_image, (width / 5, height / 10))

        self.button(menu1_image, menu2_image, 100, 100, 50, 50)
        self.screen.blit(kaartn_image, (20, 20))
        self.screen.blit(kaarts_image, (700, 20))

        mouse = pg.mouse.get_pos()
        if 700 + 80 > mouse[0] > 700 and 20 + 160 > mouse[1] > 20:
            self.screen.blit(kaart1, (600, 20))
        if 20 + 80 > mouse[0] > 20 and 20 + 160 > mouse[1] > 20:
            self.screen.blit(kaart2, (70, 20))

        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN:
                if 100 + 50 > mouse[0] > 100 and 100 + 50 > mouse[1] > 100:
                    g.main_menu()"""

    def draw(self):
        self.screen.fill(dark_grey)
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

        pg.display.flip()

    """def options(self):
            self.screen.fill(aqua)
            TextSurf, TextRect = text_objects("options", pg.font.Font('freesansbold.ttf', 60))
            TextRect.center = ((width / 2), (height/ 10))
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

            for event in pg.event.get():
                if event.type == pg.MOUSEBUTTONDOWN:
                    if (width / 8 * 2) + width / 6 > mouse[0] > (width / 8 * 2) and height\
                                / 6 + height\
                                / 6 > mouse[1] > height\
                                / 6:
                        pg.transform.scale(self.screen, (640, 480))
                        pg.display.set_mode((640, 480))
                        height = 480
                        width = 640
                    if (width / 8 * 4) + width / 6 > mouse[0] > (width / 8 * 4) and height / 6 + height / 6 > mouse[1] > height / 6:
                        pg.display.set_mode((1280, 720))
                        pg.transform.scale(self.screen, (1280, 720))
                        width = 1280
                        height = 720
                    if (width / 8 * 6) + width / 6 > mouse[0] > (width / 8 * 6) and height / 6 + height\
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
                            pg.quit()"""

    def events(self):
        # catch all events here
        if self.player1.hp > 0 and self.player2.hp > 0:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.quit()
                if event.type == pg.KEYUP:
                    if event.key == pg.K_ESCAPE:
                        self.quit()
                    if event.key == pg.K_p:
                        self.paused = not self.paused
                    if event.key == pg.K_LEFT:
                        if self.player_counter == 1:
                            self.player1.move(dx=-1)
                            break
                        if self.player_counter == 2:
                            self.player2.move(dx=-1)
                            break
                    if event.key == pg.K_RIGHT:
                        if self.player_counter == 1:
                            self.player1.move(dx=1)
                            break
                        if self.player_counter == 2:
                            self.player2.move(dx=1)
                            break
                    if event.key == pg.K_UP:
                        if self.player_counter == 1:
                            self.player1.move(dy=-1)
                            break
                        if self.player_counter == 2:
                            self.player2.move(dy=-1)
                            break
                    if event.key == pg.K_DOWN:
                        if self.player_counter == 1:
                            self.player1.move(dy=1)
                            break
                        if self.player_counter == 2:
                            self.player2.move(dy=1)
                            break
                if event.type == pg.KEYDOWN:
                    if  event.key == pg.K_t and self.player_counter == 2:
                        self.player_counter = 1
                        print(self.player_counter)
                    elif event.key == pg.K_t and self.player_counter == 1:
                        self.player_counter = 2
                        print(self.player_counter)

    def main_menu(self):
        in_main_menu = True
        while in_main_menu:
            self.screen.blit(bg_image, (0, 0))
            self.screen.blit(title_image, (width / 5, width / 8))

            self.button(start_image1, start_image2, 600, 400, 150, 50)
            self.button(score1_image, score2_image, 600, 500, 150, 50)
            self.button(help1_image, help2_image, 600, 450, 150, 50)

            mouse = pg.mouse.get_pos()

            pg.display.update()

            for event in pg.event.get():
                if event.type == pg.MOUSEBUTTONDOWN:
                    if 600 + 150 > mouse[0] > 600 and 400 + 50 > mouse[1] > 150:
                        g.new()
                    if 600 + 150 > mouse[0] > 600 and 500 + 50 > mouse[1] > 150:
                        pass  # options
                    if 600 + 150 > mouse[0] > 600 and 450 + 50 > mouse[1] > 150:
                        g.instructions()
                if event.type == pg.QUIT:
                    g.quit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        g.quit()

    def show_go_screen(self):
        pass

    def Score(self):
        pass

# create the game object
g = Game()
g.main_menu()
while g.running:
    g.new()
    g.run()
    g.main_menu

pg.quit()

