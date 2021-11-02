from settings import *
from sprites import *
from flyweight import *
import random


class ChickenFactory:
    def __init__(self):
        self.imageDict = ImageFlyweight().getFlyweightImages()

    def createBall(self, x, y, sx, sy):
        ball = Ball(self.imageDict, x, y, sx, sy, 'ball')
        return ball

    def createManyBalls(self, anzahl: int):
        spriteList = []
        for _ in range(anzahl):
            spriteList.append(self.createBall(random.randint(
                5, WIDTH-32), random.randint(5, HEIGHT-32), SPEED * random.choice([1, -1, 0.5, -0.5]), SPEED * random.choice([1, -1, 0.5, -0.5])))
        return spriteList

    def createBallAtPosition(self, x, y):
        ball = Ball(self.imageDict, x, y, SPEED * random.choice([1, -1, 0.5, -0.5]),
                    SPEED * random.choice([1, -1, 0.5, -0.5]), 'ball')
        return ball

    def createCoinAtPosition(self, x, y, direction: str):
        ball = Coin(self.imageDict, x, y, SPEED * random.choice([1, -1, 0.5, -0.5]),
                    SPEED * random.choice([1, -1, 0.5, -0.5]), direction)
        return ball


class SignPostFactory:
    def __init__(self):
        self.imageDict = ImageSignPost().getFlyweightImages()

    def createSignPost(self, x, y, sx, sy):
        signPost = SignPost(self.imageDict, x, y, sx, sy, 'left')
        return signPost
