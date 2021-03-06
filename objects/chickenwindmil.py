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
    def __init__(self, flyweightImages: dict, x: int, y: int, imagename: str):
        Sprite.__init__(self, x, y, imagename)

    def update(self, position):
        self.x = self.x + position
        self.y = self.y
        self.rect.topleft = (self.x, self.y)
# Sprites


class ChickenHoleList(ChickenHole):
    def __init__(self, flyweightImages: dict, x: int, y: int, imagename: str, index: int):
        self.x = x
        self.y = y
        self.flyweightImages = flyweightImages
        self.image = pg.transform.scale(
            self.flyweightImages['chickenwindmil' + str(index)], CHICKENWINDMILSIZE)
        self.image_mask = pg.mask.from_surface(self.image)
        self.imageIndex = index
        self.imageIndexDead = index
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)
        self.fullDead = False
        self.isDead = False
        self.imageIndexDead1 = (self.imageIndex * 2)
        self.imageIndexDead2 = ((self.imageIndex * 2) + 2)

        self.maxtimer = CHICKENWINDMILSPEED
        self.timer = 0

    # update function
    def updateWindmil(self, position):
        if not self.isDead:
            self.rotate()
            ChickenHole.update(self, position)
        else:
            self.deadchicken()
            ChickenHole.update(self, position)

    # get position of the mouse
    def getPos(self):
        return self.x, self.y

    # Checks that the hit is inside rect of signPost borders
    def checkHitWindmil(self, cursor, x, y):
        # checks for rect collision
        # if self.rect.left <= x and self.rect.right >= x and self.rect.top <= y and self.rect.bottom >= y:

        # checks for mask collition instead of rect position
        offset = (x - self.rect.topleft[0], y - self.rect.topleft[1])
        result = self.image_mask.overlap(cursor, offset)
        if result:
            print("HIT chickenwindmil")
            return True
        else:
            return False

    # iterates over all .png to animate the signPost
    def rotate(self):
        self.timer += 1
        if self.timer == self.maxtimer:
            self.timer = 0
            self.imageIndex += 1
            self.imageIndexDead1 += 2
            self.imageIndexDead2 += 2
            if (self.imageIndex == 36):
                self.imageIndex = 1
                self.imageIndexDead1 = (self.imageIndex * 2)
                self.imageIndexDead2 = ((self.imageIndex * 2) + 2)
            self.image = pg.transform.scale(
                self.flyweightImages['chickenwindmil' + str(self.imageIndex)], CHICKENWINDMILSIZE)
            self.image_mask = pg.mask.from_surface(self.image)

    # changes the state of the chicken to dead
    def deadchicken(self):
        self.isDead = True
        self.timer += 1
        if self.timer == self.maxtimer:
            self.timer = 0
            self.imageIndexDead1 += 1
            if (self.imageIndexDead1 <= self.imageIndexDead2):
                self.image = pg.transform.scale(
                    self.flyweightImages['chickenwindmildead' + str(self.imageIndexDead1)], CHICKENWINDMILSIZE)
                self.image_mask = pg.mask.from_surface(self.image)
            else:
                self.fullDead = True

    def isFullDead(self):
        return self.fullDead
