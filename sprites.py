import pygame as pg
import random
from settings import *


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


class Ball(Sprite):
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

        # if (self.rect.right >= WIDTH):
        #     self.sx = self.sx * -1
        #     # direction is needed for flipping the chicken
        #     self.direction = "Left"

        # if (self.rect.left <= 0):
        #     self.sx = self.sx * -1
        #     # direction is needed for flipping the chicken
        #     self.direction = "Right"

        if (self.rect.top <= 0):
            self.sy = self.sy * -1


class Coin(Ball):
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
        #self.fullDead = False

        # Coin Speed
        self.maxtimer = COINSPEED
        self.timer = 0

# update function
    def update(self):
        if self.isDead == False:
            self.rotate()
            Ball.update(self)
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
                #self.fullDead = True
                # return True

    # def isFullDead(self):
    #    return self.fullDead
