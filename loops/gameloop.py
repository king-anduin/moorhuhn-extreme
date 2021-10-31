import pygame as pg
import random
from factory import *
from settings import *
from predator import *
from background import *


def gameLoop(clock, ChickenFactory, screen, sprites):

    count = 0

    # GameLoop running?
    running = True

    while running:
        # Delta Time
        dt = clock.tick(FPS)

        # Events
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.MOUSEMOTION:
                # If the mouse is moved, set the center of the rect
                # to the mouse pos. You can also use pg.mouse.get_pos()
                # if you're not in the event loop.
                cursor_rect.center = event.pos

        # If a chicken got hit by mouse it will be removed
            if event.type == pg.MOUSEBUTTONDOWN:

                # Checks for ending the game
                if count < 5:
                    count += 1
                    mousex, mousey = event.pos
                    # print("Maus-Pos", mousex, mousey)
                    for sprite in sprites:
                        if sprite.checkHit(mousex, mousey):
                            # print(sprite.getPos())
                            sprites.remove(sprite)

                # Else Check for ending the game
                else:
                    running = False
                    return True

            # Ends the game on ESC
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    running = False

        # create a chicken every spawners iteration on right side of screen
        randomizer = random.randrange(1, SPAWNER, 1)
        if randomizer == 1:
            sprites.append(ChickenFactory.createCoinAtPosition(
                WIDTH-(0.12*WIDTH), random.uniform((0.1*HEIGHT), (0.9*HEIGHT)), "Left"))

        # Update
        for sprite in sprites:
            sprite.update()

        # Render
        screen.fill((WHITE))
        screen.blit(background.image, background.rect)

        for sprite in sprites:
            screen.blit(sprite.getImage(), sprite.getRect())

        # Blit the image at the rect's topleft coords.
        screen.blit(CURSOR_IMG, cursor_rect)

        # Double Buffering
        pg.display.flip()
