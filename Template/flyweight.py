import os
import pygame as pg


class Image:
    def __init__(self, image):
        self.image = pg.image.load(image).convert_alpha()


class ImageFlyweight:
    def __init__(self):
        # initialize all variables and do all the setup for a new game
        game_folder = os.path.dirname(__file__)
        img_folder = os.path.join(game_folder, '_img')
        # Make Dictionary of Images
        self.images = {}
        self.images["ball"] = pg.image.load(os.path.join(
            img_folder, 'ball.png')).convert_alpha()

        for i in range(1, 12):
            self.images['chicken'+str(i)] = pg.transform.scale(pg.image.load(os.path.join(
                img_folder, 'chicken'+str(i)+'.png')).convert_alpha(),(50,50))


    def getFlyweightImages(self):
        return self.images
