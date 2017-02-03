from settings import *
import pygame as pg



pg.font.init()

Width, Height = 1024, 768

screen = pg.display.set_mode((Width, Height))





def button(naam1, naam2, x, y, w, h):
    # image, image highlight, x pos, y pos, width, height
    mouse = pg.mouse.get_pos()

    # als x pos + width groter
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        screen.blit(naam1, (x, y))
        screen.blit(naam2, (x, y))
    else:
        screen.blit(naam1, (x, y))


def how_to_play():
    htp = True
    while htp:
        screen.blit(htpbg_image, (0, 0))

        button(htphelp1_image1, start_image2, 140, 100, 150, 50)
        button(htphelp2_image1, start_image2, 140, 160, 150, 50)
        button(htphelp3_image1, start_image2, 140, 220, 150, 50)
        button(htphelp4_image1, start_image2, 140, 280, 150, 50)
        button(htphelp5_image1, start_image2, 684, 100, 150, 50)
        button(htphelp6_image1, start_image2, 684, 160, 150, 50)
        button(htphelp7_image1, start_image2, 684, 220, 150, 50)
        button(htphelp8_image1, start_image2, 684, 280, 150, 50)

        button(exit_image1, start_image2, 437, 535, 150, 50)

        mouse = pg.mouse.get_pos()

        pg.display.update()

        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN:
                if 140 + 150 > mouse[0] > 140 and 100 + 50 > mouse[1] > 100:
                    goal_of_the_game()
                if 140 + 150 > mouse[0] > 140 and 160 + 50 > mouse[1] > 160:
                    your_turn()
                if 140 + 150 > mouse[0] > 140 and 220 + 50 > mouse[1] > 220:
                    how_to_attack()
                if 140 + 150 > mouse[0] > 140 and 280 + 50 > mouse[1] > 280:
                    how_to_get_cards()
                if 684 + 150 > mouse[0] > 684 and 100 + 50 > mouse[1] > 100:
                    ship_stats()
                if 684 + 150 > mouse[0] > 684 and 160 + 50 > mouse[1] > 160:
                    what_are_cards()
                if 684 + 150 > mouse[0] > 684 and 220 + 50 > mouse[1] > 220:
                    how_to_defend()
                if 684 + 150 > mouse[0] > 684 and 280 + 50 > mouse[1] > 280:
                    how_to_use_cards()

                if 437 + 150 > mouse[0] > 437 and 535 + 50 > mouse[1] > 535:
                    main_menu()

            if event.type == pg.QUIT:
                quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    quit()


def goal_of_the_game():
    gotg = True
    while gotg:
        screen.blit(gotgbg_image, (0, 0))

        button(exit_image1, start_image2, 437, 535, 150, 50)

        mouse = pg.mouse.get_pos()

        pg.display.update()

        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN:

                if 437 + 150 > mouse[0] > 437 and 535 + 50 > mouse[1] > 535:
                    g.how_to_play()

            if event.type == pg.QUIT:
                quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    quit()


def your_turn():
    yt = True
    while yt:
        screen.blit(ytbg_image, (0, 0))

        button(exit_image1, start_image2, 437, 535, 150, 50)

        mouse = pg.mouse.get_pos()

        pg.display.update()

        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN:

                if 437 + 150 > mouse[0] > 437 and 535 + 50 > mouse[1] > 535:
                    how_to_play()

            if event.type == pg.QUIT:
                quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    quit()


def how_to_attack():
    hta = True
    while hta:
        screen.blit(htabg_image, (0, 0))

        button(exit_image1, start_image2, 437, 535, 150, 50)

        mouse = pg.mouse.get_pos()

        pg.display.update()

        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN:

                if 437 + 150 > mouse[0] > 437 and 535 + 50 > mouse[1] > 535:
                    how_to_play()

            if event.type == pg.QUIT:
                quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    quit()


def how_to_get_cards():
    htgc = True
    while htgc:
        screen.blit(htgcbg_image, (0, 0))

        button(exit_image1, start_image2, 437, 535, 150, 50)

        mouse = pg.mouse.get_pos()

        pg.display.update()

        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN:

                if 437 + 150 > mouse[0] > 437 and 535 + 50 > mouse[1] > 535:
                    how_to_play()

            if event.type == pg.QUIT:
                quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    quit()


def ship_stats():
    ss = True
    while ss:
        screen.blit(ssbg_image, (0, 0))

        button(exit_image1, start_image2, 437, 535, 150, 50)

        mouse = pg.mouse.get_pos()

        pg.display.update()

        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN:

                if 437 + 150 > mouse[0] > 437 and 535 + 50 > mouse[1] > 535:
                    how_to_play()

            if event.type == pg.QUIT:
                quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    quit()


def what_are_cards():
    wac = True
    while wac:
        screen.blit(wacbg_image, (0, 0))

        button(exit_image1, start_image2, 437, 535, 150, 50)

        mouse = pg.mouse.get_pos()

        pg.display.update()

        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN:

                if 437 + 150 > mouse[0] > 437 and 535 + 50 > mouse[1] > 535:
                    how_to_play()

            if event.type == pg.QUIT:
                quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    quit()


def how_to_defend():
    htd = True
    while htd:
        screen.blit(htdbg_image, (0, 0))

        button(exit_image1, start_image2, 437, 535, 150, 50)

        mouse = pg.mouse.get_pos()

        pg.display.update()

        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN:

                if 437 + 150 > mouse[0] > 437 and 535 + 50 > mouse[1] > 535:
                    how_to_play()

            if event.type == pg.QUIT:
                quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    quit()


def how_to_use_cards():
    htuc = True
    while htuc:
        screen.blit(htucbg_image, (0, 0))

        button(exit_image1, start_image2, 437, 535, 150, 50)

        mouse = pg.mouse.get_pos()

        pg.display.update()

        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN:

                if 437 + 150 > mouse[0] > 437 and 535 + 50 > mouse[1] > 535:
                    how_to_play()

            if event.type == pg.QUIT:
                quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    quit()


def main_menu():
    in_main_menu = True
    while in_main_menu:
        screen.blit(bg_image, (0, 0))
        screen.blit(title_image, (Width / 5, Width / 8))

        button(start_image1, start_image2, 600, 400, 150, 50)
        button(score1_image, score2_image, 600, 500, 150, 50)
        button(help1_image, help2_image, 600, 450, 150, 50)

        mouse = pg.mouse.get_pos()

        pg.display.update()

        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN:
                if 600 + 150 > mouse[0] > 600 and 400 + 50 > mouse[1] > 150:
                    new()
                if 600 + 150 > mouse[0] > 600 and 500 + 50 > mouse[1] > 150:
                    pass  # options
                if 600 + 150 > mouse[0] > 600 and 450 + 50 > mouse[1] > 150:
                    how_to_play()
            if event.type == pg.QUIT:
                quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    quit()
