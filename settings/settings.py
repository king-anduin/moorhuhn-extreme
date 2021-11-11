# Settings
WIDTH = 960
HEIGHT = 720*0.70
FPS = 60

# Sprite
SPEED = 160 / FPS
COINSPEED = int(FPS / 8)
CHICKENFOREGROUNDSPEED = int(FPS / 7)
CHICKENHOLESPEED = int(FPS / 6)
CHICKENWINDMILSPEED = int(FPS * 0.1)

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
SKYBLUE = (135, 206, 235, 1)
TRANSPARENT = (0, 0, 0, 0)

# SPAWNER is the iteration Timer for spawning new chickens
# as lower as more chickens will spawn
# Maybe usefull for dificulties
SPAWNER = 100
SPAWNERPLANE = 120
SPAWNERLEAVES = 110

# flyweight.py
CHICKEN_SIZE = (70, 70)

# signpost.py
SIGNPOSTSIZE = (379, 313)

# predator.py
CURSOR_SIZE = (20, 20)
CURSOR_MID = (40, 40)

# ammo.py
AMMOSIZE = (48, 80)
AMMOSPEED = int(FPS/16)
BULLETHOLESIZE = (35, 37)


# startloop.py
BORDERRADIUS = 5
LOCATION = [(WIDTH * 0.5, 125), (WIDTH * 0.5, 225),
            (WIDTH * 0.5, 325), (WIDTH * 0.5, 425)]
TEXT = ["Start", "Highscore", "Help", "Exit"]

# endloop.py
LOCATIONEND = [(WIDTH * 0.5, 125), (WIDTH * 0.5, 225)]
TEXTEND = ["Menu", "Exit"]

# bestlistloop.py
LOCATIONBEST = [(WIDTH * 0.5, 125), (WIDTH * 0.5, 225)]
TEXTBEST = ["Menu", "Highscore"]

# helploop.py
LOCATIONHELP = [(WIDTH * 0.5, 125), (WIDTH * 0.3, 225), (WIDTH * 0.3, 275),
                (WIDTH * 0.3, 325), (WIDTH * 0.3, 375), (WIDTH * 0.3, 425),
                (WIDTH * 0.6, 225), (WIDTH * 0.6, 275), (WIDTH * 0.6, 325),
                (WIDTH * 0.6, 375), (WIDTH * 0.6, 425)]
TEXTHELP = ["Menu", "Space", "Right Click",
            "Left Click", "Arrow Left", "Arrow Right", "Reload your weapon", "Reload your weapon",
            "Shoot", "Scroll left", "Scroll right"]
LOCATIONRECTS = [(WIDTH * 0.5 - 100, 100), (WIDTH * 0.2, 200)]
SIZERECTS = [(200, 50), (525, 250)]

# gameloop.py
LOCATIONGAME = [(WIDTH * 0.5, 15)]
TEXTGAME = ["Moorhuhn Extreme"]
SIZEMENUBAR = (WIDTH, HEIGHT)
# Distinguish between right and left mouse click
RIGHT = 3
LEFT = 1

# sprites.py
CHICKENSIZE1 = (30, 30)
CHICKENSIZE2 = (50, 50)
CHICKENSIZE3 = (70, 70)

# leaves.py
LEAVESIZE = (50, 60)

# planes.py
PLANESIZE = (45, 36)

# chickenhole.py
CHICKENHOLESIZE = (60, 60)

# chickenwindmil.py
CHICKENWINDMILSIZE = (200, 200)

# chickenforeground.py
CHICKENFOREGROUND = (300, 350)

# fonts.py
FIGURESIZE = (23, 36)
