import pygame as pg
import os
from settings import *


class Fonts:
    def __init__(self):
        self.game_folder = os.path.dirname(__file__)
        self.font_folder = os.path.join(self.game_folder, 'fonts')
        self.font_text = pg.font.Font(os.path.join(
            self.font_folder, 'comicsansms3.ttf'), 24)

    # define with font is used for ingame text
    def renderFont(self, string):
        string = self.font_text.render(string, True, (WHITE))
        return string
