import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 30
HEIGHT = 30

# This sets the margin between each cell
MARGIN = 5

# Create a 2 dimensional array. A two dimensional
# array is simply a list of lists.
grid = []
for row in range(20):
    # Add an empty array that will hold each cell
    # in this row
    grid.append([])
    for column in range(20):
        grid[row].append(0)  # Append a cell

# Set row 1, cell 5 to one.
# rows and column numbers start at zero.
grid[0][10] = 1

# Initialize pygame
pygame.init()

# [width, height]
WINDOW_SIZE = [1280, 720]
screen = pygame.display.set_mode(WINDOW_SIZE)

# screen title
pygame.display.set_caption("Banaan")
boot = pygame.image.load("bootje.png")

# loop until close button is used
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# main loop
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # in order to close the game
            done = True  # type true in order to show that you are done with the loop
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # when you click, the mouse posotion will be the output

            pos = pygame.mouse.get_pos()
            # Change the x/y screen coordinates to grid coordinates
            column = pos[0] // (WIDTH + MARGIN)
            row = pos[1] // (HEIGHT + MARGIN)
            # Set that location to one
            grid[row][column] = 1
            print("Click ", pos, "Grid coordinates: ", row, column)

    # Background color
    screen.fill(BLACK)

    # Drawing the grid
    for row in range(20):
        for column in range(20):
            color = WHITE
            if grid[row][column] == 1:
                color = BLACK

            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])



    # 60 fps
    clock.tick(60)

# update the screen to show what you want to have drawn
    pygame.display.flip()


pygame.quit()