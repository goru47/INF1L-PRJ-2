<<<<<<< HEAD
import pygame
import time
import random

pygame.init()

display_width = 1024
display_height = 768

gameDisplay = pygame.display.set_mode((display_width, display_height))

from pygame import mixer # Load the required library


pygame.display.set_caption('how to play test')

white = (255, 255, 255)
black = (0, 0, 0)

sky = (204, 255, 204)

red = (200, 0, 0)
light_red = (255, 0, 0)

yellow = (200, 56, 6)
light_yellow = (250, 117, 29)

blue = (0, 0, 204)
light_blue = (0, 255, 255)

clock = pygame.time.Clock()

smallfont = pygame.font.SysFont("comicsansms", 15)
medfont = pygame.font.SysFont("comicsansms", 25)
        
def music_menu(filename,freq,size,channel,buffersize):
    pygame.mixer.pre_init(freq, -16, 2, 4096)
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play(-1,0.0)

def text_objects(text, color, size="small"):
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    if size == "medium":
        textSurface = medfont.render(text, True, color)

    return textSurface, textSurface.get_rect()


def text_to_button(msg, color, buttonx, buttony, buttonwidth, buttonheight, size="medium"):
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = ((buttonx + (buttonwidth / 2)), buttony + (buttonheight / 2))
    gameDisplay.blit(textSurf, textRect)


def message_to_screen(msg, color, y_displace=0, size="small"):
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = (int(display_width / 2), int(display_height / 2) + y_displace)
    gameDisplay.blit(textSurf, textRect)


def Goal_of_the_game():
    gotg = True

    while gotg:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(sky)

        message_to_screen("Goal of the game", blue, -100, size="medium")
        message_to_screen("To win the Game you need to destroy all of your opponent’s ships by shooting at", black, -30)
        message_to_screen("them with your ships. This is an easy task,however by using cards this can become", black, 0)
        message_to_screen("even easier. Use card and your ships efficiently and become victorious.", black, 30)

        button("exit", 462, 500, 100, 50, yellow, light_yellow, action="exit")

        pygame.display.update()

        clock.tick(15)

def Your_Turn():
    YT = True

    while YT:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(sky)

        message_to_screen("Your turn", blue, -100, size="medium")
        message_to_screen("When it is your turn you can move all of you ships the designated amounts", black, -30)
        message_to_screen("of steps (see ship stats). After you have placed all your boats and have", black, 0)
        message_to_screen("done your attacking the turn end and your opponents makes his move.", black, 30)

        button("exit", 462, 500, 100, 50, yellow, light_yellow, action="exit")

        pygame.display.update()

        clock.tick(15)

def How_to_attack():
    hta = True

    while hta:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(sky)

        message_to_screen("How to attack", blue, -200, size="medium")
        message_to_screen("Attacking is as easy as sitting down to play this game. Every boat has an", black, -120)
        message_to_screen("attack range that is unique to their size the bigger the ship the more", black, -90)
        message_to_screen("range they have. As long as a boat is in the attack position it can", black, -60)
        message_to_screen("attack horizontally and vertically, however if a boat is in the defense", black, -30)
        message_to_screen("position the boat can only attack vertically, but it gains +1 attack range.", black, 0)
        message_to_screen("The range of a boat is equal to the boats size and the attack width is", black, 30)
        message_to_screen("to how wide the boat is. Example: boat with size 3 has 3 range and is 3 wide", black, 60)
        message_to_screen("horizontally and has 3 range vertically and is 1 wide in the attack position.", black, 90)
        message_to_screen("Boat with size 3 has 4 range and is 3 wide in the defensive position. The", black, 120)
        message_to_screen("boat may also only move when it is in attack position. Players may attack", black, 150)
        message_to_screen("twice per turn, however only once per boat.", black, 180)

        button("exit", 462, 600, 100, 50, yellow, light_yellow, action="exit")

        pygame.display.update()

        clock.tick(15)

