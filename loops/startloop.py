import pygame as pg
import time

from settings.settings import *
from settings.background import *
from settings.fonts import *

# startloop = [clock, screen, Sounds, Fonts, MenuButtons, Predator,
#               AmmoFactory, ChickenHoleFactory]


def screenLoop(startloopLoop):
    # GameLoop running?
    running = True

    # Endless sound loop
    startloopLoop[2].start_sound.play(-1)

    # list, boolean and coordinates for bulletholes
    spritesBullethole = []
    spritesBulletholeAppend = True
    coordinates = [(330, 230), (500, 265),
                   (355, 355), (600, 400)]

    # list and boolean for chickenhole
    spritesChickenHole = []
    spritesChickenHoleOut = False
    spritesChickenHoleCreated = True
    spritesEnd = False

    # time initiater variable
    timerinitialiser = 0

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
                startloopLoop[5].cursor_rect.center = event.pos

            # Ends the game on ESC
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    startloopLoop[2].start_sound.stop()
                    running = False

            # Change states when selecting a rect
            elif event.type == pg.MOUSEBUTTONDOWN:
                if startloopLoop[4].objectsRectStart[0].collidepoint(event.pos):
                    startloopLoop[2].button.play()
                    startloopLoop[2].start_sound.stop()
                    running = False
                    return 1

                elif startloopLoop[4].objectsRectStart[1].collidepoint(event.pos):
                    startloopLoop[2].button.play()
                    startloopLoop[2].start_sound.stop()
                    running = False
                    return 2

                elif startloopLoop[4].objectsRectStart[2].collidepoint(event.pos):
                    startloopLoop[2].button.play()
                    startloopLoop[2].start_sound.stop()
                    running = False
                    return 3

                elif startloopLoop[4].objectsRectStart[3].collidepoint(event.pos):
                    startloopLoop[2].button.play()
                    startloopLoop[2].start_sound.stop()
                    running = False

        #<--------------- Timer --------------->#
        timerinitialiser = timerinitialiser + 1
        if timerinitialiser == 1:
            before = time.time()
        game_timer = round((time.time()-before))

        #<--------------- Bullethole --------------->#
        # Append Bullethole Sprites to the list and updates them
        if spritesBulletholeAppend:
            if game_timer == 1:
                spritesBullethole.append(
                    startloopLoop[6].createAmmo(coordinates[0], "bullethole1"))
                # startloopLoop[2].shot_sound.play()
            if game_timer == 2:
                spritesBullethole.append(
                    startloopLoop[6].createAmmo(coordinates[1], "bullethole1"))
                # startloopLoop[2].shot_sound.play()
                spritesChickenHoleOut = True

            if game_timer == 3:
                spritesBullethole.append(
                    startloopLoop[6].createAmmo(coordinates[2], "bullethole1"))
                # startloopLoop[2].shot_sound.play()

            if game_timer == 4:
                spritesBullethole.append(
                    startloopLoop[6].createAmmo(coordinates[3], "bullethole1"))
                # startloopLoop[2].shot_sound.play()
                spritesBulletholeAppend = False

        # Update Bullethole
        for spriteBullethole in spritesBullethole:
            spriteBullethole.updateAmmo()

        #<--------------- Chickenhole --------------->#
        # Append Leaves Sprites to the list
        if spritesChickenHoleCreated:
            spritesChickenHole.append(startloopLoop[7].createChickenHole(
                (WIDTH * 0.6), 170, "Out"))
            spritesChickenHoleCreated = False

        # Update chickenhole
        if spritesChickenHoleOut:
            for spriteChickenHole in spritesChickenHole:
                spriteChickenHole.updateChickenHole(spritesEnd)

        # Render
        startloopLoop[1].fill((WHITE))
        startloopLoop[1].blit(startGameBG.image, startGameBG.rect)

        #<--------------- Render TrunkSmall --------------->#
        # loops through the signPost list and render it
        for spriteBullethole in spritesBullethole:
            startloopLoop[1].blit(spriteBullethole.getImage(),
                                  spriteBullethole.getRect())

        #<--------------- Render ChickenHole --------------->#
        # Render chickens to the screen
        for spriteChickenHole in spritesChickenHole:
            startloopLoop[1].blit(spriteChickenHole.getImage(),
                                  spriteChickenHole.getRect())

        # Render text and rects for menu
        startloopLoop[4].drawRectStart(startloopLoop[1], 4, WHITE,
                                       WIDTH * 0.5 - 100, 100, 200, 50, 5)
        startloopLoop[4].drawText(startloopLoop[1], startloopLoop[3].font_text,
                                  LOCATION, TEXT, 4, BLACK)

        # Blit the image at the rect's topleft coords.
        startloopLoop[1].blit(startloopLoop[5].CURSOR_IMG,
                              startloopLoop[5].cursor_rect)

        # Double Buffering
        pg.display.flip()
