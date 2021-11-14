import pygame as pg
import os
from settings.settings import *


class Fonts:
    def __init__(self):
        self.game_folder = os.path.dirname(__file__)
        self.font_folder = os.path.join(self.game_folder, '../fonts')
        self.font_text = pg.font.Font(os.path.join(
            self.font_folder, 'comicsansms3.ttf'), 24)

    # define with font is used for ingame text
    def renderFont(self, string, *color):
        if not color:
            color = WHITE
        string = self.font_text.render(string, True, (color))
        return string
