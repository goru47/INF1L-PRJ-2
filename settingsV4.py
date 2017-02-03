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

# ship & enemy colors
ship_1 = (0, 255, 0)
ship_2 = (0, 200, 0)
ship_3 = (0, 120, 0)
enemy_1 = (255, 0, 0)
enemy_2 = (220, 0, 0)
enemy_3 = (195, 0, 0)


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


# how to play image
htpbg_image = pg.image.load("helpbg.png")
htpbg_image = pg.transform.scale(htpbg_image, (1024, 768))

# hot to play button images
htphelp1_image1 = pg.image.load("help1.png")
htphelp1_image1 = pg.transform.scale(htphelp1_image1, (150, 50))
start_image2 = pg.image.load("arrow.png")
start_image2 = pg.transform.scale(start_image2, (150, 50))
htphelp2_image1 = pg.image.load("help2.png")
htphelp2_image1 = pg.transform.scale(htphelp2_image1, (150, 50))
start_image2 = pg.image.load("arrow.png")
start_image2 = pg.transform.scale(start_image2, (150, 50))
htphelp3_image1 = pg.image.load("help3.png")
htphelp3_image1 = pg.transform.scale(htphelp3_image1, (150, 50))
start_image2 = pg.image.load("arrow.png")
start_image2 = pg.transform.scale(start_image2, (150, 50))
htphelp4_image1 = pg.image.load("help4.png")
htphelp4_image1 = pg.transform.scale(htphelp4_image1, (150, 50))
start_image2 = pg.image.load("arrow.png")
start_image2 = pg.transform.scale(start_image2, (150, 50))
htphelp5_image1 = pg.image.load("help5.png")
htphelp5_image1 = pg.transform.scale(htphelp5_image1, (150, 50))
start_image2 = pg.image.load("arrow.png")
start_image2 = pg.transform.scale(start_image2, (150, 50))
htphelp6_image1 = pg.image.load("help6.png")
htphelp6_image1 = pg.transform.scale(htphelp6_image1, (150, 50))
start_image2 = pg.image.load("arrow.png")
start_image2 = pg.transform.scale(start_image2, (150, 50))
htphelp7_image1 = pg.image.load("help7.png")
htphelp7_image1 = pg.transform.scale(htphelp7_image1, (150, 50))
start_image2 = pg.image.load("arrow.png")
start_image2 = pg.transform.scale(start_image2, (150, 50))
htphelp8_image1 = pg.image.load("help8.png")
htphelp8_image1 = pg.transform.scale(htphelp8_image1, (150, 50))
start_image2 = pg.image.load("arrow.png")
start_image2 = pg.transform.scale(start_image2, (150, 50))
exit_image1 = pg.image.load("exit.png")
exit_image1 = pg.transform.scale(exit_image1, (150, 50))
start_image2 = pg.image.load("arrow.png")
start_image2 = pg.transform.scale(start_image2, (150, 50))

#text for the how to play
gotgbg_image = pg.image.load("gotgbg.png")
gotgbg_image = pg.transform.scale(gotgbg_image, (1024, 768))
ytbg_image = pg.image.load("ytbg.png")
ytbg_image = pg.transform.scale(ytbg_image, (1024, 768))
htabg_image = pg.image.load("htabg.png")
htabg_image = pg.transform.scale(htabg_image, (1024, 768))
htgcbg_image = pg.image.load("htgcbg.png")
htgcbg_image = pg.transform.scale(htgcbg_image, (1024, 768))
ssbg_image = pg.image.load("ssbg.png")
ssbg_image = pg.transform.scale(ssbg_image, (1024, 768))
wacbg_image = pg.image.load("wacbg.png")
wacbg_image = pg.transform.scale(wacbg_image, (1024, 768))
htucbg_image = pg.image.load("htucbg.png")
htucbg_image = pg.transform.scale(htucbg_image, (1024, 768))
htdbg_image = pg.image.load("htdbg.png")
htdbg_image = pg.transform.scale(htdbg_image, (1024, 768))



# images
bg_image = pg.image.load("check.png")
bg_image = pg.transform.scale(bg_image, (1024, 768))

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
board_image = pg.transform.scale(board_image, (1024, 768))
map_image = pg.image.load("gamemap.png")
map_image = pg.transform.scale(map_image, (480, 480))

