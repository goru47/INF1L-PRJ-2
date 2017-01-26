import pygame

pygame.init()


#window aanmaken
window = pygame.display.set_mode((1000,600))


#window naam instellen
pygame.display.set_caption("Explosion Animation")


# icoon toevoegen
gameIcon = pygame.image.load('images/BPicon.png')
pygame.display.set_icon(gameIcon)





explx = 200
exply = 100
white = (255,255,255)



clock = pygame.time.Clock()



#================================================================

# load explosion sprites
expl1 = pygame.image.load("explosion/expl1.png")
expl2 = pygame.image.load("explosion/expl2.png")
expl3 = pygame.image.load("explosion/expl3.png")
expl4 = pygame.image.load("explosion/expl4.png")
expl5 = pygame.image.load("explosion/expl5.png")
expl6 = pygame.image.load("explosion/expl6.png")
expl7 = pygame.image.load("explosion/expl7.png")
expl8 = pygame.image.load("explosion/expl8.png")
expl9 = pygame.image.load("explosion/expl9.png")
expl10 = pygame.image.load("explosion/expl10.png")
expl11 = pygame.image.load("explosion/expl11.png")
expl12 = pygame.image.load("explosion/expl12.png")
expl13 = pygame.image.load("explosion/expl13.png")
expl14 = pygame.image.load("explosion/expl14.png")



# animating explosions
explosionCurrentImage = 1


gameLoop=True
while gameLoop:

    for event in pygame.event.get():
        if (event.type==pygame.QUIT):
            gameLoop=False
            window.fill(white)

        if (explosionCurrentImage==1):
            window.fill(white)
            window.blit(expl1, (explx,exply))

        if (explosionCurrentImage==2):
            window.fill(white)
            window.blit(expl2, (explx,exply))

        if (explosionCurrentImage==3):
            window.fill(white)
            window.blit(expl3, (explx,exply))

        if (explosionCurrentImage==4):
            window.fill(white)
            window.blit(expl4, (explx,exply))

        if (explosionCurrentImage == 5):
            window.fill(white)
            window.blit(expl5, (explx,exply))

        if (explosionCurrentImage == 6):
            window.fill(white)
            window.blit(expl6, (explx,exply))

        if (explosionCurrentImage == 7):
            window.fill(white)
            window.blit(expl7, (explx,exply))

        if (explosionCurrentImage == 8):
            window.fill(white)
            window.blit(expl8, (explx,exply))

        if (explosionCurrentImage == 9):
            window.fill(white)
            window.blit(expl9, (explx,exply))

        if (explosionCurrentImage == 10):
            window.fill(white)
            window.blit(expl10, (explx,exply))

        if (explosionCurrentImage == 11):
            window.fill(white)
            window.blit(expl11, (explx,exply))

        if (explosionCurrentImage == 12):
            window.fill(white)
            window.blit(expl12, (explx,exply))

        if (explosionCurrentImage == 13):
            window.fill(white)
            window.blit(expl13, (explx,exply))

        if (explosionCurrentImage == 14):
            window.fill(white)
            window.blit(expl14, (explx,exply))



        if (explosionCurrentImage==14):
            explosionCurrentImage=1

        else:
            explosionCurrentImage+=1;






# ================================================================









    pygame.display.flip()
    clock.tick(10)
pygame.quit()