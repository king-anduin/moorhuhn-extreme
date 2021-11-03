import pygame as pg
from factory import *
from settings import *
from predator import *
from background import *


def bestlistloop(clock, screen):
    # GameLoop running?
    running = True

    # Create Buttons Object
    buttons = MenuButtons()

    # Render
    font_text = pg.font.Font("freesansbold.ttf", 24)
    # Sounds
    bestlist_sound = pg.mixer.Sound("sounds/bestlist.mp3")
    bestlist_sound.play(-1)

    while running:
        # Delta Time
        dt = clock.tick(FPS)

        # Events
        for event in pg.event.get():
            if event.type == pg.QUIT:
                bestlist_sound.stop()
                running = False

            elif event.type == pg.MOUSEMOTION:
                # If the mouse is moved, set the center of the rect
                # to the mouse pos. You can also use pg.mouse.get_pos()
                # if you're not in the event loop.
                cursor_rect.center = event.pos

            # Ends the game on ESC
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    bestlist_sound.stop()
                    running = False

            # Change states when selecting a rect
            elif event.type == pg.MOUSEBUTTONDOWN:
                if buttons.objectsRect[0].collidepoint(event.pos):
                    bestlist_sound.stop()
                    running = False

                    return True

        # Render
        screen.fill((WHITE))
        screen.blit(bestListBG.image, bestListBG.rect)

        # Render text and rects for menu
        buttons.drawRect(screen, 2, WHITE, WIDTH * 0.5 - 100, 100, 200, 50, 5)
        buttons.drawText(screen, font_text, LOCATIONBEST, TEXTBEST, 2, BLACK)

        # Blit the image at the rect's topleft coords.
        screen.blit(CURSOR_IMG, cursor_rect)

        # Double Buffering
        pg.display.flip()
