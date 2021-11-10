import os
import pygame as pg
from settings.settings import *

# Flyweight


class ImageChickenWindmil:
    def __init__(self):
        # initialize all variables and do all the setup for a new game
        game_folder = os.path.dirname(__file__)
        img_folder = os.path.join(game_folder, '../_img/chickenwindmil')
        # Make Dictionary of Images
        self.images = {}

        for i in range(1, 37):
            self.images['chickenwindmil'+str(i)] = pg.transform.scale(pg.image.load(os.path.join(
                img_folder, 'chickenwindmil'+str(i)+'.png')).convert_alpha(), (CHICKENWINDMILSIZE))

        for i in range(0, 75):
            self.images['chickenwindmildead'+str(i)] = pg.transform.scale(pg.image.load(os.path.join(
                img_folder, 'chickenwindmildead'+str(i)+'.png')).convert_alpha(), (CHICKENWINDMILSIZE))

    def getFlyweightImages(self):
        return self.images

# Factory


class ChickenWindmilFactory:
    def __init__(self):
        self.imageDict = ImageChickenWindmil().getFlyweightImages()

    def createChickenWindmil(self, x, y, imagename: str, index: int):
        chickenWindmil = ChickenHoleList(
            self.imageDict, x, y, imagename, index)
        return chickenWindmil
# Sprites


class Sprite:
    def __init__(self, flyweightImages: dict, x: int, y: int, imagename: str, index: int):
        self.x = x
        self.y = y
        self.image = flyweightImages[imagename]
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)
        self.direction = ""

    def update(self):
        self.x = self.x
        self.y = self.y
        self.rect.topleft = (self.x, self.y)

    def update(self):
        raise NotImplementedError

    def getImage(self):
        return self.image

    def getRect(self):
        return self.rect


class ChickenHole(Sprite):
    def __init__(self, flyweightImages: dict, x: int, y: int, imagename: str):
        Sprite.__init__(self, x, y, imagename)

    def update(self):
        self.x = self.x
        self.y = self.y
        self.rect.topleft = (self.x, self.y)
# Sprites


class ChickenHoleList(ChickenHole):
    def __init__(self, flyweightImages: dict, x: int, y: int, imagename: str, index: int):
        self.x = x
        self.y = y
        self.flyweightImages = flyweightImages
        self.image = self.flyweightImages[imagename]
        self.imageIndex = index
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)

        self.maxtimer = CHICKENWINDMILSPEED
        self.timer = 0

    # update function
    def updateChickenHole(self, alive):
        self.rotate(alive)
        ChickenHole.update(self)

    # get position of the mouse
    def getPos(self):
        return self.x, self.y

    # Checks that the hit is inside rect of signPost borders
    def checkHitWindmil(self, x, y):
        if self.rect.left <= x and self.rect.right >= x and self.rect.top <= y and self.rect.bottom >= y:
            print("HIT chickenwindmil")
            return True
        else:
            return False

    # iterates over all .png to animate the signPost
    def rotate(self, alive):
        self.alive = alive
        if self.alive:
            self.timer += 1
            if self.timer == self.maxtimer:
                self.timer = 0
                self.imageIndex += 1
                if (self.imageIndex == 36):
                    self.imageIndex = 1
                self.image = pg.transform.scale(
                    self.flyweightImages['chickenwindmil' + str(self.imageIndex)], CHICKENWINDMILSIZE)
        else:
            self.timer += 1
            if self.timer == self.maxtimer:
                self.timer = 0
                self.imageIndex += 1
                if (self.imageIndex == 74):
                    self.imageIndex = 1
                self.image = pg.transform.scale(
                    self.flyweightImages['chickenwindmildead' + str(self.imageIndex)], CHICKENWINDMILSIZE)
