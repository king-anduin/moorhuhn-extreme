from importmodules import *

# Initialization
pg.init()
pg.mixer.init()
screen = pg.display.set_mode((WIDTH, int(HEIGHT)), pg.SCALED)
pg.display.set_caption("Moorhuhn Extreme")

# creates object
ChickenFactory = ChickenFactory()

# Create Object
SignPostFactory = SignPostFactory()

# Create Object
AmmoFactory = AmmoFactory()

# Create Object
ChickenHoleFactory = ChickenHoleFactory()

# Create Object
TreeFactory = TreeFactory()

# Create Predator
Predator = Predator()

# Create Object
ChickenForegroundFactory = ChickenForegroundFactory()

# Create Object
PumpkinFactory = PumpkinFactory()

# Create Object
PlaneFactory = PlaneFactory()

# Create Object
ChickenWindmilFactory = ChickenWindmilFactory()

# Create Object
LeavesFactory = LeavesFactory()

# Create Sounds Object
Sounds = Sounds()

# create font object
Fonts = Fonts()

# Create Buttons Object
MenuButtons = MenuButtons()

# observer
ObserverSubject = Player()

# pg Clock
clock = pg.time.Clock()

# List for handing over to loops
startloopList = [clock, screen, Sounds,
                 Fonts, MenuButtons, Predator, AmmoFactory, ChickenHoleFactory]
gameloopList = [clock, screen, ChickenFactory, SignPostFactory,
                ChickenForegroundFactory, Sounds, Fonts, MenuButtons, TreeFactory,
                PumpkinFactory, PlaneFactory, LeavesFactory, ChickenHoleFactory, Predator, AmmoFactory, ObserverSubject, ChickenWindmilFactory]
endloopList = [clock, screen, Sounds, Fonts, MenuButtons, Predator]
bestlistloopList = [clock, screen, Sounds, Fonts, MenuButtons, Predator]
helpLoopList = [clock, screen, Sounds, Fonts, MenuButtons, Predator]


class GameState:
    def start(self):
        raise NotImplementedError

    def loop(self):
        raise NotImplementedError

    def end(self):
        raise NotImplementedError

    def best(self):
        raise NotImplementedError

    def help(self):
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

    def helpGame(self):
        self.gameState.help()

    def endGame(self):
        self.gameState.end()


class GameStartState(GameState):
    def __init__(self, game: Game):
        self.game = game

    def start(self):
        print("Already in start screen, GameStartState")
        check = screenLoop(startloopList)
        if check == 1:
            game.loopGame()
        elif check == 2:
            game.bestGame()
        elif check == 3:
            game.helpGame()

    def loop(self):
        self.game.changeState(GameLoopState(self.game))

    def best(self):
        self.game.changeState(GameBestList(self.game))

    def help(self):
        self.game.changeState(GameHelpState(self.game))

    def end(self):
        self.game.changeState(GameEndState(self.game))

    def enter(self):
        print("You enter start screen, GameStartState")
        check = screenLoop(startloopList)
        if check == 1:
            game.loopGame()
        elif check == 2:
            game.bestGame()
        elif check == 3:
            game.helpGame()

    def exit(self):
        pass


class GameLoopState(GameState):
    def __init__(self, game: Game):
        self.game = game

    def start(self):
        self.game.changeState(GameStartState(self.game))

    def loop(self):
        print("Already in Game loop, GameLoopState")

    def end(self):
        self.game.changeState(GameEndState(self.game))

    def enter(self):
        print("You enter game loop, GameLoopState")
        if gameLoop(gameloopList):
            game.endGame()

    def exit(self):
        pass


class GameEndState(GameState):
    def __init__(self, game: Game):
        self.game = game

    def start(self):
        self.game.changeState(GameStartState(self.game))

    def best(self):
        self.game.changeState(GameBestList(self.game))

    def end(self):
        print("Already in End Screen, GameEndState")

    def enter(self):
        print("You enter end game, GameEndState")
        if endloop(endloopList):
            game.startGame()

    def exit(self):
        pass


class GameBestList(GameState):
    def __init__(self, game: Game):
        self.game = game

    def start(self):
        self.game.changeState(GameStartState(self.game))

    def best(self):
        print("Already in best list, GameBestList")

    def end(self):
        self.game.changeState(GameEndState(self.game))

    def enter(self):
        print("You enter best list, GameBestList")
        if bestlistloop(bestlistloopList):
            game.startGame()

    def exit(self):
        pass


class GameHelpState(GameState):
    def __init__(self, game: Game):
        self.game = game

    def start(self):
        self.game.changeState(GameStartState(self.game))

    def best(self):
        self.game.changeState(GameBestList(self.game))

    def help(self):
        print("Already in help Screen, GameHelpState")

    def enter(self):
        print("You enter help game, GameHelpState")
        if helpLoop(helpLoopList):
            game.startGame()

    def exit(self):
        pass


# Creates game states
game = Game()

# Starts the game
game.loopGame()

# Done! Time to quit.
pg.quit()
