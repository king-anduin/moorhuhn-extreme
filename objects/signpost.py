import os
import pygame as pg
from settings.settings import *

# Flyweight


class ImageSignPost:
    def __init__(self):
        # initialize all variables and do all the setup for a new game
        game_folder = os.path.dirname(__file__)
        img_folder = os.path.join(game_folder, '../_img/signpost')
        # Make Dictionary of Images
        self.images = {}

        for i in range(1, 3):
            self.images['signpost'+str(i)] = pg.transform.scale(pg.image.load(os.path.join(
                img_folder, 'signpost'+str(i)+'.png')).convert_alpha(), (SIGNPOSTSIZE))

    def getFlyweightImages(self):
        return self.images

# Factory


class SignPostFactory:
    def __init__(self):
        self.imageDict = ImageSignPost().getFlyweightImages()

    def createSignPost(self, x, y):
        signPost = SignPostList(self.imageDict, x, y)
        return signPost
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


class Post(Sprite):
    def __init__(self, flyweightImages: dict, x: int, y: int, imagename: str):
        Sprite.__init__(self, x, y, imagename)

    def update(self):
        self.x = self.x
        self.y = self.y
        self.rect.topleft = (self.x, self.y)

# State Pattern


class SignPostState:
    def start(self):
        raise NotImplementedError

    def end(self):
        raise NotImplementedError

    def enter(self):
        raise NotImplementedError

    def exit(self):
        raise NotImplementedError


class SignPost:
    def __init__(self):
        self.signPostState = SignPostStartState(self)

    def changeState(self, newState: SignPostState):
        if self.signPostState != None:
            self.signPostState.exit()
        self.signPostState = newState
        self.signPostState.enter()

    def startState(self):
        self.signPostState.start()

    def endState(self):
        self.signPostState.end()


class SignPostStartState(SignPostState):
    def __init__(self, signPost: SignPost):
        self.signPost = signPost

    def start(self):
        print("Sign is already in start state, SignPostStartState")

    def end(self):
        self.signPost.changeState(SignPostEndState(self.signPost))

    def enter(self):
        print("Sign is in start state, SignPostStartState")

    def exit(self):
        pass


class SignPostEndState(SignPostState):
    def __init__(self, signPost: SignPost):
        self.signPost = signPost

    def start(self):
        self.signPost.changeState(SignPostStartState(self.signPost))

    def end(self):
        print("Sign is already in end state, SignPostEndState")

    def enter(self):
        print("sign is now in end state, SignPostEndState")

    def exit(self):
        pass
# Sprites


class SignPostList(Post):
    def __init__(self, flyweightImages: dict, x: int, y: int):
        self.x = x
        self.y = y
        self.flyweightImages = flyweightImages
        self.image = self.flyweightImages['signpost1']
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)

    # update function
    def updateSign(self, start: bool):
        self.rotate(start)
        Post.update(self)

    # get position of the mouse
    def getPos(self):
        return self.x, self.y

    # Checks that the hit is inside rect of signPost borders
    def checkHitSign(self, x, y):
        # print("Sign", self.rect.left, self.rect.right,
        #       self.rect.top, self.rect.bottom)
        if self.rect.left <= x and self.rect.right >= x and self.rect.top <= y and self.rect.bottom >= y:
            print("HIT signpost")
            return True
        else:
            return False

    # iterates over all .png to animate the signPost
    def rotate(self, start: bool):
        self.start = start
        if self.start:
            self.image = self.flyweightImages['signpost1']
        else:
            self.image = self.flyweightImages['signpost2']
