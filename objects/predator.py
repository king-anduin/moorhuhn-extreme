import pygame as pg
import os
from settings.settings import *


class Predator():
    def __init__(self):
        # Set and load folder
        self.game_folder = os.path.dirname(__file__)
        self.img_folder = os.path.join(self.game_folder, '../_img')

        # Cursor image for the predator
        self.CURSOR_IMG = (
            (pg.image.load(os.path.join(self.img_folder, 'cursor/cursor.png')).convert_alpha()))
        self.CURSOR_IMG_MASK = pg.mask.from_surface(self.CURSOR_IMG)
        self.cursor_rect = self.CURSOR_IMG.get_rect()

        self.CURSOR_IMG_RED = (
            (pg.image.load(os.path.join(self.img_folder, 'cursor/cursorred.png')).convert_alpha()))
        self.CURSOR_IMG_RED_MASK = pg.mask.from_surface(self.CURSOR_IMG_RED)
        # Get rect for the predator image

        # # Images for the ammo
        # self.SHELL_IMG = (
        #     (pg.image.load(os.path.join(self.img_folder, 'munition/shell.png'))))
        # # Get rect for the ammo image
        # self.shell_rect = self.SHELL_IMG.get_rect()

# Create crosshair for aiming
# CURSOR_IMG = pg.Surface((CURSOR_MID), pg.SRCALPHA)
# pg.draw.circle(CURSOR_IMG, pg.Color('red'), (CURSOR_SIZE), 20, 2)
# pg.draw.circle(CURSOR_IMG, pg.Color('red'), (CURSOR_SIZE), 2)
# Create a rect which we'll use as the blit position of the cursor.
