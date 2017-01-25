import pygame as pg

#   Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (200, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 200)
yellow = (255, 255, 0)
aqua = (0, 255, 255)
silver = (192, 192, 192)
dark_silver = (220, 220, 220)
bright_red = (255, 0, 0)
bright_blue = (0, 0, 255)
light_grey = (100, 100, 100)
dark_grey = (40, 40, 40)

# game settings
display_width = 1024
display_height = 768
'''display_width = 1024    # 16 * 64 or 32 * 32 or 64 * 16
display_height = 768    # # 16 * 48 or 32 * 24 or 64 * 12'''
fps = 30


tilesize = 32
Title = 'pygame test'
grid_width = display_width / tilesize
grid_height = display_height / tilesize


'''#   text font sizes
largeText = pg.font.Font('freesansbold.ttf', 115)
mediumText = pg.font.Font('freesansbold.ttf', 60)
smallText = pg.font.Font('freesansbold.ttf', 20)'''


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


#   loading images and setting the right resolution
bg_image = pg.image.load("check.png") #bg1 is vervangen
bg_image = pg.transform.scale(bg_image, (display_width, display_height))
ship_img = pg.image.load("boot4.png")