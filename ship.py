import pygame as pg
from settings import *


class Ship(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load("bootje2.png")
        self.image.set_colorkey(white)
        self.rect = self.image.get_rect()
        self.rect.center = (width / 2, height / 2)

    def update(self):
        self.rect.x += 5
        if self.rect.left > width:
            self.rect.right = 0


