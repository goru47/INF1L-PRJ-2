import sys
import random
from settings import *
from endplayer1won import *
from endplayer2won import *
import pygame as pg

MapSize = 20                                  #how many tiles in either direction of grid

TileWidth = 30                               #pixel sizes for grid squares
TileHeight = 25
TileMargin = 4

BLACK = (0, 0, 0)                             #some color definitions
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
AQUA = (0, 255, 255)



class MapTile(object):                       #The main class for stationary things that inhabit the grid ... water, shipwrecks, rocks and stuff.
    def __init__(self, Name, Column, Row):
        self.Name = Name
        self.Column = Column
        self.Row = Row


class Character(object):                    #Characters can move around and do cool stuff
    def __init__(self, Name, HP, Column, Row):
        self.Name = Name
        self.HP = HP
        self.Column = Column
        self.Row = Row
        self.Damage = 1
        self.Movement = 4
        self.Attack_times = 1
        self.Attack_range = 4

    def Move(self, Direction):              #This function is how a character moves around in a certain direction

        if Direction == "UP":
            if self.Row > 0:                #If within boundaries of grid
                if self.CollisionCheck("UP") == False and self.Movement > 0:       #And nothing in the way
                    self.Row -= 1            #Go ahead and move
                    self.Movement -= 1

        elif Direction == "LEFT":
            if self.Column > 0:
                if self.CollisionCheck("LEFT") == False and self.Movement > 0:
                    self.Column -= 1
                    self.Movement -= 1

        elif Direction == "RIGHT":
            if self.Column < MapSize-1:
                if self.CollisionCheck("RIGHT") == False and self.Movement > 0:
                    self.Column += 1
                    self.Movement -= 1

        elif Direction == "DOWN":
            if self.Row < MapSize-1:
                if self.CollisionCheck("DOWN") == False and self.Movement > 0:
                    self.Row += 1
                    self.Movement -= 1

        Map.update()

    def CollisionCheck(self, Direction):       #Checks if anything is in the water in the direction that the character wants to move. Used in the move function
        if Direction == "UP":
            if len(Map.Grid[self.Column][(self.Row)-1]) > 1:
                return True
        elif Direction == "LEFT":
            if len(Map.Grid[self.Column-1][(self.Row)]) > 1:
                return True
        elif Direction == "RIGHT":
            if len(Map.Grid[self.Column+1][(self.Row)]) > 1:
                return True
        elif Direction == "DOWN":
            if len(Map.Grid[self.Column][(self.Row)+1]) > 1:
                return True
        return False

    def Attack(self):
        for r in range(1, self.Attack_range + 1):
            for i in range(0, len(Map.Grid[self.Column][self.Row - r])):
                if Map.Grid[self.Column][self.Row - r][i].__class__.__name__ == "Character":
                    Map.Grid[self.Column][self.Row - r][i].HP -= self.Damage
                    print(str(self.Damage) + " damage ")
        for r in range(1, self.Attack_range + 1):
            for i in range(0, len(Map.Grid[self.Column + r][self.Row])):
                if Map.Grid[self.Column + r][self.Row][i].__class__.__name__ == "Character":
                    Map.Grid[self.Column + r][self.Row][i].HP -= self.Damage
                    print(str(self.Damage) + " damage")
        for r in range(1, self.Attack_range + 1):
            for i in range(0, len(Map.Grid[self.Column - r][self.Row])):
                if Map.Grid[self.Column - r][self.Row][i].__class__.__name__ == "Character":
                    Map.Grid[self.Column - r][self.Row][i].HP -= self.Damage
                    print(str(self.Damage) + " damage")
        for r in range(1, self.Attack_range + 1):
            for i in range(0, len(Map.Grid[self.Column][self.Row + r])):
                if Map.Grid[self.Column][self.Row + r][i].__class__.__name__ == "Character":
                    Map.Grid[self.Column][self.Row + r][i].HP -= self.Damage
                    print(str(self.Damage) + " damage")

    def Location(self):
        print("Coordinates: " + str(self.Column) + ", " + str(self.Row))


