import pygame
vec = pygame.math.Vector2
from abc import ABC, abstractmethod
from settings.settings import *
from settings.background import *

class Camera:
    def __init__(self, player):
        self.player = player

    def setmethod(self, method):
        self.method = method

    def scroll(self):
        self.method.scroll()

class CamScroll(ABC):
    def __init__(self, camera,player):
        self.camera = camera
        self.player = player

    @abstractmethod
    def scroll(self):
        pass


class Border(CamScroll):
    def __init__(self, camera, player):
        CamScroll.__init__(self, camera, player)
        self.offset = camera
        self.offset_x = self.offset[0]
        self.offset_y = self.offset[1]

    def scroll(self):        
        if self.player[0] < 50 or WIDTH - self.player[0] < 50:
            self.offset_x += (self.camera[0] - self.offset_x)
            self.offset_y += (self.camera[1] - self.offset_y)
            self.offset = (int(self.offset_x), int(self.offset_y))
