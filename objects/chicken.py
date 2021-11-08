import os
import random
import pygame as pg
from settings.settings import *


class Image:
    def __init__(self, image):
        self.image = pg.image.load(image).convert_alpha()


class ImageChicken:
    def __init__(self):
        # initialize all variables and do all the setup for a new game
        game_folder = os.path.dirname(__file__)
        img_folder = os.path.join(game_folder, '../_img/chicken')
        # Make Dictionary of Images
        self.images = {}

        for i in range(1, 13):
            self.images['chicken'+str(i)] = pg.transform.scale(pg.image.load(os.path.join(
                img_folder, 'chicken'+str(i)+'.png')).convert_alpha(), (CHICKEN_SIZE))

        for i in range(1, 9):
            self.images['chickendead'+str(i)] = pg.transform.scale(pg.image.load(os.path.join(
                img_folder, 'chickendead'+str(i)+'.png')).convert_alpha(), (CHICKEN_SIZE))

    def getFlyweightImages(self):
        return self.images

# Factory


class ChickenFactory:
    def __init__(self):
        self.imageDict = ImageChicken().getFlyweightImages()

    def createChicken(self, x, y, direction: str):
        chicken = ChickenList(self.imageDict, x, y, SPEED * random.choice([1, -1, 0.5, -0.5]),
                              SPEED * random.choice([0, -0, 0, -0]), direction)
        return chicken

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


class Chicken(Sprite):
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


class ChickenForegroundState:
    def alive(self):
        raise NotImplementedError

    def dead(self):
        raise NotImplementedError

    def enter(self):
        raise NotImplementedError

    def exit(self):
        raise NotImplementedError


class ChickenNormal:
    def __init__(self):
        self.chickenState = ChickenAliveState(self)

    def changeState(self, newState: ChickenForegroundState):
        if self.chickenState != None:
            self.chickenState.exit()
        self.chickenState = newState
        self.chickenState.enter()

    def aliveState(self, test):
        self.chickenState.alive()

    def deadState(self):
        self.chickenState.dead()


class ChickenAliveState(ChickenForegroundState):
    def __init__(self, chickenForeground: ChickenNormal):
        self.chickenForeground = chickenForeground

    def alive(self):
        print("Sign is already in start state, SignPostStartState")

    def dead(self):
        self.chickenForeground.changeState(
            ChickenDeadState(self.chickenForeground))

    def enter(self):
        print("Sign is in start state, SignPostStartState")

    def exit(self):
        pass


class ChickenDeadState(ChickenForegroundState):
    def __init__(self, chickenForeground: ChickenNormal):
        self.chickenForeground = chickenForeground

    def alive(self):
        self.chickenForeground.changeState(
            ChickenAliveState(self.chickenForeground))

    def dead(self):
        print("Sign is already in end state, SignPostEndState")

    def enter(self):
        print("sign is now in end state, SignPostEndState")

    def exit(self):
        pass
# Sprites


class ChickenList(Chicken):
    def __init__(self, flyweightImages: dict, x: int, y: int, sx: int, sy: int, direction: str):
        self.x = x
        self.y = y
        self.flyweightImages = flyweightImages
        self.size = random.choice([CHICKENSIZE1, CHICKENSIZE2, CHICKENSIZE3])
        self.image = pg.transform.scale(
            self.flyweightImages['chicken1'], self.size)
        self.imageIndex = 1
        self.imageIndexDead = 1
        # print(id(self.flyweightImages))
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)
        self.sx = sx
        self.sy = sy
        self.direction = direction
        self.isDead = False

        # Coin Speed
        self.maxtimer = COINSPEED
        self.timer = 0

# update function
    def update(self):
        if self.isDead == False:
            self.rotate()
            Chicken.update(self)
        else:
            self.deadchicken()

# get position of the mouse
    def getPos(self):
        return self.x, self.y

# Checks that the hit is inside rect of chicken borders
    def checkHit(self, x, y):
        # print("Huhn", self.rect.left, self.rect.right,
        #       self.rect.top, self.rect.bottom)
        if self.rect.left <= x and self.rect.right >= x and self.rect.top <= y and self.rect.bottom >= y:
            print("HIT chicken")
            return True
        else:
            return False

# iterates over all .png to animate the chicken
# if a chicken hits the wall at right or left, they will turn in that direction
    def rotate(self):
        if (self.direction == "Right"):
            self.timer += 1
            if self.timer == self.maxtimer:
                self.timer = 0
                self.imageIndex += 1
                if (self.imageIndex == 12):
                    self.imageIndex = 1
                self.image = pg.transform.flip(
                    pg.transform.scale(self.flyweightImages['chicken'+str(self.imageIndex)], self.size), True, False)
        else:
            self.timer += 1
            if self.timer == self.maxtimer:
                self.timer = 0
                self.imageIndex += 1
                if (self.imageIndex == 12):
                    self.imageIndex = 1
                self.image = pg.transform.scale(
                    self.flyweightImages['chicken' + str(self.imageIndex)], self.size)

# changes the state of the chicken to dead
    def deadchicken(self):
        transparent = (0, 0, 0, 0)
        self.isDead = True
        self.timer += 1
        if self.timer == self.maxtimer:
            self.timer = 0
            self.imageIndexDead += 1
            if (self.imageIndexDead <= 8):
                self.image = pg.transform.scale(
                    self.flyweightImages['chickendead' + str(self.imageIndexDead)], self.size)
            else:
                self.image.fill(transparent)
                # return True