def How_to_get_cards():
    htgc = True

    while htgc:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(sky)

        message_to_screen("How to get cards", blue, -100, size="medium")
        message_to_screen("There are 2 types of cards normal cards and special cards. Normal", black, -30)
        message_to_screen("cards are easy to obtain at the start of the game both players", black, 0)
        message_to_screen("are given 2 cards and every time it is your turn you draw a card. Special", black, 30)
        message_to_screen("cards are harder to get you can only get them by reaching the harbor you opponent", black, 60)
        message_to_screen("opponent controls. This means you need to get behind enemy lines.", black, 90)

        button("exit", 462, 500, 100, 50, yellow, light_yellow, action="exit")

        pygame.display.update()

        clock.tick(15)

def Ship_Stats():
    SS = True

    while SS:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(sky)

        message_to_screen("Ship Stats", blue, -200, size="medium")
        message_to_screen("If a ship is destroyed it becomes debris and ships can no longer move over that space.", black, -130)
        message_to_screen("Boat Size	  Hit points (HP)	    Move set	 Offensive range	     Defensive range", black, -30)
        message_to_screen("    2	            2	                3	     Hor&Ver range 2	     Vertical range 3", black, 0)
        message_to_screen("    3	            3	                2	     Hor&Ver range 3	     Vertical range 4", black, 30)
        message_to_screen("    4	            4	                1	     Hor&Ver range 4	     Vertical range 5", black, 60)

        button("exit", 462, 500, 100, 50, yellow, light_yellow, action="exit")

        pygame.display.update()

        clock.tick(15)

def What_are_cards():
    wac = True

    while wac:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(sky)

        message_to_screen("What are cards", blue, -130, size="medium")
        message_to_screen("Cards are additional aids that help you win the game more easily", black, -60)
        message_to_screen("as they can either permanently buff you ships, heal you ships, allow your", black, -30)
        message_to_screen("ships to move more steps, add more health to your ships or give them more damage.", black, 0)
        message_to_screen("There are 2 types of cards. Normal cards which exist out of: help, defensive and", black, 30)
        message_to_screen("offensive cards, trap cards and special cards. Special card usually buff", black, 60)
        message_to_screen("your ships and as such are harder to get. A player may only have 6 cards", black, 90)
        message_to_screen("in his/her hand if you end your turn with more than 6 ", black, 120)
        message_to_screen("then u must discard card until you have only 6 left.", black, 150)

        button("exit", 462, 570, 100, 50, yellow, light_yellow, action="exit")

        pygame.display.update()

        clock.tick(15)

def How_to_defend():
    htd = True

    while htd:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(sky)

        message_to_screen("How to defend", blue, -100, size="medium")
        message_to_screen("So as you may have guessed you also need to defend your own ships", black, -30)
        message_to_screen("as well as attack this can be done by turning the boat horizontally", black, 0)
        message_to_screen("in doing so you boat gains +1 range however it can only attack vertically.", black, 30)
        message_to_screen("The boat also can no longer move making it stationary it can continue to", black, 60)
        message_to_screen("move when it switches back to the attack position.", black, 90)
        message_to_screen("Switching from position also uses a move.", black, 120)

        button("exit", 462, 540, 100, 50, yellow, light_yellow, action="exit")

        pygame.display.update()

        clock.tick(15)

def How_to_use_cards():
    htuc = True

    while htuc:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(sky)

        message_to_screen("How to use cards", blue, -160, size="medium")
        message_to_screen("at any given moment during your turn you may activate a card. After a", black, -90)
        message_to_screen("card is activated its effects are used and the player discards the card", black, -60)
        message_to_screen("onto the discard pile. If a player draws a trap card at the start of a turn", black, -30)
        message_to_screen("they need to place the card faced down on the bottom row. A trap may be", black, 0)
        message_to_screen("activated even on an opponent’s turn. And a special card may be activated", black, 30)
        message_to_screen("activated only on your turn, however if a special card is a perk after the", black, 60)
        message_to_screen("the card is used the card is placed on a perk spot and its effects last for", black, 90)
        message_to_screen("the rest of the game or if the linked ship is destroyed.", black, 120)

        button("exit", 462, 530, 100, 50, yellow, light_yellow, action="exit")

        pygame.display.update()

        clock.tick(15)

