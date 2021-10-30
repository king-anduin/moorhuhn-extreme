from background import *


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

    def loop(self):
        self.game.changeState(GameLoopState(self.game))

    def best(self):
        self.game.changeState(GameBestList(self.game))

    def end(self):
        self.game.changeState(GameEndState(self.game))

    def enter(self):
        print("You enter start screen, GameLoopState")

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

    def exit(self):
        pass
