import os
import pygame as pg
from settings.settings import *

# Flyweight


class ImageTree:
    def __init__(self):
        # initialize all variables and do all the setup for a new game
        game_folder = os.path.dirname(__file__)
        img_folder = os.path.join(game_folder, '../_img/world')
        # Make Dictionary of Images
        self.images = {}

        for i in range(1, 2):
            self.images['trunkSmall'+str(i)] = pg.transform.scale(pg.image.load(os.path.join(
                img_folder, 'trunkSmall'+str(i)+'.png')).convert_alpha(), (100, int(HEIGHT)))

        for i in range(1, 2):
            self.images['trunkBig'+str(i)] = pg.transform.scale(pg.image.load(os.path.join(
                img_folder, 'trunkBig'+str(i)+'.png')).convert_alpha(), (200, int(HEIGHT)))

    def getFlyweightImages(self):
        return self.images

# Factory


class TreeFactory:
    def __init__(self):
        self.imageDict = ImageTree().getFlyweightImages()

    def createTree(self, x, y, imagename: str):
        tree = TreeList(self.imageDict, x, y, imagename)
        return tree
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


class Tree(Sprite):
    def __init__(self, flyweightImages: dict, x: int, y: int, imagename: str):
        Sprite.__init__(self, x, y, imagename)

    def update(self, position):
        self.x = self.x + position
        self.y = self.y
        self.rect.topleft = (self.x, self.y)
# Sprites


class TreeList(Tree):
    def __init__(self, flyweightImages: dict, x: int, y: int, imagename: str):
        self.x = x
        self.y = y
        self.flyweightImages = flyweightImages
        self.image = self.flyweightImages[imagename]
        self.imageIndex = 1
        self.imageIndexDead = 1
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)

    # update function
    def updateTrunk(self, position):
        Tree.update(self, position)

    # get position of the mouse
    def getPos(self):
        return self.x, self.y

    # Checks that the hit is inside rect of signPost borders
    def checkHitTrunk(self, x, y):
        # print("Sign", self.rect.left, self.rect.right,
        #       self.rect.top, self.rect.bottom)
        if self.rect.left <= x and self.rect.right >= x and self.rect.top <= y and self.rect.bottom >= y:
            print("HIT tree")
            return True
        else:
            return False

    # iterates over all .png to animate the signPost
    def rotate(self):
        self.image = self.flyweightImages['trunkBig1']
