import pygame as pg
from settings import *

# Create crosshair for aiming
CURSOR_IMG = pg.Surface((CURSOR_MID), pg.SRCALPHA)
pg.draw.circle(CURSOR_IMG, pg.Color('red'), (CURSOR_SIZE), 20, 2)
pg.draw.circle(CURSOR_IMG, pg.Color('red'), (CURSOR_SIZE), 2)
# Create a rect which we'll use as the blit position of the cursor.
cursor_rect = CURSOR_IMG.get_rect()
