import pygame as pg
import sys
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
        self.wall = pg.sprite.Group()
        self.player = Player(self, 10, 10)
        self.boat = Boat(self, 11, 5)
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
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()
                if event.key == pg.K_p:
                    self.paused = not self.paused
                if event.key == pg.K_LEFT:
                    self.player.move(dx=-1)
                if event.key == pg.K_RIGHT:
                    self.player.move(dx=1)
                if event.key == pg.K_UP:
                    self.player.move(dy=-1)
                if event.key == pg.K_DOWN:
                    self.player.move(dy=1)

    def how_to_play(self):
        htp = True
        while htp:
            self.screen.blit(htpbg_image, (0, 0))

            self.button(htphelp1_image1, start_image2, 140, 100, 150, 50)
            self.button(htphelp2_image1, start_image2, 140, 160, 150, 50)
            self.button(htphelp3_image1, start_image2, 140, 220, 150, 50)
            self.button(htphelp4_image1, start_image2, 140, 280, 150, 50)
            self.button(htphelp5_image1, start_image2, 684, 100, 150, 50)
            self.button(htphelp6_image1, start_image2, 684, 160, 150, 50)
            self.button(htphelp7_image1, start_image2, 684, 220, 150, 50)
            self.button(htphelp8_image1, start_image2, 684, 280, 150, 50)

            self.button(exit_image1, start_image2, 437, 535, 150, 50)

            mouse = pg.mouse.get_pos()

            pg.display.update()

            for event in pg.event.get():
                if event.type == pg.MOUSEBUTTONDOWN:
                    if 140 + 150 > mouse[0] > 140 and 100 + 50 > mouse[1] > 100:
                        g.goal_of_the_game()
                    if 140 + 150 > mouse[0] > 140 and 160 + 50 > mouse[1] > 160:
                        g.your_turn()
                    if 140 + 150 > mouse[0] > 140 and 220 + 50 > mouse[1] > 220:
                        g.how_to_attack()
                    if 140 + 150 > mouse[0] > 140 and 280 + 50 > mouse[1] > 280:
                        g.how_to_get_cards()
                    if 684 + 150 > mouse[0] > 684 and 100 + 50 > mouse[1] > 100:
                        g.ship_stats()
                    if 684 + 150 > mouse[0] > 684 and 160 + 50 > mouse[1] > 160:
                        g.what_are_cards()
                    if 684 + 150 > mouse[0] > 684 and 220 + 50 > mouse[1] > 220:
                        g.how_to_defend()
                    if 684 + 150 > mouse[0] > 684 and 280 + 50 > mouse[1] > 280:
                        g.how_to_use_cards()

                    if 437 + 150 > mouse[0] > 437 and 535 + 50 > mouse[1] > 535:
                        g.main_menu()

                if event.type == pg.QUIT:
                    g.quit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        g.quit()

    def goal_of_the_game(self):
        gotg = True
        while gotg:
            self.screen.blit(gotgbg_image, (0, 0))

            self.button(exit_image1, start_image2, 437, 535, 150, 50)

            mouse = pg.mouse.get_pos()

            pg.display.update()

            for event in pg.event.get():
                if event.type == pg.MOUSEBUTTONDOWN:

                    if 437 + 150 > mouse[0] > 437 and 535 + 50 > mouse[1] > 535:
                        g.how_to_play()

                if event.type == pg.QUIT:
                    g.quit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        g.quit()

    def your_turn(self):
        yt = True
        while yt:
            self.screen.blit(ytbg_image, (0, 0))

            self.button(exit_image1, start_image2, 437, 535, 150, 50)

            mouse = pg.mouse.get_pos()

            pg.display.update()

            for event in pg.event.get():
                if event.type == pg.MOUSEBUTTONDOWN:

                    if 437 + 150 > mouse[0] > 437 and 535 + 50 > mouse[1] > 535:
                        g.how_to_play()

                if event.type == pg.QUIT:
                    g.quit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        g.quit()

    def how_to_attack(self):
        hta = True
        while hta:
            self.screen.blit(htabg_image, (0, 0))

            self.button(exit_image1, start_image2, 437, 535, 150, 50)

            mouse = pg.mouse.get_pos()

            pg.display.update()

            for event in pg.event.get():
                if event.type == pg.MOUSEBUTTONDOWN:

                    if 437 + 150 > mouse[0] > 437 and 535 + 50 > mouse[1] > 535:
                        g.how_to_play()

                if event.type == pg.QUIT:
                    g.quit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        g.quit()

    def how_to_get_cards(self):
        htgc = True
        while htgc:
            self.screen.blit(htgcbg_image, (0, 0))

            self.button(exit_image1, start_image2, 437, 535, 150, 50)

            mouse = pg.mouse.get_pos()

            pg.display.update()

            for event in pg.event.get():
                if event.type == pg.MOUSEBUTTONDOWN:

                    if 437 + 150 > mouse[0] > 437 and 535 + 50 > mouse[1] > 535:
                        g.how_to_play()

                if event.type == pg.QUIT:
                    g.quit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        g.quit()

    def ship_stats(self):
        ss = True
        while ss:
            self.screen.blit(ssbg_image, (0, 0))

            self.button(exit_image1, start_image2, 437, 535, 150, 50)

            mouse = pg.mouse.get_pos()

            pg.display.update()

            for event in pg.event.get():
                if event.type == pg.MOUSEBUTTONDOWN:

                    if 437 + 150 > mouse[0] > 437 and 535 + 50 > mouse[1] > 535:
                        g.how_to_play()

                if event.type == pg.QUIT:
                    g.quit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        g.quit()

    def what_are_cards(self):
        wac = True
        while wac:
            self.screen.blit(wacbg_image, (0, 0))

            self.button(exit_image1, start_image2, 437, 535, 150, 50)

            mouse = pg.mouse.get_pos()

            pg.display.update()

            for event in pg.event.get():
                if event.type == pg.MOUSEBUTTONDOWN:

                    if 437 + 150 > mouse[0] > 437 and 535 + 50 > mouse[1] > 535:
                        g.how_to_play()

                if event.type == pg.QUIT:
                    g.quit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        g.quit()

    def how_to_defend(self):
        htd = True
        while htd:
            self.screen.blit(htdbg_image, (0, 0))

            self.button(exit_image1, start_image2, 437, 535, 150, 50)

            mouse = pg.mouse.get_pos()

            pg.display.update()

            for event in pg.event.get():
                if event.type == pg.MOUSEBUTTONDOWN:

                    if 437 + 150 > mouse[0] > 437 and 535 + 50 > mouse[1] > 535:
                        g.how_to_play()

                if event.type == pg.QUIT:
                    g.quit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        g.quit()

    def how_to_use_cards(self):
        htuc = True
        while htuc:
            self.screen.blit(htucbg_image, (0, 0))

            self.button(exit_image1, start_image2, 437, 535, 150, 50)

            mouse = pg.mouse.get_pos()

            pg.display.update()

            for event in pg.event.get():
                if event.type == pg.MOUSEBUTTONDOWN:

                    if 437 + 150 > mouse[0] > 437 and 535 + 50 > mouse[1] > 535:
                        g.how_to_play()

                if event.type == pg.QUIT:
                    g.quit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        g.quit()

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
                        g.how_to_play()
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