




def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: "+str(count), True, black)
    gameDisplay.blit(text,(0,0))

    if thing_starty > display_height:
        thing_starty = 0 - thing_height
        thing_startx = random.randrange(0, display_width)
        dodged += 1
        thing_speed += 1
        thing_width += (dodged * 1.2)