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

        for i in range(1, 20):
            self.images['chickenforeground'+str(i)] = pg.transform.scale(pg.image.load(os.path.join(
                img_folder, 'chickenforeground'+str(i)+'.png')).convert_alpha(), (SIGNPOSTSIZE))

        for i in range(1, 6):
            self.images['chickenforegroundead'+str(i)] = pg.transform.scale(pg.image.load(os.path.join(
                img_folder, 'chickenforegroundead'+str(i)+'.png')).convert_alpha(), (SIGNPOSTSIZE))

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

# State Pattern


class ChickenForegroundState:
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
        self.chickenState = ChickenForegroundAliveState(self)

    def changeState(self, newState: ChickenForegroundState):
        if self.chickenState != None:
            self.chickenState.exit()
        self.chickenState = newState
        self.chickenState.enter()

    def aliveState(self, test):
        self.chickenState.alive()

    def deadState(self):
        self.chickenState.dead()


class ChickenForegroundAliveState(ChickenForegroundState):
    def __init__(self, chickenForeground: ChickenForeground):
        self.chickenForeground = chickenForeground

    def alive(self):
        print("Sign is already in start state, SignPostStartState")

    def dead(self):
        self.chickenForeground.changeState(
            ChickenForegroundDeadState(self.chickenForeground))

    def enter(self):
        print("Sign is in start state, SignPostStartState")

    def exit(self):
        pass


class ChickenForegroundDeadState(ChickenForegroundState):
    def __init__(self, chickenForeground: ChickenForeground):
        self.chickenForeground = chickenForeground

    def alive(self):
        self.chickenForeground.changeState(
            ChickenForegroundAliveState(self.chickenForeground))

    def dead(self):
        print("Sign is already in end state, SignPostEndState")

    def enter(self):
        print("sign is now in end state, SignPostEndState")

    def exit(self):
        pass
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
        self.size = (300, 360)
        self.maxtimer = CHICKENFOREGROUNDSPEED
        self.timer = 0
        self.alive = True

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
                    pg.transform.scale(self.flyweightImages['chickenforeground' + str(self.imageIndex)], self.size), True, False)

    def deadchicken(self):
        transparent = (0, 0, 0, 0)
        self.alive = False
        self.timer += 1
        if self.timer == self.maxtimer:
            self.timer = 0
            self.imageIndexDead += 1
            if (self.imageIndexDead < 6):
                self.image = pg.transform.scale(
                    self.flyweightImages['chickenforegroundead' + str(self.imageIndexDead)], self.size)
            else:
                self.image.fill(transparent)
