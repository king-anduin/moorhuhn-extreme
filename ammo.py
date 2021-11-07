import os
import pygame as pg
from settings import *

# Flyweight


class ImageAmmo:
    def __init__(self):
        # initialize all variables and do all the setup for a new game
        game_folder = os.path.dirname(__file__)
        img_folder = os.path.join(game_folder, '_img/ammo')
        # Make Dictionary of Images
        self.images = {}

        for i in range(1, 3):
            self.images['Ammo'+str(i)] = pg.transform.scale(pg.image.load(os.path.join(
                img_folder, 'Ammo'+str(i)+'.png')).convert_alpha(), (AMMOSIZE))

    def getFlyweightImages(self):
        return self.images

# Factory


class AmmoFactory:
    def __init__(self):
        self.imageDict = ImageAmmo().getFlyweightImages()

    def createAmmo(self, x, y):
        ammo = AmmoList(self.imageDict, x, y)
        return ammo
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


class AmmoSprite(Sprite):
    def __init__(self, flyweightImages: dict, x: int, y: int, imagename: str):
        Sprite.__init__(self, x, y, imagename)

    def update(self):
        self.x = self.x
        self.y = self.y
        self.rect.topleft = (self.x, self.y)

# State Pattern


class AmmoState:
    def alive(self):
        raise NotImplementedError

    def dead(self):
        raise NotImplementedError

    def enter(self):
        raise NotImplementedError

    def exit(self):
        raise NotImplementedError


class Ammo(AmmoSprite):
    def __init__(self):
        self.ammoState = AmmoAliveState(self)

    def changeState(self, newState: AmmoState):
        if self.ammoState != None:
            self.ammoState.exit()
        self.ammoState = newState
        self.ammoState.enter()

    def aliveState(self):
        self.ammoState.alive()

    def deadState(self):
        self.ammoState.dead()


class AmmoAliveState(AmmoState):
    def __init__(self, ammo: Ammo):
        self.ammo = ammo

    def alive(self):
        print("Sign is already in start state, SignPostStartState")

    def dead(self):
        self.ammo.changeState(
            AmmoDeadState(self.ammo))

    def enter(self):
        print("Sign is in start state, SignPostStartState")

    def exit(self):
        pass


class AmmoDeadState(AmmoState):
    def __init__(self, ammo: Ammo):
        self.ammo = ammo

    def alive(self):
        self.ammo.changeState(
            AmmoAliveState(self.ammo))

    def dead(self):
        print("Sign is already in end state, SignPostEndState")

    def enter(self):
        print("sign is now in end state, SignPostEndState")

    def exit(self):
        pass
# Sprites


class AmmoList(Ammo):
    def __init__(self, flyweightImages: dict, x: int, y: int):
        self.x = x
        self.y = y
        self.flyweightImages = flyweightImages
        self.image = self.flyweightImages['Ammo1']
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
    def updateAmmo(self):
        if self.alive:
            self.rotate()
            Ammo.update(self)
        else:
            self.deadAmmo()

    # get position of the mouse
    def getPos(self):
        return self.x, self.y

    # Checks that the hit is inside rect of signPost borders
    def checkHitAmmo(self, x, y):
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
                    pg.transform.scale(self.flyweightImages['Ammo' + str(self.imageIndex)], self.size), True, False)

    def deadAmmo(self):
        transparent = (0, 0, 0, 0)
        self.alive = False
        self.timer += 1
        if self.timer == self.maxtimer:
            self.timer = 0
            self.imageIndexDead += 1
            if (self.imageIndexDead < 6):
                self.image = pg.transform.scale(
                    self.flyweightImages['Ammo' + str(self.imageIndexDead)], self.size)
            else:
                self.image.fill(transparent)
