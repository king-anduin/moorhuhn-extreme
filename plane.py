import os
import pygame as pg
import random

from settings import *

# Flyweight


class Image:
    def __init__(self, image):
        self.image = pg.image.load(image).convert_alpha()


class ImagePlane:
    def __init__(self):
        # initialize all variables and do all the setup for a new game
        game_folder = os.path.dirname(__file__)
        img_folder = os.path.join(game_folder, '_img/plane')
        # Make Dictionary of Images
        self.images = {}

        for i in range(1, 21):
            self.images['plane'+str(i)] = pg.transform.scale(pg.image.load(os.path.join(
                img_folder, 'plane'+str(i)+'.png')).convert_alpha(), (45, 36))

    def getFlyweightImages(self):
        return self.images

# Factory


class PlaneFactory:
    def __init__(self):
        self.imageDict = ImagePlane().getFlyweightImages()

    def createPlane(self, x, y, direction: str):
        plane = PlaneList(self.imageDict, x, y, SPEED * random.choice([1, -1, 0.5, -0.5]),
                          SPEED * random.choice([0, -0, 0, -0]), direction)
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

    def update(self):
        self.x = self.x + self.sx
        self.y = self.y + self.sy
        self.rect.topleft = (self.x, self.y)

        if (self.rect.bottom >= HEIGHT):
            self.sy = self.sy * -1

        if (self.rect.top <= 0):
            self.sy = self.sy * -1
# State Pattern


class PlaneState:
    def alive(self):
        raise NotImplementedError

    def dead(self):
        raise NotImplementedError

    def enter(self):
        raise NotImplementedError

    def exit(self):
        raise NotImplementedError


class PlaneChange:
    def __init__(self):
        self.planeState = PlaneNormal(self)

    def changeState(self, newState: PlaneState):
        if self.planeState != None:
            self.planeState.exit()
        self.planeState = newState
        self.planeState.enter()

    def aliveState(self):
        self.planeState.alive()

    def deadState(self):
        self.planeState.dead()


class PlaneNormal(PlaneState):
    def __init__(self, planeChange: PlaneChange):
        self.plane = planeChange

    def alive(self):
        print("Sign is already in start state, SignPostStartState")

    def dead(self):
        self.plane.changeState(
            PlaneFly(self.planeChange))

    def enter(self):
        print("Sign is in start state, SignPostStartState")

    def exit(self):
        pass


class PlaneFly(PlaneState):
    def __init__(self, planeChange: PlaneChange):
        self.chickenForeground = planeChange

    def alive(self):
        self.chickenForeground.changeState(
            PlaneNormal(self.chickenForeground))

    def dead(self):
        print("Sign is already in end state, SignPostEndState")

    def enter(self):
        print("sign is now in end state, SignPostEndState")

    def exit(self):
        pass

# Sprites


class PlaneList(Plane):
    def __init__(self, flyweightImages: dict, x: int, y: int, sx: int, sy: int, direction: str):
        self.x = x
        self.y = y
        self.flyweightImages = flyweightImages
        self.image = self.flyweightImages['plane1']
        self.imageIndex = 1
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)
        self.sx = sx
        self.sy = sy
        self.direction = direction
        self.size = (45, 36)

        # Coin Speed
        self.maxtimer = COINSPEED
        self.timer = 0

    # update function
    def updatePlane(self):
        self.rotate()
        Plane.update(self)

    # get position of the mouse
    def getPos(self):
        return self.x, self.y

    # Checks that the hit is inside rect of signPost borders
    def checkHitPlane(self, x, y):
        # print("Sign", self.rect.left, self.rect.right,
        #       self.rect.top, self.rect.bottom)
        if self.rect.left <= x and self.rect.right >= x and self.rect.top <= y and self.rect.bottom >= y:
            print("HIT plane")
            return True
        else:
            return False

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
                    pg.transform.scale(self.flyweightImages['plane'+str(self.imageIndex)], self.size), True, False)
        else:
            self.timer += 1
            if self.timer == self.maxtimer:
                self.timer = 0
                self.imageIndex += 1
                if (self.imageIndex == 20):
                    self.imageIndex = 1
                self.image = pg.transform.scale(
                    self.flyweightImages['plane' + str(self.imageIndex)], self.size)
