import os
import pygame as pg
from settings.settings import *

# Flyweight


class Image:
    def __init__(self, image):
        self.image = pg.image.load(image).convert_alpha()


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

# State Pattern


class ChickenHoleStates:
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
        self.chickenState = ChickenHoleNormal(self)

    def changeState(self, newState: ChickenHoleStates):
        if self.chickenState != None:
            self.chickenState.exit()
        self.chickenState = newState
        self.chickenState.enter()

    def aliveState(self):
        self.chickenState.alive()

    def deadState(self):
        self.chickenState.dead()


class ChickenHoleNormal(ChickenHoleStates):
    def __init__(self, chickenForeground: LeaveChange):
        self.chickenForeground = chickenForeground

    def alive(self):
        print("Sign is already in start state, SignPostStartState")

    def dead(self):
        self.chickenForeground.changeState(
            ChickenHoleOut(self.chickenForeground))

    def enter(self):
        print("Sign is in start state, SignPostStartState")

    def exit(self):
        pass


class ChickenHoleOut(ChickenHoleStates):
    def __init__(self, chickenForeground: LeaveChange):
        self.chickenForeground = chickenForeground

    def alive(self):
        self.chickenForeground.changeState(
            ChickenHoleNormal(self.chickenForeground))

    def dead(self):
        print("Sign is already in end state, SignPostEndState")

    def enter(self):
        print("sign is now in end state, SignPostEndState")

    def exit(self):
        pass
# Sprites


class ChickenHoleList(ChickenHole):
    def __init__(self, flyweightImages: dict, x: int, y: int, direction: str, position):
        self.x = x
        self.y = y
        self.flyweightImages = flyweightImages
        self.image = self.flyweightImages['chickenhole1']
        self.imageIndex = 1
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)
        self.direction = direction
        self.out = False

        self.maxtimer = CHICKENHOLESPEED
        self.timer = 0

     # update function
    def updateChickenHole(self, position, out):
        if out:
            self.rotate()
        ChickenHole.update(self, position)   

    # get position of the mouse
    def getPos(self):
        return self.x, self.y

    # Checks that the hit is inside rect of signPost borders
    def checkHitChickenHole(self, x, y):
        if self.rect.left <= x and self.rect.right >= x and self.rect.top <= y and self.rect.bottom >= y:
            print("HIT chickenhole")
            return True
        else:
            return False

    # iterates over all .png to animate the signPost
    def rotate(self):
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
