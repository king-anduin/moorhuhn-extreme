import pygame as pg
from factory import *
from settings import *
from predator import *
from background import *

# endloop = [clock, screen, Sounds, Fonts]


def endloop(endloopList):

    # GameLoop running?
    running = True

    # Endless sound loop
    endloopList[2].ende_sound.play(-1)

    while running:

        # Delta Time
        dt = endloopList[0].tick(FPS)

        # Events
        for event in pg.event.get():
            if event.type == pg.QUIT:
                endloopList[2].ende_sound.stop()
                running = False
            elif event.type == pg.MOUSEMOTION:
                # If the mouse is moved, set the center of the rect
                # to the mouse pos. You can also use pg.mouse.get_pos()
                # if you're not in the event loop.
                cursor_rect.center = event.pos

            # Ends the game on ESC
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    endloopList[2].ende_sound.stop()
                    running = False

            # Change states when selecting a rect
            elif event.type == pg.MOUSEBUTTONDOWN:
                if endloopList[4].objectsRectEnd[0].collidepoint(event.pos):
                    endloopList[2].button.play()
                    endloopList[2].ende_sound.stop()
                    running = False
                    return True

                elif endloopList[4].objectsRectEnd[1].collidepoint(event.pos):
                    endloopList[2].button.play()
                    endloopList[2].ende_sound.stop()
                    running = False

        # Render
        endloopList[1].fill((WHITE))
        endloopList[1].blit(endGameBG.image, endGameBG.rect)

        # Render text and rects for menu
        endloopList[4].drawRectEnd(endloopList[1], 2, WHITE, WIDTH *
                                   0.5 - 100, 100, 200, 50, 5)
        endloopList[4].drawText(endloopList[1], endloopList[3].font_text,
                                LOCATIONEND, TEXTEND, 2, BLACK)

        # Blit the image at the rect's topleft coords.
        endloopList[1].blit(CURSOR_IMG, cursor_rect)

        # Double Buffering
        pg.display.flip()
