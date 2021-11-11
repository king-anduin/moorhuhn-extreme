import os
import pygame as pg
from settings.settings import *

# Flyweight


class ImageChickenHole:
    def __init__(self):
        # initialize all variables and do all the setup for a new game
        game_folder = os.path.dirname(__file__)
        img_folder = os.path.join(game_folder, '../_img/chickenhole')
        # Make Dictionary of Images
        self.images = {}

        for i in range(1, 15):
            self.images['chickenhole'+str(i)] = pg.transform.scale(pg.image.load(os.path.join(
                img_folder, 'chickenhole'+str(i)+'.png')).convert_alpha(), (CHICKENHOLESIZE))

    def getFlyweightImages(self):
        return self.images

# Factory


class ChickenHoleFactory:
    def __init__(self):
        self.imageDict = ImageChickenHole().getFlyweightImages()

    def createChickenHole(self, x, y, direction: str, position):
        chickenHole = ChickenHoleList(self.imageDict, x, y, direction, position)
        return chickenHole
# Sprites


class Sprite:
    def __init__(self, flyweightImages: dict, x: int, y: int, imagename: str, direction: str, position):
        self.x = x
        self.y = y
        self.image = flyweightImages[imagename]
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)
        self.direction = ""

    def update(self, position):
        self.x = self.x + position
        self.y = self.y
        self.rect.topleft = (self.x, self.y)

    def update(self):
        raise NotImplementedError

    def getImage(self):
        return self.image

    def getRect(self):
        return self.rect


class ChickenHole(Sprite):
    def __init__(self, flyweightImages: dict, x: int, y: int, imagename: str, direction: str, position):
        Sprite.__init__(self, x, y, imagename)

    def update(self, position):
        self.x = self.x + position
        self.y = self.y
        self.rect.topleft = (self.x, self.y)
# Sprites


class ChickenHoleList(ChickenHole):
    def __init__(self, flyweightImages: dict, x: int, y: int, direction: str, position):
        self.x = x
        self.y = y
        self.flyweightImages = flyweightImages
        self.image = self.flyweightImages['chickenhole1']
        self.image_mask = pg.mask.from_surface(self.image)
        self.imageIndex = 1
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)
        self.direction = direction
        self.out = False

        self.maxtimer = CHICKENHOLESPEED
        self.timer = 0

     # update function
    def updateChickenHole(self, position, out, end: bool):
        if out:
            self.rotate(end)
        ChickenHole.update(self, position)   

    # get position of the mouse
    def getPos(self):
        return self.x, self.y

    # Checks that the hit is inside rect of signPost borders
    def checkHitChickenHole(self, cursor, x, y):
        # checks for rect collision
        # if self.rect.left <= x and self.rect.right >= x and self.rect.top <= y and self.rect.bottom >= y:

        # checks for mask collition instead of rect position
        offset = (x - self.rect.topleft[0], y - self.rect.topleft[1])
        result = self.image_mask.overlap(cursor, offset)
        if result:
            print("HIT chickenhole")
            return True
        else:
            return False

    # iterates over all .png to animate the signPost
    def rotate(self, end: bool):
        self.end = end
        if not self.end:
            if (self.direction == "Out"):
                self.out = True
                self.timer += 1
                if self.timer == self.maxtimer:
                    self.timer = 0
                    self.imageIndex += 1
                    if (self.imageIndex == 14):
                        self.imageIndex = 1
                    self.image = pg.transform.scale(
                        self.flyweightImages['chickenhole' + str(self.imageIndex)], CHICKENHOLESIZE)
        else:
            self.image = self.flyweightImages['chickenhole1']
