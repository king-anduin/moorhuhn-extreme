import pygame as pg
from settings.settings import *
from settings.background import *
import json
# bestlistloop = [clock, screen, Sounds, Fonts, MenuButtons, Predator]


def bestlistloop(bestlistloopList):
    # GameLoop running?
    running = True

    # Endless Sound loop
    bestlistloopList[2].bestlist_sound.play(-1)

    data = {"highscores": []}
    try:
        with open("highscore\highscore.json", "r") as f:
            data = json.load(f)
    except:
        pass

    highscores = []
    highscoreLocs = []
    orders = []
    orderLocs = []
    y_offset = 50
    count = 1
    # Create best list
    for high in data["highscores"]:
        highscores.append(str(high["value"]))
        highscoreLocs.append((WIDTH * 0.5 + 100, y_offset * count + 100))
        orders.append(str(count) + ".")
        orderLocs.append((WIDTH * 0.5 - 100, y_offset * count + 100))
        count = count + 1

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
        bestlistloopList[4].drawRectBest(bestlistloopList[1], 1, WHITE,
                                         WIDTH * 0.5 - 100, 50, 200, 50, 5)
        bestlistloopList[4].drawText(bestlistloopList[1], bestlistloopList[3].font_text,
                                     LOCATIONBEST, TEXTBEST, 1, BLACK)

        # Render best list
        pg.draw.rect(bestlistloopList[1], WHITE, pg.Rect(
            WIDTH * 0.5 - 150, 125, 300, 300), border_radius=5)
        bestlistloopList[4].drawText(bestlistloopList[1], bestlistloopList[3].font_text,
                                     highscoreLocs, highscores, len(highscores), BLACK)
        bestlistloopList[4].drawText(bestlistloopList[1], bestlistloopList[3].font_text,
                                     orderLocs, orders, len(highscores), BLACK)

        # Blit the image at the rect's topleft coords.
        bestlistloopList[1].blit(
            bestlistloopList[5].CURSOR_IMG, bestlistloopList[5].cursor_rect)

        # Double Buffering
        pg.display.flip()