def how_to_play():
    htp = True

    while htp:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(sky)
        button("Goal of the game", 140, 100, 200, 50, blue, light_blue, action="gotg")
        button("Your Turn", 140, 160, 200, 50, blue, light_blue, action="YT")
        button("How to attack", 140, 220, 200, 50, blue, light_blue, action="hta")
        button("How to get cards", 140, 280, 200, 50, blue, light_blue, action="htgc")
        button("Ship Stats", 684, 100, 200, 50, blue, light_blue, action="SS")
        button("What are cards?", 684, 160, 200, 50, blue, light_blue, action="wac")
        button("How to defend", 684, 220, 200, 50, blue, light_blue, action="htd")
        button("How to use cards", 684, 280, 200, 50, blue, light_blue, action="htuc")


        button("exit", 462, 500, 100, 50, yellow, light_yellow, action="exit")

        pygame.display.update()

        clock.tick(15)


def button(text, x, y, width, height, inactive_color, active_color, action=None):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + width > cur[0] > x and y + height > cur[1] > y:
        pygame.draw.rect(gameDisplay, active_color, (x, y, width, height))
        if click[0] == 1 and action != None:

            if action == "how to play":
                how_to_play()

            if action == "gotg":
                Goal_of_the_game()

            if action == "YT":
                Your_Turn()

            if action == "hta":
                How_to_attack()

            if action == "htgc":
                How_to_get_cards()

            if action == "SS":
                Ship_Stats()

            if action == "wac":
                What_are_cards()

            if action == "htd":
                How_to_defend()

            if action == "htuc":
                How_to_use_cards()

            if action == "exit":
                game_intro()

    else:
        pygame.draw.rect(gameDisplay, inactive_color, (x, y, width, height))

    text_to_button(text, sky, x, y, width, height)

def game_intro():
    intro = True
    music_menu("intro.mp3", 44100, -16 ,2, 4096)
    while intro:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                elif event.key == pygame.K_q:

                    pygame.quit()
                    quit()

        gameDisplay.fill(sky)
        message_to_screen("this is to test how to play", blue, -100, size="small")

        button("how to play", 412, 500, 200, 50, yellow, light_yellow, action="how to play")
        

        pygame.display.update()

        clock.tick(15)

game_intro()
=======
import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height))

pygame.display.set_caption('how to play test')

white = (255, 255, 255)
black = (0, 0, 0)

red = (200, 0, 0)
light_red = (255, 0, 0)

yellow = (200, 200, 0)
light_yellow = (255, 255, 0)

green = (34, 177, 76)
light_green = (0, 255, 0)

clock = pygame.time.Clock()

smallfont = pygame.font.SysFont("comicsansms", 15)
medfont = pygame.font.SysFont("comicsansms", 25)
largefont = pygame.font.SysFont("comicsansms", 85)

def text_objects(text, color, size="small"):
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    if size == "medium":
        textSurface = medfont.render(text, True, color)
    if size == "large":
        textSurface = largefont.render(text, True, color)

    return textSurface, textSurface.get_rect()


def text_to_button(msg, color, buttonx, buttony, buttonwidth, buttonheight, size="medium"):
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = ((buttonx + (buttonwidth / 2)), buttony + (buttonheight / 2))
    gameDisplay.blit(textSurf, textRect)


def message_to_screen(msg, color, y_displace=0, size="small"):
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = (int(display_width / 2), int(display_height / 2) + y_displace)
    gameDisplay.blit(textSurf, textRect)


def Goal_of_the_game():
    gotg = True

    while gotg:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)

        message_to_screen("Goal of the game", green, -100, size="medium")
        message_to_screen("To win the Game you need to destroy all of your opponent’s ships by shooting at", black, -30)
        message_to_screen("them with your ships. This is an easy task,however by using cards this can become", black, 0)
        message_to_screen("even easier. Use card and your ships efficiently and become victorious.", black, 30)

        button("exit", 350, 500, 100, 50, yellow, light_yellow, action="exit")

        pygame.display.update()

        clock.tick(15)

def Your_Turn():
    YT = True

    while YT:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)

        message_to_screen("Your turn", green, -100, size="medium")
        message_to_screen("When it is your turn you can move all of you ships the designated amounts", black, -30)
        message_to_screen("of steps (see ship stats). After you have placed all your boats and have", black, 0)
        message_to_screen("done your attacking the turn end and your opponents makes his move.", black, 30)

        button("exit", 350, 500, 100, 50, yellow, light_yellow, action="exit")

        pygame.display.update()

        clock.tick(15)

