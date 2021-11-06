import pygame as pg
from factory import *
from settings import *
from predator import *
from background import *
from fonts import *

# startloop = [clock, screen, Sounds, Fonts]


def screenLoop(startloopLoop):
    # GameLoop running?
    running = True

    # Create Buttons Object
    buttons = MenuButtons()

    # Endless sound loop
    startloopLoop[2].start_sound.play(-1)

    while running:
        # Delta Time
        dt = startloopLoop[0].tick(FPS)

        # Events
        for event in pg.event.get():
            if event.type == pg.QUIT:
                startloopLoop[2].start_sound.stop()
                running = False
            elif event.type == pg.MOUSEMOTION:
                # If the mouse is moved, set the center of the rect
                # to the mouse pos. You can also use pg.mouse.get_pos()
                # if you're not in the event loop.
                cursor_rect.center = event.pos

            # Ends the game on ESC
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    startloopLoop[2].start_sound.stop()
                    running = False

            # Change states when selecting a rect
            elif event.type == pg.MOUSEBUTTONDOWN:
                if buttons.objectsRect[0].collidepoint(event.pos):
                    running = False
                    startloopLoop[2].start_sound.stop()
                    return True
                elif buttons.objectsRect[1].collidepoint(event.pos):
                    startloopLoop[2].start_sound.stop()
                    running = False

                    return False
                elif buttons.objectsRect[2].collidepoint(event.pos):
                    startloopLoop[2].start_sound.stop()
                    running = False

        # Render
        startloopLoop[1].fill((WHITE))
        startloopLoop[1].blit(startGameBG.image, startGameBG.rect)

        # Render text and rects for menu
        buttons.drawRect(startloopLoop[1], 3, WHITE,
                         WIDTH * 0.5 - 100, 100, 200, 50, 5)
        buttons.drawText(startloopLoop[1], startloopLoop[3].font_text,
                         LOCATION, TEXT, 3, BLACK)

        # Blit the image at the rect's topleft coords.
        startloopLoop[1].blit(CURSOR_IMG, cursor_rect)

        # Double Buffering
        pg.display.flip()
