import pygame as pg
from factory import *
from settings import *
from predator import *
from background import *

# bestlistloop = [clock, screen, Sounds, Fonts]


def bestlistloop(bestlistloopList):
    # GameLoop running?
    running = True

    # Create Buttons Object
    buttons = MenuButtons()

    # Endless Sound loop
    bestlistloopList[2].bestlist_sound.play(-1)

    while running:
        # Delta Time
        dt = bestlistloopList[0].tick(FPS)

        # Events
        for event in pg.event.get():
            if event.type == pg.QUIT:
                bestlistloopList[2].bestlist_sound.stop()
                running = False

            elif event.type == pg.MOUSEMOTION:
                # If the mouse is moved, set the center of the rect
                # to the mouse pos. You can also use pg.mouse.get_pos()
                # if you're not in the event loop.
                cursor_rect.center = event.pos

            # Ends the game on ESC
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    bestlistloopList[2].bestlist_sound.stop()
                    running = False

            # Change states when selecting a rect
            elif event.type == pg.MOUSEBUTTONDOWN:
                if buttons.objectsRect[0].collidepoint(event.pos):
                    bestlistloopList[2].bestlist_sound.stop()
                    running = False

                    return True

        # Render
        bestlistloopList[1].fill((WHITE))
        bestlistloopList[1].blit(bestListBG.image, bestListBG.rect)

        # Render text and rects for menu
        buttons.drawRect(bestlistloopList[1], 2, WHITE,
                         WIDTH * 0.5 - 100, 100, 200, 50, 5)
        buttons.drawText(bestlistloopList[1], bestlistloopList[3].font_text,
                         LOCATIONBEST, TEXTBEST, 2, BLACK)

        # Blit the image at the rect's topleft coords.
        bestlistloopList[1].blit(CURSOR_IMG, cursor_rect)

        # Double Buffering
        pg.display.flip()
