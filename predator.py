import pygame as pg
import os
from settings import *

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, '_img')

# Create crosshair for aiming
# CURSOR_IMG = pg.Surface((CURSOR_MID), pg.SRCALPHA)
CURSOR_IMG = ((pg.image.load(os.path.join(img_folder, 'cursor/cursor.png'))))
# pg.draw.circle(CURSOR_IMG, pg.Color('red'), (CURSOR_SIZE), 20, 2)
# pg.draw.circle(CURSOR_IMG, pg.Color('red'), (CURSOR_SIZE), 2)
# Create a rect which we'll use as the blit position of the cursor.
cursor_rect = CURSOR_IMG.get_rect()

# Create ammo image
SHELL_IMG = ((pg.image.load(os.path.join(img_folder, 'munition/shell.png'))))
# Get the rect of the ammo image
shell_rect = SHELL_IMG.get_rect()
