import pygame

pygame.init()

display_width = 800
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

boot_width = 73

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('bana')
clock = pygame.time.Clock()

boot = pygame.image.load('bootje.png')


def boot1(x, y):
    gameDisplay.blit(boot,(x, y))


def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.8)

    x_change = 0
    y_change = 0

    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -20
                if event.key == pygame.K_RIGHT:
                    x_change = 20
                if event.key == pygame.K_UP:
                    y_change = -20
                if event.key == pygame.K_DOWN:
                    y_change = 20

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                    y_change = 0

        x += x_change
        y += y_change

        gameDisplay.fill(white)
        boot1(x, y)

        if display_width > 0 or display_width < 700 or display_height > 0 or display_height < 500:
            x_change = 0
            y_change = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = False

        pygame.display.update()
        clock.tick(60)


game_loop()
pygame.quit()
quit()