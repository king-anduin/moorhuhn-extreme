import pygame as pg
from settings import *


class MenuButtons():
    def __init__(self):
        pg.sprite.Sprite.__init__(self)  # call Sprite initializer
        self.objectsRectStart = []
        self.objectsRectGame = []
        self.objectsRectEnd = []
        self.objectsRectBest = []

    def drawText(self, screen, font_text, location, text, amount, color):
        for i in range(amount):
            self.text = text
            self.location = location
            font_box = font_text.render(text[i], True, color)
            rect_box = font_box.get_rect()
            rect_box.center = location[i]
            screen.blit(font_box, rect_box)

    def drawRectStart(self, screen, amount, color, left, top, width, height, borderradius):
        y = top
        for i in range(amount):
            self.objectsRectStart.append(pg.Rect(left, y, width, height))
            pg.draw.rect(
                screen, color, self.objectsRectStart[i], border_radius=borderradius)
            y += 100

    def drawRectGame(self, screen, amount, color, left, top, width, height, borderradius):
        y = top
        for i in range(amount):
            self.objectsRectGame.append(pg.Rect(left, y, width, height))
            pg.draw.rect(
                screen, color, self.objectsRectGame[i], border_radius=borderradius)
            y += 100

    def drawRectEnd(self, screen, amount, color, left, top, width, height, borderradius):
        y = top
        for i in range(amount):
            self.objectsRectEnd.append(pg.Rect(left, y, width, height))
            pg.draw.rect(
                screen, color, self.objectsRectEnd[i], border_radius=borderradius)
            y += 100

    def drawRectBest(self, screen, amount, color, left, top, width, height, borderradius):
        y = top
        for i in range(amount):
            self.objectsRectBest.append(pg.Rect(left, y, width, height))
            pg.draw.rect(
                screen, color, self.objectsRectBest[i], border_radius=borderradius)
            y += 100
