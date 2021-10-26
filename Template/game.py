import pygame
import random
import os
from factory import *
from settings import *

# Initialization
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.SCALED)
pygame.display.set_caption("Morhuhn Extreme")

# create object
sprites = []
ballFactory = BallFactory()

# pygame Clock
clock = pygame.time.Clock()

# GameLoop running?
running = True


# Create crosshair for aiming
CURSOR_IMG = pg.Surface((40, 40), pg.SRCALPHA)
pg.draw.circle(CURSOR_IMG, pg.Color('red'), (20, 20), 20, 2)
pg.draw.circle(CURSOR_IMG, pg.Color('red'), (20, 20), 2)
# Create a rect which we'll use as the blit position of the cursor.
cursor_rect = CURSOR_IMG.get_rect()


# Adding Backround img Castle
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, '_img')
bg = ((pg.image.load(os.path.join(img_folder,'backgroundCastle.png'))))
BackGround = Background(bg, [0,0])


while running:
    # Delta Time
    dt = clock.tick(FPS)



    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pg.MOUSEMOTION:
            # If the mouse is moved, set the center of the rect
            # to the mouse pos. You can also use pygame.mouse.get_pos()
            # if you're not in the event loop.
            cursor_rect.center = event.pos

        # create chicken with a click - outdated!
        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     mousex, mousey = event.pos
        #     sprites.append(ballFactory.createCoinAtPosition(mousex, mousey))

    
    #create a chicken every 50th iteration on right side of screen
    randomizer = random.randrange(1, SPAWNER, 1)
    if randomizer == 1:
        sprites.append(ballFactory.createCoinAtPosition(WIDTH-(0.12*WIDTH), random.uniform((0.1*HEIGHT), (0.9*HEIGHT)),"Left"))

    # Update
    for sprite in sprites:
        sprite.update()




    # Render
    screen.fill((255, 255, 255))
    screen.blit(BackGround.image, BackGround.rect)


    for sprite in sprites:
        screen.blit(sprite.getImage(), sprite.getRect())
    # Blit the image at the rect's topleft coords.
    screen.blit(CURSOR_IMG, cursor_rect)

    # Double Buffering
    pygame.display.flip()


# Done! Time to quit.
pygame.quit()
