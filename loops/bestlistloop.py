import pygame as pg
from settings.settings import *
from settings.background import *

# bestlistloop = [clock, screen, Sounds, Fonts, MenuButtons, Predator, Highscore]


def bestlistloop(bestlistloopList):
    # GameLoop running?
    running = True

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
                bestlistloopList[5].cursor_rect.center = event.pos

            # Ends the game on ESC
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    bestlistloopList[2].bestlist_sound.stop()
                    running = False

            # Change states when selecting a rect
            elif event.type == pg.MOUSEBUTTONDOWN:
                if bestlistloopList[4].objectsRectBest[0].collidepoint(event.pos):
                    bestlistloopList[2].button.play()
                    bestlistloopList[2].bestlist_sound.stop()
                    running = False
                    return True

        # Render
        bestlistloopList[1].fill((WHITE))
        bestlistloopList[1].blit(bestListBG.image, bestListBG.rect)

        # Render text and rects for menu
        bestlistloopList[4].drawRectBest(bestlistloopList[1], 2, WHITE,
                                         LOCATIONRECTSBEST, SIZERECTSBEST, 5)
        bestlistloopList[4].drawText(bestlistloopList[1], bestlistloopList[3].font_text,
                                     LOCATIONBEST, bestlistloopList[6].getHighscore(), 13, BLACK)

        # Blit the image at the rect's topleft coords.
        bestlistloopList[1].blit(
            bestlistloopList[5].CURSOR_IMG, bestlistloopList[5].cursor_rect)

        # Double Buffering
        pg.display.flip()
