import os
import random
import pygame as pg
from settings.settings import *

# Flyweight


class ImageLeave:
    def __init__(self):
        # initialize all variables and do all the setup for a new game
        game_folder = os.path.dirname(__file__)
        img_folder = os.path.join(game_folder, '../_img/fallingleaf')
        # Make Dictionary of Images
        self.images = {}

        for i in range(1, 21):
            self.images['leaves'+str(i)] = pg.transform.scale(pg.image.load(os.path.join(
                img_folder, 'leaves'+str(i)+'.png')).convert_alpha(), (LEAVESIZE))

        for i in range(0, 25):
            self.images['leavesshot'+str(i)] = pg.transform.scale(pg.image.load(os.path.join(
                img_folder, 'leavesshot'+str(i)+'.png')).convert_alpha(), (LEAVESIZE))

    def getFlyweightImages(self):
        return self.images

# Factory


class LeavesFactory:
    def __init__(self):
        self.imageDict = ImageLeave().getFlyweightImages()

    def createLeaves(self, x, y, direction: str):
        leaves = LeavesList(self.imageDict, x, y, SPEED * random.choice([0, -0, 0, -0]),
                            SPEED * random.choice([1, 1, 0.5, 0.5]), direction)
        return leaves
# Sprites


class Sprite:
    def __init__(self, flyweightImages: dict, x: int, y: int, sx: int, sy: int, imagename: str, direction: str):
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


class Leaves(Sprite):
    def __init__(self, flyweightImages: dict, x: int, y: int, sx: int, sy: int, imagename: str, direction: str):
        Sprite.__init__(self, x, y, imagename)
        self.sx = sx
        self.sy = sy

    def update(self, position, falling):
        self.x = self.x + position
        self.y = self.y
        if falling:
            self.x = self.x + self.sx
            self.y = self.y + self.sy
        self.rect.topleft = (self.x, self.y)
# Sprites


class LeavesList(Leaves):
    def __init__(self, flyweightImages: dict, x: int, y: int, sx: int, sy: int, direction: str):
        self.x = x
        self.y = y
        self.flyweightImages = flyweightImages
        self.image = self.flyweightImages['leaves1']
        self.imageIndex = 1
        self.imageIndexShot = 0
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)
        self.sx = sx
        self.sy = sy
        self.direction = direction
        self.shot = False
        self.fullDead = False

        self.maxtimer = COINSPEED
        self.timer = 0

    # update function
    def updateLeaves(self, position, falling):
        if falling:
            self.fallingLeaves()
        Leaves.update(self, position, falling)
    def updateLeaves(self, position, falling):
        if not self.shot:
            if falling:
                self.fallingLeaves()
            Leaves.update(self, position, falling)
        else:
            if falling:
                self.fallingShot()
            Leaves.update(self, position, falling)

    # get position of the mouse
    def getPos(self):
        return self.x, self.y

    # Checks that the hit is inside rect of signPost borders
    def checkHitLeaves(self, x, y):
        if self.rect.left <= x and self.rect.right >= x and self.rect.top <= y and self.rect.bottom >= y:
            print("HIT leaves")
            return True
        else:
            return False

    # iterates over all .png to animate the signPost
    def fallingLeaves(self):
        if (self.direction == "Down"):
            self.timer += 1
            if self.timer == self.maxtimer:
                self.timer = 0
                self.imageIndex += 1
                if (self.imageIndex == 20):
                    self.imageIndex = 1
                self.image = pg.transform.scale(
                    self.flyweightImages['leaves' + str(self.imageIndex)], LEAVESIZE)

    def fallingShot(self):
        self.shot = True
        self.timer += 1
        if self.timer == self.maxtimer:
            self.timer = 0
            self.imageIndexShot += 1
            if (self.imageIndexShot < 25):
                self.image = pg.transform.scale(
                    self.flyweightImages['leavesshot' + str(self.imageIndexShot)], LEAVESIZE)
            else:
                self.image.fill(TRANSPARENT)
                self.fullDead = True  # ------

    def isFullDead(self):
        return self.fullDead  # -----------
