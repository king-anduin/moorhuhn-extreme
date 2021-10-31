import pygame as pg
from flyweight import *
import os

# Adding Backround img Castle
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, '_img')
bg = ((pg.image.load(os.path.join(img_folder, 'backgroundCastle.png'))))
background = Background(bg, [0, 0])

# Adding Backround GameStartEnd
bgGameStartEnd = (
    (pg.image.load(os.path.join(img_folder, 'GameStartEnd.png'))))
GameStartEnd = Background(bgGameStartEnd, [0, 0])
