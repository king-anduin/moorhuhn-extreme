import pygame as pg
from factory import *
from settings import *
from predator import *
from background import *
from loops.startloop import *
from loops.gameloop import *
from loops.endloop import *
from loops.bestlistloop import *

# Initialization
pg.init()
pg.mixer.init()
screen = pg.display.set_mode((WIDTH, HEIGHT), pg.SCALED)
pg.display.set_caption("Moorhuhn Extreme")

# create object
sprites = []
ChickenFactory = ChickenFactory()

# pg Clock
clock = pg.time.Clock()


class GameState:
    def start(self):
        raise NotImplementedError

    def loop(self):
        raise NotImplementedError

    def end(self):
        raise NotImplementedError

    def best(self):
        raise NotImplementedError

    def exit(self):
        raise NotImplementedError

    def enter(self):
        raise NotImplementedError


class Game:
    def __init__(self):
        self.gameState = GameStartState(self)

    def changeState(self, newState: GameState):
        if self.gameState != None:
            self.gameState.exit()
        self.gameState = newState
        self.gameState.enter()

    def startGame(self):
        self.gameState.start()

    def loopGame(self):
        self.gameState.loop()

    def bestGame(self):
        self.gameState.best()

    def endGame(self):
        self.gameState.end()


class GameStartState(GameState):
    def __init__(self, game: Game):
        self.game = game

    def start(self):
        print("Already in start screen, GameStartState")
        if screenLoop(clock, screen) == True:
            game.loopGame()
        elif screenLoop(clock, screen) == False:
            game.bestGame()

    def loop(self):
        self.game.changeState(GameLoopState(self.game))

    def best(self):
        self.game.changeState(GameBestList(self.game))

    def end(self):
        self.game.changeState(GameEndState(self.game))

    def enter(self):
        print("You enter start screen, GameStartState")
        if screenLoop(clock, screen) == True:
            game.loopGame()
        elif screenLoop(clock, screen) == False:
            game.bestGame()

    def exit(self):
        pass


class GameLoopState(GameState):
    def __init__(self, game: Game):
        self.game = game

    def start(self):
        self.game.changeState(GameStartState(self.game))

    def loop(self):
        print("Already in Game loop, GameLoopState")

    def best(self):
        self.game.changeState(GameBestList(self.game))

    def end(self):
        self.game.changeState(GameEndState(self.game))

    def enter(self):
        print("You enter game loop, GameLoopState")
        if gameLoop(clock, ChickenFactory, screen, sprites):
            game.endGame()

    def exit(self):
        pass


class GameEndState(GameState):
    def __init__(self, game: Game):
        self.game = game

    def start(self):
        self.game.changeState(GameStartState(self.game))

    def loop(self):
        self.game.changeState(GameLoopState(self.game))

    def best(self):
        self.game.changeState(GameBestList(self.game))

    def end(self):
        print("Already in End Screen")

    def enter(self):
        print("You enter end game, GameEndState")
        if endloop(clock, screen):
            game.startGame()

    def exit(self):
        pass


class GameBestList(GameState):
    def __init__(self, game: Game):
        self.game = game

    def start(self):
        self.game.changeState(GameStartState(self.game))

    def loop(self):
        self.game.changeState(GameLoopState(self.game))

    def best(self):
        print("Already in best list")

    def end(self):
        self.game.changeState(GameEndState(self.game))

    def enter(self):
        print("You enter best list, GameEndState")
        if bestlistloop(clock, screen):
            game.startGame()

    def exit(self):
        pass


# Creates game states
game = Game()

# Starts the game
game.startGame()

# Done! Time to quit.
pg.quit()
