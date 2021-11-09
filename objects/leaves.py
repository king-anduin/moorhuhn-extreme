import os
import random
import pygame as pg
from settings.settings import *

# Flyweight


class Image:
    def __init__(self, image):
        self.image = pg.image.load(image).convert_alpha()


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

    def update(self):
        self.x = self.x + self.sx
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

    def update(self):
        self.x = self.x + self.sx
        self.y = self.y + self.sy
        self.rect.topleft = (self.x, self.y)

# State Pattern


class LeavesStates:
    def alive(self):
        raise NotImplementedError

    def dead(self):
        raise NotImplementedError

    def enter(self):
        raise NotImplementedError

    def exit(self):
        raise NotImplementedError


class LeaveChange:
    def __init__(self):
        self.chickenState = LeavesNormal(self)

    def changeState(self, newState: LeavesStates):
        if self.chickenState != None:
            self.chickenState.exit()
        self.chickenState = newState
        self.chickenState.enter()

    def aliveState(self):
        self.chickenState.alive()

    def deadState(self):
        self.chickenState.dead()


class LeavesNormal(LeavesStates):
    def __init__(self, chickenForeground: LeaveChange):
        self.chickenForeground = chickenForeground

    def alive(self):
        print("Sign is already in start state, SignPostStartState")

    def dead(self):
        self.chickenForeground.changeState(
            LeavesFalling(self.chickenForeground))

    def enter(self):
        print("Sign is in start state, SignPostStartState")

    def exit(self):
        pass


class LeavesFalling(LeavesStates):
    def __init__(self, chickenForeground: LeaveChange):
        self.chickenForeground = chickenForeground

    def alive(self):
        self.chickenForeground.changeState(
            LeavesNormal(self.chickenForeground))

    def dead(self):
        print("Sign is already in end state, SignPostEndState")

    def enter(self):
        print("sign is now in end state, SignPostEndState")

    def exit(self):
        pass
# Sprites


class LeavesList(Leaves):
    def __init__(self, flyweightImages: dict, x: int, y: int, sx: int, sy: int, direction: str):
        self.x = x
        self.y = y
        self.flyweightImages = flyweightImages
        self.image = self.flyweightImages['leaves1']
        self.imageIndex = 1
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)
        self.sx = sx
        self.sy = sy
        self.direction = direction

        self.maxtimer = COINSPEED
        self.timer = 0

    # update function
    def updateLeaves(self):
        self.fallingLeaves()
        Leaves.update(self)

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
