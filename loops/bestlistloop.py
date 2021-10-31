import pygame as pg
from factory import *
from settings import *
from predator import *
from background import *


def bestlistloop(clock, screen):
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

            # Ends the game on ESC
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    running = False

            # Change states when selecting a rect
            elif event.type == pg.MOUSEBUTTONDOWN:
                if objectsRect[0].collidepoint(event.pos):
                    running = False
                    return True

        # Render
        screen.fill((WHITE))
        screen.blit(GameStartEnd.image, GameStartEnd.rect)

        # Render
        font_text = pg.font.Font("freesansbold.ttf", 24)

        # Render rects for options on screen
        y = 50
        objectsRect = []
        for i in range(2):
            objectsRect.append(pg.Rect(200, y, 150, 50))
            pg.draw.rect(
                screen, WHITE, objectsRect[i], border_radius=BORDERRADIUS)
            y += 100

        # Render text for buttons on screen
        for i in range(2):
            text = ["menu", "Best list"]
            location = [(250, 50), (250, 150), (250, 250)]
            font_box = font_text.render(text[i], True, [0, 0, 0])
            rect_box = font_box.get_rect()
            rect_box.left, rect_box.top = location[i]
            screen.blit(font_box, rect_box)

        # Blit the image at the rect's topleft coords.
        screen.blit(CURSOR_IMG, cursor_rect)

        # Double Buffering
        pg.display.flip()