def How_to_attack():
    hta = True

    while hta:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)

        message_to_screen("How to attack", green, -200, size="medium")
        message_to_screen("Attacking is as easy as sitting down to play this game. Every boat has an", black, -120)
        message_to_screen("attack range that is unique to their size the bigger the ship the more", black, -90)
        message_to_screen("range they have. As long as a boat is in the attack position it can", black, -60)
        message_to_screen("attack horizontally and vertically, however if a boat is in the defense", black, -30)
        message_to_screen("position the boat can only attack vertically, but it gains +1 attack range.", black, 0)
        message_to_screen("The range of a boat is equal to the boats size and the attack width is", black, 30)
        message_to_screen("to how wide the boat is. Example: boat with size 3 has 3 range and is 3 wide", black, 60)
        message_to_screen("horizontally and has 3 range vertically and is 1 wide in the attack position.", black, 90)
        message_to_screen("Boat with size 3 has 4 range and is 3 wide in the defensive position. The", black, 120)
        message_to_screen("boat may also only move when it is in attack position. Players may attack", black, 150)
        message_to_screen("twice per turn, however only once per boat.", black, 180)

        button("exit", 350, 500, 100, 50, yellow, light_yellow, action="exit")

        pygame.display.update()

        clock.tick(15)

def How_to_get_cards():
    htgc = True

    while htgc:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)

        message_to_screen("How to get cards", green, -100, size="medium")
        message_to_screen("There are 2 types of cards normal cards and special cards. Normal", black, -30)
        message_to_screen("cards are easy to obtain at the start of the game both players", black, 0)
        message_to_screen("are given 2 cards and every time it is your turn you draw a card. Special", black, 30)
        message_to_screen("cards are harder to get you can only get them by reaching the harbor you opponent", black, 60)
        message_to_screen("opponent controls. This means you need to get behind enemy lines.", black, 90)

        button("exit", 350, 500, 100, 50, yellow, light_yellow, action="exit")

        pygame.display.update()

        clock.tick(15)

def Ship_Stats():
    SS = True

    while SS:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)

        message_to_screen("Ship Stats", green, -200, size="medium")
        message_to_screen("If a ship is destroyed it becomes debris and ships can no longer move over that space.", black, -130)
        message_to_screen("Boat Size	  Hit points (HP)	    Move set	 Offensive range	     Defensive range", black, -30)
        message_to_screen("    2	            2	                3	     Hor&Ver range 2	     Vertical range 3", black, 0)
        message_to_screen("    3	            3	                2	     Hor&Ver range 3	     Vertical range 4", black, 30)
        message_to_screen("    4	            4	                1	     Hor&Ver range 4	     Vertical range 5", black, 60)

        button("exit", 350, 500, 100, 50, yellow, light_yellow, action="exit")

        pygame.display.update()

        clock.tick(15)

def What_are_cards():
    wac = True

    while wac:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)

        message_to_screen("What are cards", green, -130, size="medium")
        message_to_screen("Cards are additional aids that help you win the game more easily", black, -60)
        message_to_screen("as they can either permanently buff you ships, heal you ships, allow your", black, -30)
        message_to_screen("ships to move more steps, add more health to your ships or give them more damage.", black, 0)
        message_to_screen("There are 2 types of cards. Normal cards which exist out of: help, defensive and", black, 30)
        message_to_screen("offensive cards, trap cards and special cards. Special card usually buff", black, 60)
        message_to_screen("your ships and as such are harder to get. A player may only have 6 cards", black, 90)
        message_to_screen("in his/her hand if you end your turn with more than 6 ", black, 120)
        message_to_screen("then u must discard card until you have only 6 left.", black, 150)

        button("exit", 350, 500, 100, 50, yellow, light_yellow, action="exit")

        pygame.display.update()

        clock.tick(15)

def How_to_defend():
    htd = True

    while htd:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)

        message_to_screen("How to defend", green, -100, size="medium")
        message_to_screen("So as you may have guessed you also need to defend your own ships", black, -30)
        message_to_screen("as well as attack this can be done by turning the boat horizontally", black, 0)
        message_to_screen("in doing so you boat gains +1 range however it can only attack vertically.", black, 30)
        message_to_screen("The boat also can no longer move making it stationary it can continue to", black, 60)
        message_to_screen("move when it switches back to the attack position.", black, 90)
        message_to_screen("Switching from position also uses a move.", black, 120)

        button("exit", 350, 500, 100, 50, yellow, light_yellow, action="exit")

        pygame.display.update()

        clock.tick(15)

