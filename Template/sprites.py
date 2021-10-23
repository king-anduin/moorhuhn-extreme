import pygame as pg
import os
from settings import *


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


class Ball(Sprite):
    def __init__(self, flyweightImages: dict, x: int, y: int, sx: int, sy: int, imagename: str):
        Sprite.__init__(self, x, y, imagename)
        self.sx = sx
        self.sy = sy

    def update(self):
        self.x = self.x + self.sx
        self.y = self.y + self.sy
        self.rect.topleft = (self.x, self.y)

        if (self.rect.bottom >= HEIGHT):
            self.sy = self.sy * -1

        if (self.rect.right >= WIDTH):
            self.sx = self.sx * -1

        if (self.rect.left <= 0):
            self.sx = self.sx * -1

        if (self.rect.top <= 0):
            self.sy = self.sy * -1


class Coin(Ball):
    def __init__(self, flyweightImages: dict, x: int, y: int, sx: int, sy: int):
        self.x = x
        self.y = y
        self.flyweightImages = flyweightImages
        self.image = self.flyweightImages['coin1']
        self.imageIndex = 1
        print(id(self.flyweightImages))
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)
        self.sx = sx
        self.sy = sy

        # Coin Speed
        self.maxtimer = COINSPEED
        self.timer = 0

    def update(self):
        self.rotate()
        Ball.update(self)

    def rotate(self):
        self.timer += 1
        if self.timer == self.maxtimer:
            self.timer = 0
            self.imageIndex += 1
            if (self.imageIndex == 9):
                self.imageIndex = 1
            self.image = self.flyweightImages['coin'+str(self.imageIndex)]