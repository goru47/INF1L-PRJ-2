import random
import pygame

pygame.init()                                 #start up dat pygame
clock = pygame.time.Clock()                   #for framerate or something? still not very sure
Screen = pygame.display.set_mode([650, 650])  #making the window
Done = False                                  #variable to keep track if window is open
MapSize = 20                                  #how many tiles in either direction of grid

TileWidth = 20                                #pixel sizes for grid squares
TileHeight = 20
TileMargin = 4

BLACK = (0, 0, 0)                             #some color definitions
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
AQUA = (0, 255, 255)

TURN = 0


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

    def Attack(self, Direction):

        for x in range(1, 5):
            if Direction == "UP":
                if len(Map.Grid[self.Column][(self.Row)-x]) > 1:
                    print("Enemy in sight", x, "tiles away")
            elif Direction == "LEFT":
                if len(Map.Grid[self.Column-x][(self.Row)]) > 1:
                    print("Enemy in sight", x, "tiles away")
            elif Direction == "RIGHT":
                if len(Map.Grid[self.Column+x][(self.Row)]) > 1:
                    print("Enemy in sight", x, "tiles away")
            elif Direction == "DOWN":
                if len(Map.Grid[self.Column][(self.Row)+x]) > 1:
                    print("Enemy in sight", x, "tiles away")
        return False

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

    RandomRow = random.randint(0, MapSize - 1)      #Dropping the hero in
    RandomColumn = random.randint(0, MapSize - 1)
    Hero = Character("Hero", 10, RandomColumn, RandomRow)
    RandomRow = random.randint(0, MapSize - 1)      #Dropping the enemy in
    RandomColumn = random.randint(0, MapSize - 1)
    Enemy = Character("Enemy", 10, RandomColumn, RandomRow)

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
                    elif Map.Grid[Column][Row][i].Name == "Hero":
                        Map.Grid[Column][Row].remove(Map.Grid[Column][Row][i])
                    elif Map.Grid[Column][Row][i].Name == "Enemy":
                        Map.Grid[Column][Row].remove(Map.Grid[Column][Row][i])
        Map.Grid[int(Map.Hero.Column)][int(Map.Hero.Row)].append(Map.Hero)
        Map.Grid[int(Map.Enemy.Column)][int(Map.Enemy.Row)].append(Map.Enemy)

Map = Map()

while not Done:     #Main pygame loop
    TURN = TURN
    for event in pygame.event.get():         #catching events
        if event.type == pygame.QUIT:
            Done = True

        elif event.type == pygame.MOUSEBUTTONDOWN:
            Pos = pygame.mouse.get_pos()
            Column = Pos[0] // (TileWidth + TileMargin)  #Translating the position of the mouse into rows and columns
            Row = Pos[1] // (TileHeight + TileMargin)
            print(str(Row) + ", " + str(Column))

            for i in range(len(Map.Grid[Column][Row])):
                   print(str(Map.Grid[Column][Row][i].Name))  #print stuff that inhabits that square

        elif event.type == pygame.KEYDOWN:
            if TURN % 2 == 0:
                if event.key == pygame.K_LEFT:
                    Map.Hero.Move("LEFT")
                if event.key == pygame.K_RIGHT:
                    Map.Hero.Move("RIGHT")
                if event.key == pygame.K_UP:
                    Map.Hero.Move("UP")
                if event.key == pygame.K_DOWN:
                    Map.Hero.Move("DOWN")
                if event.key == 116:
                    TURN += 1
                    Map.Enemy.Movement = 4
                if event.key == 32:
                    Map.Hero.Attack("LEFT")
                    Map.Hero.Attack("RIGHT")
                    Map.Hero.Attack("UP")
                    Map.Hero.Attack("DOWN")
                    """if event.key == pygame.K_LEFT:
                        Map.Hero.Move("LEFT")
                    if event.key == pygame.K_RIGHT:
                        Map.Hero.Move("RIGHT")
                    if event.key == pygame.K_UP:
                        Map.Hero.Move("UP")
                    if event.key == pygame.K_DOWN:
                        Map.Hero.Move("DOWN")"""

            else:
                if event.key == pygame.K_LEFT:
                    Map.Enemy.Move("LEFT")
                if event.key == pygame.K_RIGHT:
                    Map.Enemy.Move("RIGHT")
                if event.key == pygame.K_UP:
                    Map.Enemy.Move("UP")
                if event.key == pygame.K_DOWN:
                    Map.Enemy.Move("DOWN")
                if event.key == 116:
                    TURN += 1
                    Map.Hero.Movement = 4

    Screen.fill(BLACK)

    for Row in range(MapSize):           # Drawing grid
        for Column in range(MapSize):
            for i in range(0, len(Map.Grid[Column][Row])):
                Color = AQUA
                if len(Map.Grid[Column][Row]) == 2:
                    Color = RED
                if Map.Grid[Column][Row][i].Name == "Hero":
                    Color = GREEN
                if Map.Grid[Column][Row][i].Name == "Enemy":
                    Color = BLACK


            pygame.draw.rect(Screen, Color, [(TileMargin + TileWidth) * Column + TileMargin,
                                             (TileMargin + TileHeight) * Row + TileMargin,
                                             TileWidth,
                                             TileHeight])

    clock.tick(60)      #Limit to 60 fps or something

    pygame.display.flip()     #Honestly not sure what this does, but it breaks if I remove it
    Map.update()

pygame.quit()