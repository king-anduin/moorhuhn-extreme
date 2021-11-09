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

    def update(self):
        self.x = self.x
        self.y = self.y
        self.rect.topleft = (self.x, self.y)

# State Pattern


class TreeState:
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
        self.chickenState = TreeNormal(self)

    def changeState(self, newState: TreeState):
        if self.chickenState != None:
            self.chickenState.exit()
        self.chickenState = newState
        self.chickenState.enter()

    def aliveState(self):
        self.chickenState.alive()

    def deadState(self):
        self.chickenState.dead()


class TreeNormal(TreeState):
    def __init__(self, chickenForeground: ChickenForeground):
        self.chickenForeground = chickenForeground

    def alive(self):
        print("Sign is already in start state, SignPostStartState")

    def dead(self):
        self.chickenForeground.changeState(
            TreeAction(self.chickenForeground))

    def enter(self):
        print("Sign is in start state, SignPostStartState")

    def exit(self):
        pass


class TreeAction(TreeState):
    def __init__(self, chickenForeground: ChickenForeground):
        self.chickenForeground = chickenForeground

    def alive(self):
        self.chickenForeground.changeState(
            TreeNormal(self.chickenForeground))

    def dead(self):
        print("Sign is already in end state, SignPostEndState")

    def enter(self):
        print("sign is now in end state, SignPostEndState")

    def exit(self):
        pass
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
    def updateTrunk(self):
        Tree.update(self)

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