class Map(object):              #The main class; where the action happens
    global MapSize

    Grid = []

    for Row in range(MapSize):     # Creating grid
        Grid.append([])
        for Column in range(MapSize):
            Grid[Row].append([])

    for Row in range(MapSize):     #Filling grid with water
        for Column in range(MapSize):
            TempTile = MapTile("Water", Column, Row)
            Grid[Column][Row].append(TempTile)

    """for Row in range(MapSize):     #Putting some rocks near the top
        for Column in range(MapSize):
            TempTile = MapTile("Rock", Column, Row)
            if Row == 1:
                Grid[Column][Row].append(TempTile)"""

    for i in range(15):          #Placing Random shipwrecks
        RandomRow = random.randint(0, MapSize - 1)
        RandomColumn = random.randint(0, MapSize - 1)
        TempTile = MapTile("Shipwreck", RandomColumn, RandomRow)
        Grid[RandomColumn][RandomRow].append(TempTile)

    RandomRow = random.randint(0, MapSize - 1)      #Dropping the Ship in
    RandomColumn = random.randint(0, MapSize - 1)
    Ship = Character("Ship", 4, RandomColumn, RandomRow)
    RandomRow = random.randint(0, MapSize - 1)      #Dropping the enemy in
    RandomColumn = random.randint(0, MapSize - 1)
    Enemy = Character("Enemy", 4, RandomColumn, RandomRow)

    RandomRow = random.randint(0, MapSize - 1)  # Dropping the Ship2 in
    RandomColumn = random.randint(0, MapSize - 1)
    Ship2 = Character("Ship2", 4, RandomColumn, RandomRow)
    RandomRow = random.randint(0, MapSize - 1)  # Dropping the Ship3 in
    RandomColumn = random.randint(0, MapSize - 1)
    Ship3 = Character("Ship3", 4, RandomColumn, RandomRow)
    RandomRow = random.randint(0, MapSize - 1)  # Dropping the Enemy2 in
    RandomColumn = random.randint(0, MapSize - 1)
    Enemy2 = Character("Enemy2", 4, RandomColumn, RandomRow)
    RandomRow = random.randint(0, MapSize - 1)  # Dropping the Enemy3 in
    RandomColumn = random.randint(0, MapSize - 1)
    Enemy3 = Character("Enemy3", 4, RandomColumn, RandomRow)

    def update(self):        #Very important function
                             #This function goes through the entire grid
                             #And checks to see if any object's internal coordinates
                             #Disagree with its current position in the grid
                             #If they do, it removes the objects and places it
                             #on the grid according to its internal coordinates

        for Column in range(MapSize):
            for Row in range(MapSize):
                for i in range(len(Map.Grid[Column][Row])):
                    if Map.Grid[Column][Row][i].Column != Column:
                        Map.Grid[Column][Row].remove(Map.Grid[Column][Row][i])
                    elif Map.Grid[Column][Row][i].Name == "Ship":
                        Map.Grid[Column][Row].remove(Map.Grid[Column][Row][i])
                    elif Map.Grid[Column][Row][i].Name == "Enemy":
                        Map.Grid[Column][Row].remove(Map.Grid[Column][Row][i])
                    elif Map.Grid[Column][Row][i].Name == "Ship2":
                        Map.Grid[Column][Row].remove(Map.Grid[Column][Row][i])
                    elif Map.Grid[Column][Row][i].Name == "Ship3":
                        Map.Grid[Column][Row].remove(Map.Grid[Column][Row][i])
                    elif Map.Grid[Column][Row][i].Name == "Enemy2":
                        Map.Grid[Column][Row].remove(Map.Grid[Column][Row][i])
                    elif Map.Grid[Column][Row][i].Name == "Enemy3":
                        Map.Grid[Column][Row].remove(Map.Grid[Column][Row][i])
        Map.Grid[int(Map.Ship.Column)][int(Map.Ship.Row)].append(Map.Ship)
        Map.Grid[int(Map.Enemy.Column)][int(Map.Enemy.Row)].append(Map.Enemy)
        Map.Grid[int(Map.Ship2.Column)][int(Map.Ship2.Row)].append(Map.Ship2)
        Map.Grid[int(Map.Ship3.Column)][int(Map.Ship3.Row)].append(Map.Ship3)
        Map.Grid[int(Map.Enemy2.Column)][int(Map.Enemy2.Row)].append(Map.Enemy2)
        Map.Grid[int(Map.Enemy3.Column)][int(Map.Enemy3.Row)].append(Map.Enemy3)


        for column in range(MapSize):   #This checks entire grid for any dead characters and removes them
            for row in range(MapSize):
                for i in range(len(Map.Grid[column][row])):
                    if Map.Grid[column][row][i].__class__.__name__ == "Character":
                        if Map.Grid[column][row][i].HP <= 0:
                            Map.Grid[column][row].remove(Map.Grid[column][row][i])
                            # print("Character died")

Map = Map()


class States(object):
    def __init__(self):
        self.done = False
        self.next = None
        self.quit = False
        self.previous = None


