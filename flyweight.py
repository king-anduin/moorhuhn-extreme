import os
import pygame as pg
from settings import *


class Image:
    def __init__(self, image):
        self.image = pg.image.load(image).convert_alpha()


class ImageFlyweight:
    def __init__(self):
        # initialize all variables and do all the setup for a new game
        game_folder = os.path.dirname(__file__)
        img_folder = os.path.join(game_folder, '_img/chicken')
        # Make Dictionary of Images
        self.images = {}

        for i in range(1, 13):
            self.images['chicken'+str(i)] = pg.transform.scale(pg.image.load(os.path.join(
                img_folder, 'chicken'+str(i)+'.png')).convert_alpha(), (CHICKEN_SIZE))

        for i in range(1, 9):
            self.images['chickendead'+str(i)] = pg.transform.scale(pg.image.load(os.path.join(
                img_folder, 'chickendead'+str(i)+'.png')).convert_alpha(), (CHICKEN_SIZE))

    def getFlyweightImages(self):
        return self.images
