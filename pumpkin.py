import os
import pygame as pg
from settings import *

# Flyweight


class Image:
    def __init__(self, image):
        self.image = pg.image.load(image).convert_alpha()


class ImagePumpkin:
    def __init__(self):
        # initialize all variables and do all the setup for a new game
        game_folder = os.path.dirname(__file__)
        img_folder = os.path.join(game_folder, '_img/pumpkin')
        # Make Dictionary of Images
        self.images = {}

        for i in range(1, 9):
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

    def update(self):
        self.x = self.x
        self.y = self.y
        self.rect.topleft = (self.x, self.y)

# State Pattern


class PumpkinState:
    def alive(self):
        raise NotImplementedError

    def dead(self):
        raise NotImplementedError

    def enter(self):
        raise NotImplementedError

    def exit(self):
        raise NotImplementedError


class ChickenForeground:
    def __init__(self):
        self.chickenState = PumpkinNormal(self)

    def changeState(self, newState: Pumpkin):
        if self.chickenState != None:
            self.chickenState.exit()
        self.chickenState = newState
        self.chickenState.enter()

    def aliveState(self):
        self.chickenState.alive()

    def deadState(self):
        self.chickenState.dead()


class PumpkinNormal(Pumpkin):
    def __init__(self, chickenForeground: ChickenForeground):
        self.chickenForeground = chickenForeground

    def alive(self):
        print("Sign is already in start state, SignPostStartState")

    def dead(self):
        self.chickenForeground.changeState(
            PumpkinShot(self.chickenForeground))

    def enter(self):
        print("Sign is in start state, SignPostStartState")

    def exit(self):
        pass


class PumpkinShot(Pumpkin):
    def __init__(self, chickenForeground: ChickenForeground):
        self.chickenForeground = chickenForeground

    def alive(self):
        self.chickenForeground.changeState(
            PumpkinNormal(self.chickenForeground))

    def dead(self):
        print("Sign is already in end state, SignPostEndState")

    def enter(self):
        print("sign is now in end state, SignPostEndState")

    def exit(self):
        pass
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
    def updatePumpkin(self):
        self.rotate()
        Pumpkin.update(self)

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
            if (self.imageIndex == 8):
                self.imageIndex = 1
            self.image = pg.transform.scale(
                self.flyweightImages['pumpkin' + str(self.imageIndex)], self.size)