class Menu(States):
    def __init__(self):
        States.__init__(self)
        self.next = 'game'
        self.screen = pg.display.set_mode((800, 600))
    def cleanup(self):
        print('cleaning up Menu state')

    def startup(self):
        print('starting Menu state')

    def button(self, naam1, naam2, x, y, w, h):
        # image, image highlight, x pos, y pos, width, height
        mouse = pg.mouse.get_pos()

        # als x pos + width groter
        if x + w > mouse[0] > x and y + h > mouse[1] > y:
            self.screen.blit(naam1, (x, y))
            self.screen.blit(naam2, (x, y))
        else:
            self.screen.blit(naam1, (x, y))

    def get_event(self, event):
        mouse = pg.mouse.get_pos()
        if event.type == pg.MOUSEBUTTONDOWN:
            if 600 + 150 > mouse[0] > 600 and 400 + 50 > mouse[1] > 150:
                self.done = True
            if 600 + 150 > mouse[0] > 600 and 500 + 50 > mouse[1] > 150:
                pass
            if 600 + 150 > mouse[0] > 600 and 450 + 50 > mouse[1] > 150:
                pass
        if event.type == pg.QUIT:
            self.done = True
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                self.done = True

    def update(self, screen, dt):
        self.draw(screen)

    def draw(self, screen):
        self.screen.blit(bg_image, (0, 0))
        self.screen.blit(title_image, (width / 5, width / 8))

        self.button(start_image1, start_image2, 600, 400, 150, 50)
        self.button(score1_image, score2_image, 600, 500, 150, 50)
        self.button(help1_image, help2_image, 600, 450, 150, 50)

        pg.display.update()


