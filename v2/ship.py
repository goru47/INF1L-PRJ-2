import pygame as pg
from settings import *

"""class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.image.load("bootje22.png")
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y

    def move(self, dx=0, dy=0):
        self.x += dx
        self.y += dy

    def update(self):
        self.rect.x = self.x * tilesize
        self.rect.y = self.y * tilesize"""


class Player(pg.sprite.Sprite):
<<<<<<< HEAD
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
=======
    def __init__(self, game, x, y,hp):
        self.groups = game.all_sprites, game.player_sprites
>>>>>>> 150cb17e51798e83e6c29249e3f96ebefa2046c2
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((tilesize, 3 * tilesize))
        self.image.fill(yellow)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
<<<<<<< HEAD
=======
        self.hp = hp
>>>>>>> 150cb17e51798e83e6c29249e3f96ebefa2046c2

    def move(self, dx=0, dy=0):
        if not self.collide_wall(dx, dy):
            self.x += dx
            self.y += dy
<<<<<<< HEAD
=======
        if not self.collide_boat(dx, dy):
            self.x += dx
            self.y += dy
>>>>>>> 150cb17e51798e83e6c29249e3f96ebefa2046c2

    def collide_wall(self, dx=0, dy=0):
        for wall in self.game.wall:
            if wall.x == self.x + dx and wall.y == self.y + dy:
<<<<<<< HEAD
                return True
        return False
=======
                return False
        return True
    def collide_boat(self, dx=0, dy=0):
        for _ in self.game.player_sprites:
            if pg.sprite.spritecollideany(self,self.game.player_sprites):
                print(pg.sprite.spritecollideany(self,self.groups),(self.x,self.y))
                return False
        return True
>>>>>>> 150cb17e51798e83e6c29249e3f96ebefa2046c2

    def update(self):
        self.rect.x = self.x * tilesize
        self.rect.y = self.y * tilesize
        if self.rect.bottom > height - 2 * tilesize:
            self.rect.bottom = height - 2 * tilesize
        """if self.rect.right > WIDTH - 6 * tilesize:
            self.rect.right = WIDTH - 6 * tilesize
        elif self.rect.left < 6 * tilesize:
            self.rect.left = 6 * tilesize
        elif self.rect.top < 2 * tilesize:
            self.rect.top = 2 * tilesize"""


class Boat(pg.sprite.Sprite):
<<<<<<< HEAD
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
=======
    def __init__(self, game, x, y,hp):
        self.groups = game.all_sprites, game.player_sprites
>>>>>>> 150cb17e51798e83e6c29249e3f96ebefa2046c2
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((tilesize, 3 * tilesize))
        self.image.fill(red)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
<<<<<<< HEAD

=======
        self.hp = hp
>>>>>>> 150cb17e51798e83e6c29249e3f96ebefa2046c2
    def move(self, dx=0, dy=0):
        if not self.collide_wall(dx, dy):
            self.x += dx
            self.y += dy
<<<<<<< HEAD
=======
        if not self.collide_player(dx, dy):
            self.x += dx
            self.y += dy
>>>>>>> 150cb17e51798e83e6c29249e3f96ebefa2046c2

    def collide_wall(self, dx=0, dy=0):
        for wall in self.game.wall:
            if wall.x == self.x + dx and wall.y == self.y + dy:
                return True
        return False
<<<<<<< HEAD
=======
    def collide_player(self, dx=0, dy=0):
        for _ in self.game.player_sprites:
            if pg.sprite.spritecollideany(self,self.game.player_sprites) != None:
                print(pg.sprite.spritecollide(self,self.player_sprites),(self.x,self.y))
                return False
        return True
>>>>>>> 150cb17e51798e83e6c29249e3f96ebefa2046c2

    def update(self):
        self.rect.x = self.x * tilesize
        self.rect.y = self.y * tilesize
        if self.rect.bottom > height - 2 * tilesize:
            self.rect.bottom = height - 2 * tilesize
        """if self.rect.right > WIDTH - 6 * tilesize:
            self.rect.right = WIDTH - 6 * tilesize
        elif self.rect.left < 6 * tilesize:
            self.rect.left = 6 * tilesize
        elif self.rect.top < 2 * tilesize:
            self.rect.top = 2 * tilesize"""

class Wall(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.wall
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((tilesize, tilesize))
        self.image.fill(black)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * tilesize
        self.rect.y = y * tilesize


<<<<<<< HEAD


=======
>>>>>>> 150cb17e51798e83e6c29249e3f96ebefa2046c2
