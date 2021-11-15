import os
import pygame as pg
import random
from settings.settings import *

# Flyweight


class ImagePlane:
    def __init__(self):
        # initialize all variables and do all the setup for a new game
        game_folder = os.path.dirname(__file__)
        img_folder = os.path.join(game_folder, '../_img/plane')
        # Make Dictionary of Images
        self.images = {}

        for i in range(0, 21):
            self.images['plane'+str(i)] = pg.transform.scale(pg.image.load(os.path.join(
                img_folder, 'plane'+str(i)+'.png')).convert_alpha(), PLANESIZE)

        for i in range(0, 1):
            self.images['planebanner'+str(i)] = pg.transform.scale(pg.image.load(os.path.join(
                img_folder, 'planebanner'+str(i)+'.png')).convert_alpha(), PLANESIZE)

    def getFlyweightImages(self):
        return self.images

# Factory


class PlaneFactory:
    def __init__(self):
        self.imageDict = ImagePlane().getFlyweightImages()

    def createPlane(self, x, y, direction: str, imagename: str, speed: int):
        plane = PlaneList(self.imageDict, x, y, speed,
                          0, direction, imagename)
        return plane

# Sprites


class Sprite:
    def __init__(self, flyweightImages: dict, x: int, y: int, imagename: str, direction: str):
        self.x = x
        self.y = y
        self.image = flyweightImages[imagename]
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)
        self.direction = ""

    def update(self, position):
        self.x = self.x + self.sx + position
        self.y = self.y + self.sy
        self.rect.topleft = (self.x, self.y)

    def update(self):
        raise NotImplementedError

    def getImage(self):
        return self.image

    def getRect(self):
        return self.rect


class Plane(Sprite):
    def __init__(self, flyweightImages: dict, x: int, y: int, sx: int, sy: int, imagename: str, direction: str):
        Sprite.__init__(self, x, y, imagename)
        self.sx = sx
        self.sy = sy

    def update(self, position):
        self.x = self.x + self.sx + position
        self.y = self.y + self.sy
        self.rect.topleft = (self.x, self.y)
# Sprites


class PlaneList(Plane):
    def __init__(self, flyweightImages: dict, x: int, y: int, sx: int, sy: int, direction: str, imagename: str):
        self.x = x
        self.y = y
        self.flyweightImages = flyweightImages
        self.image = self.flyweightImages[imagename]
        self.imageIndex = 1
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)
        self.sx = sx
        self.sy = sy
        self.direction = direction

        # Coin Speed
        self.maxtimer = COINSPEED
        self.timer = 0

    # update function
    def updatePlane(self, position):
        self.rotate()
        Plane.update(self, position)

    # update function banner
    def updateBanner(self, position):
        self.planeBanner()
        Plane.update(self, position)

    # get position of the mouse
    def getPos(self):
        return self.x, self.y

    # Checks that the hit is inside rect of signPost borders
    def checkHitPlane(self, x, y):
        # checks for rect collision
        if self.rect.left <= x and self.rect.right >= x and self.rect.top <= y and self.rect.bottom >= y:

            # checks for mask collition instead of rect position
            # offset = (x - self.rect.topleft[0], y - self.rect.topleft[1])
            # result = self.image_mask.overlap(cursor, offset)
            # if result:
            print("HIT plane")
            return True
        else:
            return False

    def planeBanner(self):
        self.image = self.flyweightImages['planebanner0']

    # iterates over all .png to animate the signPost
    def rotate(self):
        if (self.direction == "Right"):
            self.timer += 1
            if self.timer == self.maxtimer:
                self.timer = 0
                self.imageIndex += 1
                if (self.imageIndex == 20):
                    self.imageIndex = 1
                self.image = pg.transform.flip(
                    pg.transform.scale(self.flyweightImages['plane'+str(self.imageIndex)], PLANESIZE), True, False)
        else:
            self.timer += 1
            if self.timer == self.maxtimer:
                self.timer = 0
                self.imageIndex += 1
                if (self.imageIndex == 20):
                    self.imageIndex = 1
                self.image = pg.transform.scale(
                    self.flyweightImages['plane' + str(self.imageIndex)], PLANESIZE)
