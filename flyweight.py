import os
import pygame as pg
from settings import *


class Image:
    def __init__(self, image):
        self.image = pg.image.load(image).convert_alpha()


class ImageFlyweight:
    def __init__(self):
        # initialize all variables and do all the setup for a new game
        game_folder = os.path.dirname(__file__)
        img_folder = os.path.join(game_folder, '_img/chicken')
        # Make Dictionary of Images
        self.images = {}

        for i in range(1, 12):
            self.images['chicken'+str(i)] = pg.transform.scale(pg.image.load(os.path.join(
                img_folder, 'chicken'+str(i)+'.png')).convert_alpha(), (CHICKEN_SIZE))

        for i in range(1, 9):
            self.images['chickendead'+str(i)] = pg.transform.scale(pg.image.load(os.path.join(
                img_folder, 'chickendead'+str(i)+'.png')).convert_alpha(),(CHICKEN_SIZE))

    def getFlyweightImages(self):
        return self.images


class ImageSignPost:
    def __init__(self):
        # initialize all variables and do all the setup for a new game
        game_folder = os.path.dirname(__file__)
        img_folder = os.path.join(game_folder, '_img/signpost')
        # Make Dictionary of Images
        self.images = {}

        for i in range(1, 2):
            self.images['signpost'+str(i)] = pg.transform.scale(pg.image.load(os.path.join(
                img_folder, 'signpost'+str(i)+'.png')).convert_alpha(), (SIGNPOST))

    def getFlyweightImages(self):
        return self.images


class Background(pg.sprite.Sprite):
    def __init__(self, bg, location):
        pg.sprite.Sprite.__init__(self)  # call Sprite initializer
        self.image = bg
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


class BackgroundScreens(pg.sprite.Sprite):
    def __init__(self, bg, location):
        pg.sprite.Sprite.__init__(self)  # call Sprite initializer
        self.image = bg
        self.rect = self.image.get_rect()
        self.rect.center = location


class MenuButtons(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)  # call Sprite initializer
        self.objectsRect = []

    def drawText(self, screen, font_text, location, text, amount, color):
        for i in range(amount):
            self.text = text
            self.location = location
            font_box = font_text.render(text[i], True, color)
            rect_box = font_box.get_rect()
            rect_box.center = location[i]
            screen.blit(font_box, rect_box)

    def drawRect(self, screen, amount, color, left, top, width, height, borderradius):
        y = top
        for i in range(amount):
            self.objectsRect.append(pg.Rect(left, y, width, height))
            pg.draw.rect(
                screen, color, self.objectsRect[i], border_radius=borderradius)
            y += 100
