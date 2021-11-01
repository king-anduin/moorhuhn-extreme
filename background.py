import pygame as pg
from flyweight import *
import os

# Folders where all pictures are
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, '_img')

# Adding Backround random world 1
bg = ((pg.image.load(os.path.join(img_folder, 'world/background1.png'))))
background1 = Background(bg, [0, 100])

# Adding Backround random world 1
bg = ((pg.image.load(os.path.join(img_folder, 'world/background2.png'))))
background2 = Background(bg, [0, 50])

# Adding Backround start, end, bestlist screen 1
bgStartGame = (
    (pg.image.load(os.path.join(img_folder, 'backgrounds/backgroundworlds.png'))))
startGameBG = BackgroundScreens(bgStartGame, [WIDTH * 0.5, HEIGHT * 0.5])
# Adding Backround start, end, bestlist screen 2
bgEndGame = (
    (pg.image.load(os.path.join(img_folder, 'backgrounds/backgroundtarget1.png'))))
endGameBG = BackgroundScreens(bgEndGame, [WIDTH * 0.5, HEIGHT * 0.5])
# Adding Backround start, end, bestlist screen 3
bgBestList = (
    (pg.image.load(os.path.join(img_folder, 'backgrounds/backgroundtarget2.png'))))
bestListBG = BackgroundScreens(bgBestList, [WIDTH * 0.5, HEIGHT * 0.5])
