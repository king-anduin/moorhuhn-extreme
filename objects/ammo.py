import os
import pygame as pg
from settings.settings import *

# Flyweight


class ImageAmmo:
    def __init__(self):
        # initialize all variables and do all the setup for a new game
        game_folder = os.path.dirname(__file__)
        img_folder = os.path.join(game_folder, '../_img/ammo')
        img_bullethole = os.path.join(game_folder, '../_img/bullethole')
        # Make Dictionary of Images
        self.images = {}

        for i in range(1, 18):
            self.images['Ammo'+str(i)] = pg.transform.scale(pg.image.load(os.path.join(
                img_folder, 'Ammo'+str(i)+'.png')).convert_alpha(), (AMMOSIZE))

        for i in range(1, 2):
            self.images['bullethole'+str(i)] = pg.transform.scale(pg.image.load(os.path.join(
                img_bullethole, 'bullethole'+str(i)+'.png')).convert_alpha(), (BULLETHOLESIZE))

    def getFlyweightImages(self):
        return self.images

# Factory


class AmmoFactory:
    def __init__(self):
        self.imageDict = ImageAmmo().getFlyweightImages()

    def createAmmo(self, coordinates, imagename: str):
        ammo = AmmoList(
            self.imageDict, coordinates[0], coordinates[1], imagename)
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
    def __init__(self, flyweightImages: dict, x: int, y: int, imagename: str):
        self.x = x
        self.y = y
        self.flyweightImages = flyweightImages
        self.image = self.flyweightImages[imagename]
        self.imageIndex = 1
        self.imageIndexDead = 1
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)

        self.direction = True
        self.size = (300, 360)
        self.maxtimer = AMMOSPEED
        self.timer = 0
        self.alive = True
        self.fullDead = False

    # update function
    def updateAmmo(self):
        if self.alive:
            # self.rotate()
            Ammo.update(self)
        else:
            self.deadAmmo()

    # get position of the mouse
    def getPos(self):
        return self.x, self.y

    # rotate#--------------------------------#-------------------------------
    # checkHitAmmo--------------------------------#--------------------------------

    def deadAmmo(self):
        transparent = (0, 0, 0, 0)
        self.alive = False
        self.timer += 1
        if self.timer == self.maxtimer:
            self.timer = 0
            self.imageIndexDead += 1
            if (self.imageIndexDead < 18):  # --------------------------------
                self.image = self.flyweightImages['Ammo' +
                                                  str(self.imageIndexDead)]
            else:
                self.image.fill(transparent)
                self.fullDead = True

    def isFullDead(self):
        return self.fullDead
