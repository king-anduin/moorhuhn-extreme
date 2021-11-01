# Settings
WIDTH = 960
HEIGHT = 720*0.70
FPS = 60

# Sprite
SPEED = 160 / FPS
COINSPEED = int(FPS / 8)

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
SKYBLUE = (135, 206, 235, 1)

# SPAWNER is the iteration Timer for spawning new chickens
# as lower as more chickens will spawn
# Maybe usefull for dificulties
SPAWNER = 100

# flyweight.py
CHICKEN_SIZE = (70, 70)
SIGNPOST = (100, 500)

# predator.py
CURSOR_SIZE = (20, 20)
CURSOR_MID = (40, 40)

# startloop.py
BORDERRADIUS = 5
LOCATION = [(WIDTH * 0.5, 125), (WIDTH * 0.5, 225), (WIDTH * 0.5, 325)]
TEXT = ["start", "best list", "exit"]

# endloop.py
LOCATIONEND = [(WIDTH * 0.5, 125), (WIDTH * 0.5, 225)]
TEXTEND = ["menu", "exit"]

# bestlistloop.py
LOCATIONBEST = [(WIDTH * 0.5, 125), (WIDTH * 0.5, 225)]
TEXTBEST = ["menu", "Best list"]

# gameloop.py
LOCATIONGAME = [(WIDTH * 0.5, 15)]
TEXTGAME = ["Moorhuhn Extreme"]
SIZEMENUBAR = (WIDTH, HEIGHT)
