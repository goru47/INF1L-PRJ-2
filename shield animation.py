import pygame

pygame.init()


#window aanmaken
window = pygame.display.set_mode((1000,600))


#window naam instellen
pygame.display.set_caption("+HP Animation")


# icoon toevoegen
gameIcon = pygame.image.load('images/BPicon.png')
pygame.display.set_icon(gameIcon)



white = (255,255,255)
shieldsize = 32
shieldx = 200
shieldy = 50
clock = pygame.time.Clock()


# load + hp sprites
shield1 = pygame.image.load("shield/shield1.png")
shield1 = pygame.transform.scale(shield1, (shieldsize, shieldsize))

shield2 = pygame.image.load("shield/shield2.png")
shield2 = pygame.transform.scale(shield2, (shieldsize, shieldsize))

shield3 = pygame.image.load("shield/shield3.png")
shield3 = pygame.transform.scale(shield3, (shieldsize, shieldsize))

shield4 = pygame.image.load("shield/shield4.png")
shield4 = pygame.transform.scale(shield4, (shieldsize, shieldsize))

shield5 = pygame.image.load("shield/shield5.png")
shield5 = pygame.transform.scale(shield5, (shieldsize, shieldsize))

shield6 = pygame.image.load("shield/shield6.png")
shield6 = pygame.transform.scale(shield6, (shieldsize, shieldsize))

shield7 = pygame.image.load("shield/shield7.png")
shield7 = pygame.transform.scale(shield7, (shieldsize, shieldsize))

shield8 = pygame.image.load("shield/shield8.png")
shield8 = pygame.transform.scale(shield8, (shieldsize, shieldsize))

shield9 = pygame.image.load("shield/shield9.png")
shield9 = pygame.transform.scale(shield9, (shieldsize, shieldsize))

shield10 = pygame.image.load("shield/shield10.png")
shield10 = pygame.transform.scale(shield10, (shieldsize, shieldsize))

shield11 = pygame.image.load("shield/shield11.png")
shield11 = pygame.transform.scale(shield11, (shieldsize, shieldsize))

shield12 = pygame.image.load("shield/shield12.png")
shield12 = pygame.transform.scale(shield12, (shieldsize, shieldsize))

shield13 = pygame.image.load("shield/shield13.png")
shield13 = pygame.transform.scale(shield13, (shieldsize, shieldsize))

shield14 = pygame.image.load("shield/shield14.png")
shield14 = pygame.transform.scale(shield14, (shieldsize, shieldsize))



# animating shield

shieldCurrentImage = 1

gameLoop=True
while gameLoop:


    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            gameLoop = False
            window.fill(white)

        if (shieldCurrentImage == 1):
            window.fill(white)
            window.blit(shield1, (shieldx, shieldy))

        if (shieldCurrentImage == 2):
            window.fill(white)
            window.blit(shield2, (shieldx, shieldy))

        if (shieldCurrentImage == 3):
            window.fill(white)
            window.blit(shield3, (shieldx, shieldy))

        if (shieldCurrentImage == 4):
            window.fill(white)
            window.blit(shield4, (shieldx, shieldy))

        if (shieldCurrentImage == 5):
            window.fill(white)
            window.blit(shield5, (shieldx, shieldy))

        if (shieldCurrentImage == 6):
            window.fill(white)
            window.blit(shield6, (shieldx, shieldy))

        if (shieldCurrentImage == 7):
            window.fill(white)
            window.blit(shield7, (shieldx, shieldy))

        if (shieldCurrentImage == 8):
            window.fill(white)
            window.blit(shield8, (shieldx, shieldy))

        if (shieldCurrentImage == 9):
            window.fill(white)
            window.blit(shield9, (shieldx, shieldy))

        if (shieldCurrentImage == 10):
            window.fill(white)
            window.blit(shield10, (shieldx, shieldy))

        if (shieldCurrentImage == 11):
            window.fill(white)
            window.blit(shield12, (shieldx, shieldy))

        if (shieldCurrentImage == 12):
            window.fill(white)
            window.blit(shield12, (shieldx, shieldy))

        if (shieldCurrentImage == 13):
            window.fill(white)
            window.blit(shield13, (shieldx, shieldy))

        if (shieldCurrentImage == 14):
            window.fill(white)
            window.blit(shield14, (shieldx, shieldy))




        if (shieldCurrentImage == 14):
            shieldCurrentImage = 1

        else:
            shieldCurrentImage += 1;





    pygame.display.update()
    clock.tick(16)
pygame.quit()