import pygame
import random

pygame.init()

#WINDOW
#window aanmaken
window = pygame.display.set_mode((1000,600))

#window naam instellen
pygame.display.set_caption("blit card")

# icoon toevoegen
gameIcon = pygame.image.load('images/BPicon.png')
pygame.display.set_icon(gameIcon)



#VALUES
# eigenschappen kaart
card_multiplier = 0.3#bepaalt hoeveel keer de kaart vergroot/verkleind wordt t.o.v. de originele grootte
cardposX = 200
cardposY = 100
cardsizeX = 600 * card_multiplier
cardsizeY = 900 * card_multiplier

#kleur
white = (255,255,255)
green = (0,200,0)
bright_green = (0,255,0)


#FUNCTIES



clock = pygame.time.Clock()









#================================================================

# load card sprite

#card offensive advanced rifling
CardOfAdRi = pygame.image.load("kaartoffensief_advrifling.png")#locatie en naam van de afbeelding
CardOfAdRi = pygame.transform.scale(CardOfAdRi, (int(cardsizeX), int(cardsizeY)))

#card offensive EMP
CardOfEMP = pygame.image.load("kaartoffensief_emp.png")
CardOfEMP = pygame.transform.scale(CardOfEMP, (int(cardsizeX), int(cardsizeY)))

#card offensive FMJ
CardOfFMJ = pygame.image.load("kaartoffensief_fmj.png")
CardOfFMJ = pygame.transform.scale(CardOfFMJ, (int(cardsizeX), int(cardsizeY)))

#card offensive Mine
CardOfMine = pygame.image.load("kaartoffensief_mine.png")
CardOfMine = pygame.transform.scale(CardOfMine, (int(cardsizeX), int(cardsizeY)))

#card offensive Mine
CardOfRif = pygame.image.load("kaartoffensief_rifling.png")
CardOfRif = pygame.transform.scale(CardOfRif, (int(cardsizeX), int(cardsizeY)))

#----------------------------------------------------------

#card defensief reinforced hull
CardDefReHull = pygame.image.load("kaartdefensief_reinforcedhull.png")
CardDefReHull = pygame.transform.scale(CardDefReHull, (int(cardsizeX), int(cardsizeY)))

#card defensief sonar
CardDefSonar = pygame.image.load("kaartdefensief_sonar.png")
CardDefSonar = pygame.transform.scale(CardDefSonar, (int(cardsizeX), int(cardsizeY)))

#card defensief smokescreen
CardDefSmoke = pygame.image.load("kaartdefensief_smoke.png")
CardDefSmoke = pygame.transform.scale(CardDefSmoke, (int(cardsizeX), int(cardsizeY)))

#card defensief sabotage
CardDefSabo = pygame.image.load("kaartdefensief_sabotage.png")
CardDefSabo = pygame.transform.scale(CardDefSabo, (int(cardsizeX), int(cardsizeY)))

#--------------------------------------------------------------

# card hulp backup
CardHulpBackup = pygame.image.load("kaarthulp_backup.png")
CardHulpBackup = pygame.transform.scale(CardHulpBackup, (int(cardsizeX), int(cardsizeY)))

#card hulp extra fuel
CardHulpFuel = pygame.image.load("kaarthulp_extrafuel.png")
CardHulpFuel = pygame.transform.scale(CardHulpFuel, (int(cardsizeX), int(cardsizeY)))

#card hulp extra fuel2
CardHulpFuel2 = pygame.image.load("kaarthulp_extrafuel2.png")
CardHulpFuel2 = pygame.transform.scale(CardHulpFuel2, (int(cardsizeX), int(cardsizeY)))

#card hulp rally
CardHulpRally = pygame.image.load("kaarthulp_rally.png")
CardHulpRally = pygame.transform.scale(CardHulpRally, (int(cardsizeX), int(cardsizeY)))

#card hulp adrenaline rush
CardHulpRush = pygame.image.load("kaarthulp_adrenaline.png")
CardHulpRush = pygame.transform.scale(CardHulpRush, (int(cardsizeX), int(cardsizeY)))










# MAIN GAME LOOP
gameLoop=True
while gameLoop:

    for event in pygame.event.get():
        if (event.type==pygame.QUIT):
            gameLoop=False


         #scherm
        window.fill(white)
        mouse = pygame.mouse.get_pos()

        # button tekenen
        knopje = pygame.draw.rect(window, green, (150, 450, 100, 50))


        # Als de knop aangeklikt wordt:
        ev = pygame.event.get
        if 150 + 100 > mouse[0] > 150 and 450 + 50 > mouse[1] > 450 and event.type == pygame.MOUSEBUTTONDOWN:


            trek_kaart = True

            if trek_kaart == True:
                pygame.draw.rect(window, bright_green, (150, 450, 100, 50))

                eenkaart = random.randint(1, 43)

                #blit cards

                # AdRi = 1,2
                if eenkaart <= 2:
                    window.blit(CardOfAdRi, (cardposX, cardposY))

                #emp = 3,4,5,6
                if eenkaart > 2 and eenkaart <= 6:
                    window.blit(CardOfEMP, (cardposX, cardposY))

                #fmj = 7,8
                if eenkaart >6 and eenkaart <= 8:
                    window.blit(CardOfFMJ, (cardposX, cardposY))

                # mine = 9,10,11,12,13,14
                if eenkaart > 8 and eenkaart <= 14:
                    window.blit(CardOfMine, (cardposX, cardposY))

                # rifle = 15, 16
                if eenkaart > 14 and eenkaart <= 16:
                    window.blit(CardOfRif, (cardposX, cardposY))
        #---------------------------------------------------------------
                # Re hull = 17, 18
                if eenkaart > 16 and eenkaart <= 18:
                    window.blit(CardDefReHull, (cardposX, cardposY))

                # sonar = 19, 20, 21, 22
                if eenkaart > 18 and eenkaart <= 22:
                    window.blit(CardDefSonar, (cardposX, cardposY))

                # smoke = 23, 24
                if eenkaart > 22 and eenkaart <= 24:
                    window.blit(CardDefReHull, (cardposX, cardposY))

                # sabotage = 25, 26
                if eenkaart > 24 and eenkaart <= 26:
                    window.blit(CardDefSabo, (cardposX, cardposY))
        #---------------------------------------------------------------------
                # backup = 27, 28
                if eenkaart > 26 and eenkaart <= 28:
                    window.blit(CardHulpBackup, (cardposX, cardposY))

                # fuel = 29, 30, 31, 32, 33, 34
                if eenkaart > 28 and eenkaart <= 34:
                    window.blit(CardHulpFuel, (cardposX, cardposY))

                # fuel 2 = 35, 36, 37, 38
                if eenkaart > 34 and eenkaart <= 38:
                    window.blit(CardHulpFuel2, (cardposX, cardposY))

                # rally = 39
                if eenkaart == 39:
                    window.blit(CardHulpRally, (cardposX, cardposY))

                # adrenaline rush = 40, 41, 42, 43
                if eenkaart > 39 and eenkaart <= 43:
                    window.blit(CardHulpRush, (cardposX, cardposY))
        else: trek_kaart = False

    # ================================================================









    pygame.display.flip()
    clock.tick(10)
pygame.quit()
