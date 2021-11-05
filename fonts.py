import pygame as pg 
import os

#define with font is used for ingame text
def fonts1(string):
    game_folder = os.path.dirname(__file__)
    font_folder = os.path.join(game_folder, 'fonts')
    fontimp = pg.font.Font(os.path.join(font_folder, 'CevicheOne-Regular.ttf'),36)
    string = fontimp.render(string, True, (255, 255, 255))
    return string