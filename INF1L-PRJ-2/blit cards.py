import pygame

pygame.init()


#window aanmaken
window = pygame.display.set_mode((1000,600))


#window naam instellen
pygame.display.set_caption("blit card")


# icoon toevoegen
gameIcon = pygame.image.load('images/BPicon.png')
pygame.display.set_icon(gameIcon)




# eigenschappen kaart
cardposX = 200
cardposY = 100
cardsizeX = 120
cardsizeY = 180


#kleur
white = (255,255,255)



clock = pygame.time.Clock()



#================================================================

# load card sprite

#card offensive advanced rifling
CardOfAdRi = pygame.image.load("normalekaarten/kaartendef/kaartoffensief_advrifling.png")
CardOfAdRi = pygame.transform.scale(CardOfAdRi, (cardsizeX, cardsizeY))




#game
gameLoop=True
while gameLoop:

    for event in pygame.event.get():
        if (event.type==pygame.QUIT):
            gameLoop=False


         #scherm
        window.fill(white)

        #blit card
        window.blit(CardOfAdRi, (cardposX, cardposY))







# ================================================================









    pygame.display.flip()
    clock.tick(10)
pygame.quit()