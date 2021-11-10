import pygame as pg
from settings.settings import *
from settings.background import *

# helpLoopList = [clock, screen, Sounds, Fonts, MenuButtons, Predator]


def helpLoop(helpLoopList):
    # GameLoop running?
    running = True

    # Endless Sound loop
    helpLoopList[2].bestlist_sound.play(-1)

    while running:
        # Delta Time
        dt = helpLoopList[0].tick(FPS)

        # Events
        for event in pg.event.get():
            if event.type == pg.QUIT:
                helpLoopList[2].bestlist_sound.stop()
                running = False

            elif event.type == pg.MOUSEMOTION:
                # If the mouse is moved, set the center of the rect
                # to the mouse pos. You can also use pg.mouse.get_pos()
                # if you're not in the event loop.
                helpLoopList[5].cursor_rect.center = event.pos

            # Ends the game on ESC
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    helpLoopList[2].bestlist_sound.stop()
                    running = False

            # Change states when selecting a rect
            elif event.type == pg.MOUSEBUTTONDOWN:
                if helpLoopList[4].objectsRectHelp[0].collidepoint(event.pos):
                    helpLoopList[2].button.play()
                    helpLoopList[2].bestlist_sound.stop()
                    running = False
                    return True

        # Render
        helpLoopList[1].fill((WHITE))
        helpLoopList[1].blit(helpGameBG.image, helpGameBG.rect)

        # Render text and rects for menu
        helpLoopList[4].drawRectHelp(helpLoopList[1], 2, WHITE,
                                     WIDTH * 0.5 - 100, 100, 200, 50, 5)
        helpLoopList[4].drawText(helpLoopList[1], helpLoopList[3].font_text,
                                 LOCATIONBEST, TEXTBEST, 2, BLACK)

        # Blit the image at the rect's topleft coords.
        helpLoopList[1].blit(
            helpLoopList[5].CURSOR_IMG, helpLoopList[5].cursor_rect)

        # Double Buffering
        pg.display.flip()
