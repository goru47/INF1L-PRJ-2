import pygame as pg

#   Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (200, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 200)
yellow = (255, 255, 0)
aqua = (0, 255, 255)
silver = (192, 192, 192)
dark_silver = (220, 220, 220)
bright_red = (255, 0, 0)
bright_blue = (0, 0, 255)
light_grey = (100, 100, 100)
dark_grey = (40, 40, 40)

# game settings
width = 800
height = 600
'''width = 1024    # 16 * 64 or 32 * 32 or 64 * 16
height = 768    # # 16 * 48 or 32 * 24 or 64 * 12'''
fps = 30


tilesize = 32
Title = 'pygame test'
grid_width = width / tilesize
grid_height = height / tilesize


'''#   text font sizes
largeText = pg.font.Font('freesansbold.ttf', 115)
mediumText = pg.font.Font('freesansbold.ttf', 60)
smallText = pg.font.Font('freesansbold.ttf', 20)'''


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()




# images
bg_image = pg.image.load("check.png")
bg_image = pg.transform.scale(bg_image, (800, 600))

# main menu image
title_image = pg.image.load("titel.png")
title_image = pg.transform.scale(title_image, (471, 78))

score1_image = pg.image.load("hscore.png")
score1_image = pg.transform.scale(score1_image, (150, 50))
score2_image = pg.image.load("arrow.png")
score2_image = pg.transform.scale(score2_image, (150, 50))

help1_image = pg.image.load("ins.png")
help1_image = pg.transform.scale(help1_image, (150, 50))
help2_image = pg.image.load("arrow.png")
help2_image = pg.transform.scale(help2_image, (150, 50))


# main menu buttons
start_image1 = pg.image.load("pl.png")
start_image1 = pg.transform.scale(start_image1, (150, 50))
start_image2 = pg.image.load("arrow.png")
start_image2 = pg.transform.scale(start_image2, (150, 50))

# board 1 en map 1
board_image = pg.image.load("menu2.png")
board_image = pg.transform.scale(board_image, (800, 600))
map_image = pg.image.load("gamemap.png")
map_image = pg.transform.scale(map_image, (480, 480))

menu1_image = pg.image.load("menu.png")
menu1_image = pg.transform.scale(menu1_image, (50, 50))
menu2_image = pg.image.load("circle.png")
menu2_image = pg.transform.scale(menu2_image, (50, 50))


# kaarten
kaartn_image = pg.image.load("backnorm.png")
kaartn_image = pg.transform.scale(kaartn_image, (115, 150))
kaarts_image = pg.image.load("backspec.png")
kaarts_image = pg.transform.scale(kaarts_image, (115, 150))

kaart1 = pg.image.load("kaartoffensief_advrifling.png")
kaart1 = pg.transform.scale(kaart1, (120, 240))
kaart2 = pg.image.load("kaartspeciaal_jack.png")
kaart2 = pg.transform.scale(kaart2, (120, 240))
# pause
pause_image = pg.image.load("pauze.png")
pause_image = pg.transform.scale(pause_image, (800, 600))
pauzet_image = pg.image.load("pauzet.png")
pauzet_image = pg.transform.scale(pauzet_image, (471, 78))


# instruction
instbg_image = pg.image.load("oceaan.jpg")
instbg_image = pg.transform.scale(instbg_image, (800, 600))

inst1_image = pg.image.load("instr2.png")
inst1_image = pg.transform.scale(inst1_image, (600, 580))


# boot

boot3 = pg.image.load("bootje2.png")
boot3 = pg.transform.scale(boot3, (50, 100))
boot3.set_colorkey(white)

boot2 = pg.image.load("bootje2.png")
boot2 = pg.transform.scale(boot2, (50, 70))
boot2.set_colorkey(white)

boot1 = pg.image.load("bootje2.png")
boot1 = pg.transform.scale(boot1, (50, 20))
boot1.set_colorkey(white)
