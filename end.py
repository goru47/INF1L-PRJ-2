
import pygame
from pygame.locals import *

pygame.init()
pygame.display.set_caption('Ending')
screen = pygame.display.set_mode((800, 600))
screen_r = screen.get_rect()
font = pygame.font.SysFont("Arial", 40)
clock = pygame.time.Clock()

def main():

    credit_list = ["Player 1 WON - Battleport"," ","Wesley Neslo - Scrum master"," Freddy da Cruz", "Suraj Doekharan ", "Joris de Putter ", "Milad Besharat ", "Mickey van Eck"]

    texts = []
    # we render the text once, since it's easier to work with surfaces

    # enumerate is being used so we can line our names up how we want it, instead of having the names in one line/sentence.
    for i, line in enumerate(credit_list):
        s = font.render(line, 1, (255, 0, 0))
        # we also create a Rect for each Surface.
        # whenever you use rects with surfaces, it may be a good idea to use sprites instead
        # we give each rect the correct starting position
        r = s.get_rect(centerx = screen_r.centerx, y = screen_r.bottom + i * 45)
        texts.append((r, s))


    while True:
        for e in pygame.event.get():
            if e.type == QUIT or e.type == KEYDOWN and e.key == pygame.K_ESCAPE:
                return

        screen.fill((0, 0, 0))

        for r, s in texts:
            # now we just move each rect by one pixel each frame
            r.move_ip(0, -1)
            # and drawing is as simple as this
            screen.blit(s, r)

        # if all rects have left the screen, we exit
        if not screen_r.collidelistall([r for (r, _) in texts]):
            return

        # update the screen -> pygame.display.update() can be used as well
        pygame.display.flip()

        # random fps
        clock.tick(60)

if __name__ == '__main__':
    main()