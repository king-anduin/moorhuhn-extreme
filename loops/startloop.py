import pygame as pg
from factory import *
from settings import *
from predator import *
from background import *


def screenLoop(clock, screen):
    # GameLoop running?
    running = True

    # Create Buttons Object
    buttons = MenuButtons()

    # Sprite list for signpost
    sprites = []

    # Render
    font_text = pg.font.Font("freesansbold.ttf", 24)

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

            # Ends the game on ESC
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    running = False

            # Change states when selecting a rect
            elif event.type == pg.MOUSEBUTTONDOWN:
                if buttons.objectsRect[0].collidepoint(event.pos):
                    running = False
                    return True
                elif buttons.objectsRect[1].collidepoint(event.pos):
                    running = False
                    return False
                elif buttons.objectsRect[2].collidepoint(event.pos):
                    running = False

        # Render
        screen.fill((WHITE))
        screen.blit(startGameBG.image, startGameBG.rect)

        # Render signpost
        # sprites.append(SignPostFactory.createSignPost(50, 50, 100, 150))

        # Update signpost
        # for sprite in sprites:
        #     sprite.update()

        # screen.blit(sprite.getImage(), sprite.getRect())

        # Render text and rects for menu
        buttons.drawRect(screen, 3, WHITE, WIDTH * 0.5 - 100, 100, 200, 50, 5)
        buttons.drawText(screen, font_text, LOCATION, TEXT, 3, BLACK)

        # Blit the image at the rect's topleft coords.
        screen.blit(CURSOR_IMG, cursor_rect)

        # Double Buffering
        pg.display.flip()