menu1_image = pg.image.load("menu.png")
menu1_image = pg.transform.scale(menu1_image, (50, 50))
menu2_image = pg.image.load("circle.png")
menu2_image = pg.transform.scale(menu2_image, (50, 50))


# kaarten
kaartn_image = pg.image.load("backnorm.png")
kaartn_image = pg.transform.scale(kaartn_image, (80, 160))
kaarts_image = pg.image.load("backspec.png")
kaarts_image = pg.transform.scale(kaarts_image, (80, 160))

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
instbg_image = pg.transform.scale(instbg_image, (1024, 768))

inst1_image = pg.image.load("instr2.png")
inst1_image = pg.transform.scale(inst1_image, (900, 700))


# boot
boot2 = pg.image.load("bootje.png")
boot2 = pg.transform.scale(boot2, (40, 80))
boot2.set_colorkey(white)


#================================================================

card_multiplier = 0.3#bepaalt hoeveel keer de kaart vergroot/verkleind wordt t.o.v. de originele grootte
cardposX = 200
cardposY = 100
cardsizeX = 600 * card_multiplier
cardsizeY = 900 * card_multiplier

# load card sprite

normaal = pg.image.load("backnorm.png")
normaal = pg.transform.scale(normaal, (int(cardsizeX), int(cardsizeY)))


#card offensive advanced rifling
CardOfAdRi = pg.image.load("kaartoffensief_advrifling.png")#locatie en naam van de afbeelding
CardOfAdRi = pg.transform.scale(CardOfAdRi, (int(cardsizeX), int(cardsizeY)))

#card offensive EMP
CardOfEMP = pg.image.load("kaartoffensief_emp.png")
CardOfEMP = pg.transform.scale(CardOfEMP, (int(cardsizeX), int(cardsizeY)))

#card offensive FMJ
CardOfFMJ = pg.image.load("kaartoffensief_fmj.png")
CardOfFMJ = pg.transform.scale(CardOfFMJ, (int(cardsizeX), int(cardsizeY)))

#card offensive Mine
CardOfMine = pg.image.load("kaartoffensief_mine.png")
CardOfMine = pg.transform.scale(CardOfMine, (int(cardsizeX), int(cardsizeY)))

#card offensive Mine
CardOfRif = pg.image.load("kaartoffensief_rifling.png")
CardOfRif = pg.transform.scale(CardOfRif, (int(cardsizeX), int(cardsizeY)))

#----------------------------------------------------------

#card defensief reinforced hull
CardDefReHull = pg.image.load("kaartdefensief_reinforcedhull.png")
CardDefReHull = pg.transform.scale(CardDefReHull, (int(cardsizeX), int(cardsizeY)))

#card defensief sonar
CardDefSonar = pg.image.load("kaartdefensief_sonar.png")
CardDefSonar = pg.transform.scale(CardDefSonar, (int(cardsizeX), int(cardsizeY)))

#card defensief smokescreen
CardDefSmoke = pg.image.load("kaartdefensief_smoke.png")
CardDefSmoke = pg.transform.scale(CardDefSmoke, (int(cardsizeX), int(cardsizeY)))

#card defensief sabotage
CardDefSabo = pg.image.load("kaartdefensief_sabotage.png")
CardDefSabo = pg.transform.scale(CardDefSabo, (int(cardsizeX), int(cardsizeY)))

#--------------------------------------------------------------

# card hulp backup
CardHulpBackup = pg.image.load("kaarthulp_backup.png")
CardHulpBackup = pg.transform.scale(CardHulpBackup, (int(cardsizeX), int(cardsizeY)))

#card hulp extra fuel
CardHulpFuel = pg.image.load("kaarthulp_extrafuel.png")
CardHulpFuel = pg.transform.scale(CardHulpFuel, (int(cardsizeX), int(cardsizeY)))

#card hulp extra fuel2
CardHulpFuel2 = pg.image.load("kaarthulp_extrafuel2.png")
CardHulpFuel2 = pg.transform.scale(CardHulpFuel2, (int(cardsizeX), int(cardsizeY)))

#card hulp rally
CardHulpRally = pg.image.load("kaarthulp_rally.png")
CardHulpRally = pg.transform.scale(CardHulpRally, (int(cardsizeX), int(cardsizeY)))

#card hulp adrenaline rush
CardHulpRush = pg.image.load("kaarthulp_adrenaline.png")
CardHulpRush = pg.transform.scale(CardHulpRush, (int(cardsizeX), int(cardsizeY)))