def How_to_use_cards():
    htuc = True

    while htuc:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)

        message_to_screen("How to use cards", green, -160, size="medium")
        message_to_screen("at any given moment during your turn you may activate a card. After a", black, -90)
        message_to_screen("card is activated its effects are used and the player discards the card", black, -60)
        message_to_screen("onto the discard pile. If a player draws a trap card at the start of a turn", black, -30)
        message_to_screen("they need to place the card faced down on the bottom row. A trap may be", black, 0)
        message_to_screen("activated even on an opponent’s turn. And a special card may be activated", black, 30)
        message_to_screen("activated only on your turn, however if a special card is a perk after the", black, 60)
        message_to_screen("the card is used the card is placed on a perk spot and its effects last for", black, 90)
        message_to_screen("the rest of the game or if the linked ship is destroyed.", black, 120)

        button("exit", 350, 500, 100, 50, yellow, light_yellow, action="exit")

        pygame.display.update()

        clock.tick(15)

def how_to_play():
    htp = True

    while htp:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        button("Goal of the game", 100, 100, 200, 50, green, light_green, action="gotg")
        button("Your Turn", 100, 160, 200, 50, green, light_green, action="YT")
        button("How to attack", 100, 220, 200, 50, green, light_green, action="hta")
        button("How to get cards", 100, 280, 200, 50, green, light_green, action="htgc")
        button("Ship Stats", 500, 100, 200, 50, green, light_green, action="SS")
        button("What are cards?", 500, 160, 200, 50, green, light_green, action="wac")
        button("How to defend", 500, 220, 200, 50, green, light_green, action="htd")
        button("How to use cards", 500, 280, 200, 50, green, light_green, action="htuc")


        button("exit", 350, 500, 100, 50, yellow, light_yellow, action="exit")

        pygame.display.update()

        clock.tick(15)


def button(text, x, y, width, height, inactive_color, active_color, action=None):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + width > cur[0] > x and y + height > cur[1] > y:
        pygame.draw.rect(gameDisplay, active_color, (x, y, width, height))
        if click[0] == 1 and action != None:

            if action == "how to play":
                how_to_play()

            if action == "gotg":
                Goal_of_the_game()

            if action == "YT":
                Your_Turn()

            if action == "hta":
                How_to_attack()

            if action == "htgc":
                How_to_get_cards()

            if action == "SS":
                Ship_Stats()

            if action == "wac":
                What_are_cards()

            if action == "htd":
                How_to_defend()

            if action == "htuc":
                How_to_use_cards()

            if action == "exit":
                game_intro()

    else:
        pygame.draw.rect(gameDisplay, inactive_color, (x, y, width, height))

    text_to_button(text, black, x, y, width, height)

def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                elif event.key == pygame.K_q:

                    pygame.quit()
                    quit()

        gameDisplay.fill(white)
        message_to_screen("this is to test how to play", green, -100, size="small")

        button("how to play", 300, 500, 200, 50, yellow, light_yellow, action="how to play")


        pygame.display.update()

        clock.tick(15)


def gameLoop():
    gameExit = False
    gameOver = False
    FPS = 15

    while not gameExit:

        if gameOver == True:
            # gameDisplay.fill(white)
            message_to_screen("Game Over", red, -50, size="large")
            message_to_screen("Press C to play again or Q to exit", black, 50)
            pygame.display.update()
            while gameOver == True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        gameExit = True
                        gameOver = False

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_c:
                            gameLoop()
                        elif event.key == pygame.K_q:

                            gameExit = True
                            gameOver = False

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                gameExit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    pass

                elif event.key == pygame.K_RIGHT:
                    pass

                elif event.key == pygame.K_UP:
                    pass


                elif event.key == pygame.K_DOWN:
                    pass

                elif event.key == pygame.K_p:
                    pause()

        gameDisplay.fill(white)
        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()
    quit()


game_intro()
gameLoop()
>>>>>>> 150cb17e51798e83e6c29249e3f96ebefa2046c2
