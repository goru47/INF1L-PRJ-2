from battleportV4 import *
from pygame.locals import *
import pygame as pg

pg.init()
pg.display.set_caption('Ending')
screen = pg.display.set_mode((1024, 768))
screen_r = screen.get_rect()
<<<<<<< HEAD
font = pg.font.SysFont("Arial", 40)
clock = pg.time.Clock()
=======
font = pygame.font.SysFont("Arial", 40)
clock = pygame.time.Clock()

def player_1_win():
>>>>>>> cfa1087ed63a19ac6783e65a79252ec0f0a8a734

def player_1_win():
    font = pg.font.SysFont("Arial", 40)
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
        for e in pg.event.get():
            if e.type == QUIT or e.type == KEYDOWN and e.key == pg.K_ESCAPE:
                return

        screen.fill((0, 0, 0))

        for r, s in texts:
            # now we just move each rect by one pixel each frame
            r.move_ip(0, -2)
            # and drawing is as simple as this
            screen.blit(s, r)

        # if all rects have left the screen, we exit
        if not screen_r.collidelistall([r for (r, _) in texts]):
            return

        # update the screen -> pg.display.update() can be used as well
        pg.display.flip()

        # random fps
        clock.tick(60)

<<<<<<< HEAD


#   if __name__ == '__main__':
#       main()
=======
if __name__ == '__main__':
    player_1_win()
>>>>>>> cfa1087ed63a19ac6783e65a79252ec0f0a8a734