class Game(States):
    def __init__(self):
        States.__init__(self)
        self.next = 'menu'
        self.TURN = 0
        self.paused = False
        self.screen = pg.display.set_mode((800, 600))
    def cleanup(self):
        print('cleaning up Game state')

    def startup(self):
        print('starting Game state')

    def button(self, naam1, naam2, x, y, w, h):
        # image, image highlight, x pos, y pos, width, height
        mouse = pg.mouse.get_pos()

        # als x pos + width groter
        if x + w > mouse[0] > x and y + h > mouse[1] > y:
            self.screen.blit(naam1, (x, y))
            self.screen.blit(naam2, (x, y))
        else:
            self.screen.blit(naam1, (x, y))

    def get_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            Pos = pg.mouse.get_pos()
            Column = Pos[0] // (TileWidth + TileMargin)  #Translating the position of the mouse into rows and columns
            Row = Pos[1] // (TileHeight + TileMargin)
            print(str(Row) + ", " + str(Column))

            for i in range(len(Map.Grid[Column][Row])):
                print(str(Map.Grid[Column][Row][i].Name))  #p  rint stuff that inhabits that square
                if len(Map.Grid[Column][Row]) > 1:
                    if Map.Grid[Column][Row][i].__class__.__name__ == "Character":
                        print("HP: " + (str(Map.Grid[Column][Row][i].HP)))
                        print("Attack range: " + (str(Map.Grid[Column][Row][i].Attack_range)))
                        print("Moves left: " + (str(Map.Grid[Column][Row][i].Movement)))

        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_p:
                self.paused = not self.paused
            if event.key == 8:         # backspace
                self.done = True
            if event.key == 122:        # z
                player_1_win()
            if event.key == 120:        # x
                player_2_win()

            if self.TURN % 6 == 0:
                if event.key == pg.K_LEFT:
                    Map.Ship.Move("LEFT")
                if event.key == pg.K_RIGHT:
                    Map.Ship.Move("RIGHT")
                if event.key == pg.K_UP:
                    Map.Ship.Move("UP")
                if event.key == pg.K_DOWN:
                    Map.Ship.Move("DOWN")
                if event.key == 9:            # tab
                    self.TURN += 1
                    Map.Enemy.Movement = 4
                if event.key == 32:
                    Map.Ship.Attack()

            elif self.TURN % 6 == 1:
                if event.key == pg.K_LEFT:
                    Map.Enemy.Move("LEFT")
                if event.key == pg.K_RIGHT:
                    Map.Enemy.Move("RIGHT")
                if event.key == pg.K_UP:
                    Map.Enemy.Move("UP")
                if event.key == pg.K_DOWN:
                    Map.Enemy.Move("DOWN")
                if event.key == 9:
                    self.TURN += 1
                    Map.Ship2.Movement = 4
                if event.key == 32:
                    Map.Enemy.Attack()

            elif self.TURN % 6 == 2:
                if event.key == pg.K_LEFT:
                    Map.Ship2.Move("LEFT")
                if event.key == pg.K_RIGHT:
                    Map.Ship2.Move("RIGHT")
                if event.key == pg.K_UP:
                    Map.Ship2.Move("UP")
                if event.key == pg.K_DOWN:
                    Map.Ship2.Move("DOWN")
                if event.key == 9:            # enter
                    self.TURN += 1
                    Map.Enemy2.Movement = 4
                if event.key == 32:
                    Map.Ship2.Attack()

            elif self.TURN % 6 == 3:
                if event.key == pg.K_LEFT:
                    Map.Enemy2.Move("LEFT")
                if event.key == pg.K_RIGHT:
                    Map.Enemy2.Move("RIGHT")
                if event.key == pg.K_UP:
                    Map.Enemy2.Move("UP")
                if event.key == pg.K_DOWN:
                    Map.Enemy2.Move("DOWN")
                if event.key == 9:
                    self.TURN += 1
                    Map.Ship3.Movement = 4
                if event.key == 32:
                    Map.Enemy2.Attack()

            elif self.TURN % 6 == 4:
                if event.key == pg.K_LEFT:
                    Map.Ship.Move("LEFT")
                if event.key == pg.K_RIGHT:
                    Map.Ship3.Move("RIGHT")
                if event.key == pg.K_UP:
                    Map.Ship3.Move("UP")
                if event.key == pg.K_DOWN:
                    Map.Ship3.Move("DOWN")
                if event.key == 9:            # enter
                    self.TURN += 1
                    Map.Enemy3.Movement = 4
                if event.key == 32:
                    Map.Ship3.Attack()

            else:
                if event.key == pg.K_LEFT:
                    Map.Enemy3.Move("LEFT")
                if event.key == pg.K_RIGHT:
                    Map.Enemy3.Move("RIGHT")
                if event.key == pg.K_UP:
                    Map.Enemy3.Move("UP")
                if event.key == pg.K_DOWN:
                    Map.Enemy3.Move("DOWN")
                if event.key == 9:
                    self.TURN += 1
                    Map.Ship.Movement = 4
                if event.key == 32:
                    Map.Enemy3.Attack()

    def update(self, screen, dt):
        Map.update()
        self.draw(screen)
        if self.paused:
            self.screen.blit(pause_image, (0, 0))
            self.screen.blit(pauzet_image, (width / 5, width / 8))
            self.button(help1_image, help2_image, 600, 450, 150, 50)
            mouse = pg.mouse.get_pos()
            #if 600 + 130 > mouse[0] > 600 and 450 + 50 > mouse[1] > 50:
                # self.screen.blit(instbg_image, (0, 0))
                # self.screen.blit(inst1_image, (100, 0))

    def draw(self, screen):
        screen.fill(BLACK)

        for Row in range(MapSize):  # Drawing grid
            for Column in range(MapSize):
                for i in range(0, len(Map.Grid[Column][Row])):
                    Color = AQUA
                    if len(Map.Grid[Column][Row]) == 2:
                        Color = light_grey
                    if Map.Grid[Column][Row][i].Name == "Ship":
                        Color = ship_1
                    if Map.Grid[Column][Row][i].Name == "Enemy":
                        Color = enemy_1
                    if Map.Grid[Column][Row][i].Name == "Ship2":
                        Color = ship_2
                    if Map.Grid[Column][Row][i].Name == "Ship3":
                        Color = ship_3
                    if Map.Grid[Column][Row][i].Name == "Enemy2":
                        Color = enemy_2
                    if Map.Grid[Column][Row][i].Name == "Enemy3":
                        Color = enemy_3

                pg.draw.rect(screen, Color, [(TileMargin + TileWidth) * Column + TileMargin,
                                                 (TileMargin + TileHeight) * Row + TileMargin,
                                                 TileWidth,
                                                 TileHeight])


class Control:
    def __init__(self, **settings):
        self.__dict__.update(settings)
        self.done = False
        self.screen = pg.display.set_mode(self.size)
        self.clock = pg.time.Clock()

    def setup_states(self, state_dict, start_state):
        self.state_dict = state_dict
        self.state_name = start_state
        self.state = self.state_dict[self.state_name]

    def flip_state(self):
        self.state.done = False
        previous, self.state_name = self.state_name, self.state.next
        self.state.cleanup()
        self.state = self.state_dict[self.state_name]
        self.state.startup()
        self.state.previous = previous

    def update(self, dt):
        if self.state.quit:
            self.done = True
        elif self.state.done:
            self.flip_state()
        self.state.update(self.screen, dt)

    def event_loop(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.done = True
            self.state.get_event(event)

    def main_game_loop(self):
        while not self.done:
            delta_time = self.clock.tick(self.fps)/1000.0
            self.event_loop()
            self.update(delta_time)
            pg.display.update()


if __name__ == '__main__':
    settings = {
        'size': (800, 600),
        'fps': 60
    }

    app = Control(**settings)
    state_dict = {
        'menu': Menu(),
        'game': Game()
    }
    app.setup_states(state_dict, 'menu')
    app.main_game_loop()
    pg.quit()
    sys.exit()
