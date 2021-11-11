import os
import pygame as pg
from settings.settings import *

# Flyweight


class ImageChickenForeground:
    def __init__(self):
        # initialize all variables and do all the setup for a new game
        game_folder = os.path.dirname(__file__)
        img_folder = os.path.join(game_folder, '../_img/chickenforeground')
        # Make Dictionary of Images
        self.images = {}

        for i in range(1, 19):
            self.images['chickenforeground'+str(i)] = pg.transform.scale(pg.image.load(os.path.join(
                img_folder, 'chickenforeground'+str(i)+'.png')).convert_alpha(), (CHICKENFOREGROUND))

        for i in range(1, 6):
            self.images['chickenforegrounddead'+str(i)] = pg.transform.scale(pg.image.load(os.path.join(
                img_folder, 'chickenforegrounddead'+str(i)+'.png')).convert_alpha(), (CHICKENFOREGROUND))

    def getFlyweightImages(self):
        return self.images

# Factory


class ChickenForegroundFactory:
    def __init__(self):
        self.imageDict = ImageChickenForeground().getFlyweightImages()

    def createChickenForeground(self, x, y):
        chickenForeground = ChickenList(self.imageDict, x, y)
        return chickenForeground
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


class Chicken(Sprite):
    def __init__(self, flyweightImages: dict, x: int, y: int, imagename: str):
        Sprite.__init__(self, x, y, imagename)

    def update(self, position):
        self.x = self.x + position
        self.y = self.y
        self.rect.topleft = (self.x, self.y)
# Sprites


class ChickenList(Chicken):
    def __init__(self, flyweightImages: dict, x: int, y: int):
        self.x = x
        self.y = y
        self.flyweightImages = flyweightImages
        self.image = self.flyweightImages['chickenforeground1']
        self.imageIndex = 1
        self.imageIndexDead = 1
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)

        self.direction = True
        self.maxtimer = CHICKENFOREGROUNDSPEED
        self.timer = 0
        self.alive = True
        self.fullDead = False  # -------------

    # update function
    def updateChicken(self, position):
        if self.alive:
            self.rotate()
            Chicken.update(self, position)
        else:
            self.deadchicken()

    # get position of the mouse
    def getPos(self):
        return self.x, self.y

    # Checks that the hit is inside rect of signPost borders
    def checkHitChicken(self, x, y):
        # print("Sign", self.rect.left, self.rect.right,
        #       self.rect.top, self.rect.bottom)
        if self.rect.left <= x and self.rect.right >= x and self.rect.top <= y and self.rect.bottom >= y:
            print("HIT chickenforeground")
            return True
        else:
            return False

    # iterates over all .png to animate the signPost
    def rotate(self):
        if (self.direction == True):
            self.timer += 1
            if self.timer == self.maxtimer:
                self.timer = 0
                self.imageIndex += 1
                if (self.imageIndex == 19):
                    self.imageIndex = 1
                self.image = pg.transform.flip(
                    pg.transform.scale(self.flyweightImages['chickenforeground' + str(self.imageIndex)], CHICKENFOREGROUND), True, False)

    def deadchicken(self):
        self.alive = False
        self.timer += 1
        if self.timer == self.maxtimer:
            self.timer = 0
            self.imageIndexDead += 1
            if (self.imageIndexDead < 6):
                self.image = pg.transform.scale(
                    self.flyweightImages['chickenforegrounddead' + str(self.imageIndexDead)], CHICKENFOREGROUND)
            else:
                self.image.fill(TRANSPARENT)
                self.fullDead = True  # ------

    def isFullDead(self):
        return self.fullDead  # -----------
