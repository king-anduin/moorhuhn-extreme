import os
import pygame as pg
from settings.settings import *

# Flyweight


class ImagePumpkin:
    def __init__(self):
        # initialize all variables and do all the setup for a new game
        game_folder = os.path.dirname(__file__)
        img_folder = os.path.join(game_folder, '../_img/pumpkin')
        # Make Dictionary of Images
        self.images = {}

        for i in range(1, 10):
            self.images['pumpkin'+str(i)] = pg.transform.scale(pg.image.load(os.path.join(
                img_folder, 'pumpkin'+str(i)+'.png')).convert_alpha(), (100, 100))

    def getFlyweightImages(self):
        return self.images

# Factory


class PumpkinFactory:
    def __init__(self):
        self.imageDict = ImagePumpkin().getFlyweightImages()

    def createPumpkin(self, x, y):
        pumpkin = PumpkinList(self.imageDict, x, y)
        return pumpkin
# Sprites


class Sprite:
    def __init__(self, flyweightImages: dict, x: int, y: int, imagename: str):
        self.x = x
        self.y = y
        self.image = flyweightImages[imagename]
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)

    def update(self):
        raise NotImplementedError

    def getImage(self):
        return self.image

    def getRect(self):
        return self.rect


class Pumpkin(Sprite):
    def __init__(self, flyweightImages: dict, x: int, y: int, imagename: str):
        Sprite.__init__(self, x, y, imagename)

    def update(self, position):
        self.x = self.x + position
        self.y = self.y
        self.rect.topleft = (self.x, self.y)
# Sprites


class PumpkinList(Pumpkin):
    def __init__(self, flyweightImages: dict, x: int, y: int):
        self.x = x
        self.y = y
        self.flyweightImages = flyweightImages
        self.image = self.flyweightImages['pumpkin1']
        self.imageIndex = 1
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)

        self.size = (100, 100)
        self.maxtimer = COINSPEED
        self.timer = 0
        self.alive = True

    # update function
    def updatePumpkin(self, position, state):
        if state:
            self.rotate()
        Pumpkin.update(self, position)

    # get position of the mouse
    def getPos(self):
        return self.x, self.y

    # Checks that the hit is inside rect of signPost borders
    def checkHitPumpkin(self, x, y):
        # print("Sign", self.rect.left, self.rect.right,
        #       self.rect.top, self.rect.bottom)
        if self.rect.left <= x and self.rect.right >= x and self.rect.top <= y and self.rect.bottom >= y:
            print("HIT pumpkin")
            return True
        else:
            return False

    # iterates over all .png to animate the signPost
    def rotate(self):
        self.timer += 1
        if self.timer == self.maxtimer:
            self.timer = 0
            self.imageIndex += 1
            if (self.imageIndex == 9):
                self.imageIndex = 8
            self.image = pg.transform.scale(
                self.flyweightImages['pumpkin' + str(self.imageIndex)], self.size)
