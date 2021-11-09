import pygame as pg
import random
import time

from settings.settings import *
from settings.background import *

# gameloopList = [clock, screen, ChickenFactory, SignPostFactory, ChickenForegroundFactory,
#                  Sounds, Fonts, MenuButtons, TreeFactory, PumpkinFactory, PlaneFactory,
#                   LeavesFactory, ChickenHoleFactory, Predator, ammoFactory ,points]


def gameLoop(gameloopList):
    #set score to 0
    score = 0

    # Starting coordinates for map
    startX, startY = 0, 100

    # Key scroll parameters
    right = False
    left = False
    keypressed = pg.key.get_pressed()
    # starting timer
    # starting_timer = 0
    timerinitialiser = 0

    # Cache screen size
    screen_width = gameloopList[1].get_width()
    screen_height = gameloopList[1].get_height()

    # Current ammo count
    ammo_count = 10
    ammos = []
    deadAmmos = []
    for i in range(1, ammo_count+1):
        ammo_x = screen_width - AMMOSIZE[0] * i
        ammo_y = screen_height - AMMOSIZE[1]
        ammos.append(gameloopList[14].createAmmo(ammo_x, ammo_y))

    # Sprite list for chicken
    sprites = []

    # Sprite List for SignPost and boolean
    spritesSignPost = []
    post = True

    # Sprite List for ChickenForeground
    SpritesChickenForeground = []

    # Sprite List for Trunks and boolean
    spritesTrunk = []
    spritesTrunkSmall = []
    spritesTrunkAppend = True
    spritesTrunkAppendSmall = True

    # Sprite List for Trunks and boolean
    spritesPlane = []

    # Ambient sound endless loop
    gameloopList[5].background_sound.play(-1)

    # Boolean values for stopping appending list objects
    spritesSignPostAppend = True
    spritesChickenForegroundAppend = True

    # GameLoop running?
    running = True

    # check for pumpkin shoot and sprite list
    pumpkinAppend = True
    pumpkinMove = False
    spritesPumpkin = []

    # check for leaves shoot and sprite list
    spritesFalling = False
    spritesLeaves = []

    # check for chickenhole shoot and sprite list
    spritesOut = False
    spritesChickenHole = []
    spritesCreated = True

    # Can predator shoot
    shoot = True

    while running:
        # Delta Time
        dt = gameloopList[0].tick(FPS)

        chickenSound = random.randint(0, 2)
        planeSound = random.randint(1, 2)

        # Events
        for event in pg.event.get():
            if event.type == pg.QUIT:
                gameloopList[5].background_sound.stop()
                running = False

            # Ends the game on ESC
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    gameloopList[5].background_sound.stop()
                    running = False
                if event.key == pg.K_SPACE:
                    if len(ammos) < 10:
                        gameloopList[5].reload_sound.play()
                        # Reset ammo count and play reload sound
                        for i in range(len(ammos)+1, ammo_count+1):
                            ammo_x = screen_width - AMMOSIZE[0] * i
                            ammo_y = screen_height - AMMOSIZE[1]
                            ammos.append(
                                gameloopList[14].createAmmo(ammo_x, ammo_y))

            elif event.type == pg.MOUSEMOTION:
                # If the mouse is moved, set the center of the rect
                # to the mouse pos. You can also use pg.mouse.get_pos()
                # if you're not in the event loop.
                gameloopList[13].cursor_rect.center = event.pos

            # Else Check for ending the game
            elif event.type == pg.MOUSEBUTTONDOWN and event.button == RIGHT:
                if len(ammos) < 10:
                    gameloopList[5].reload_sound.play()
                    for i in range(len(ammos)+1, ammo_count+1):
                        ammo_x = screen_width - AMMOSIZE[0] * i
                        ammo_y = screen_height - AMMOSIZE[1]
                        ammos.append(
                            gameloopList[14].createAmmo(ammo_x, ammo_y))

            # If a chicken got hit by mouse it will be removed
            elif event.type == pg.MOUSEBUTTONDOWN and event.button == LEFT:
                # Play shot sound
                if len(ammos) >= 1:
                    ammo = ammos[-1]
                    ammo.deadAmmo()
                    ammos.remove(ammo)
                    deadAmmos.append(ammo)
                    gameloopList[5].shot_sound.play()
                    shoot = True
                # Play shot sound if enough ammo or empty sound
                else:
                    gameloopList[5].empty_sound.play()
                    shoot = False

                # Mouse position
                mousex, mousey = event.pos

                # checks for hitting chickenhole
                for spriteChickenHole in spritesChickenHole:
                    if spriteChickenHole.checkHitChickenHole(mousex, mousey) and shoot and spritesOut:
                        gameloopList[5].chickenDeadSound(chickenSound).play()
                        # spritesOut = False
                        # print(sprite.getPos())
                        # sprite.deadchicken()
                        spritesChickenHole.remove(spriteChickenHole)

                # checks for hitting pumpkin
                for spritePumpkin in spritesPumpkin:
                    if spritePumpkin.checkHitPumpkin(mousex, mousey) and shoot:
                        gameloopList[5].scarecrowHit.play()
                        pumpkinMove = True
                        # sprites.remove(sprite)

                # checks for hitting planes
                for spritePlane in spritesPlane:
                    if spritePlane.checkHitPlane(mousex, mousey) and not spriteTrunk.rect.collidepoint(event.pos) and not spritePost.rect.collidepoint(event.pos) and shoot:
                        gameloopList[5].planeCrash(planeSound).play()
                        spritesPlane.remove(spritePlane)

                # checks for hitting chickens
                for sprite in sprites:
                    if sprite.checkHit(mousex, mousey) and not spriteTrunk.rect.collidepoint(event.pos) and not spritePost.rect.collidepoint(event.pos) and shoot:
                        gameloopList[5].chickenDeadSound(chickenSound).play()
                        score = gameloopList[15].erhoehePunkte(sprite.points)
                        # print(sprite.getPos())
                        sprite.deadchicken()
                        # sprites.remove(sprite)

                # checks for hitting sign post and uses state pattern to change
                for spritePost in spritesSignPost:
                    if spritePost.checkHitSign(mousex, mousey) and shoot:
                        gameloopList[5].treeHit.play()
                        if post:
                            # post = signPost.endState()
                            post = False
                        else:
                            # post = signPost.startState()
                            post = True

                # Checks for hitting the ChickenForeground
                for spriteChickenForeground in SpritesChickenForeground:
                    if spriteChickenForeground.checkHitChicken(mousex, mousey) and not spriteTrunk.rect.collidepoint(event.pos) and not spritePost.rect.collidepoint(event.pos) and shoot:
                        score = gameloopList[15].erhoehePunkte(sprite.points)
                        # chickenForeground.remove(spriteChickenForeground)
                        gameloopList[5].chickenDeadSound(chickenSound).play()
                        spriteChickenForeground.deadchicken()
                        
                        # gameloopList[13].aliveState("huhu")

                # Checks for hitting the TrunkBig
                for spriteTrunk in spritesTrunk:
                    if spriteTrunk.checkHitTrunk(mousex, mousey) and shoot:
                        # chickenForeground.remove(spriteChickenForeground)
                        gameloopList[5].treeHit.play()
                        spritesFalling = True
                        spritesOut = True

                # Checks for hitting the TrunkSmall
                for spriteTrunk in spritesTrunkSmall:
                    if spriteTrunk.checkHitTrunk(mousex, mousey) and shoot:
                        # chickenForeground.remove(spriteChickenForeground)
                        gameloopList[5].treeHit.play()
                        # spritesFalling = True
                        # spritesOut = True

                # Checks for hitting the leaves
                for spriteLeaves in spritesLeaves:
                    if spriteLeaves.checkHitLeaves(mousex, mousey) and shoot:
                        # chickenForeground.remove(spriteChickenForeground)
                        gameloopList[5].leafHit.play()
                        spritesFalling = True

        #<--------------- Pumpkin --------------->#
        # Append Pumpkin Sprites to the list
        if pumpkinAppend:
            spritesPumpkin.append(
                gameloopList[9].createPumpkin(WIDTH * 0.7, HEIGHT * 0.5))
            pumpkinAppend = False

        # Update Pumpkin
        if pumpkinMove:
            for spritePumpkin in spritesPumpkin:
                spritePumpkin.updatePumpkin()

        #<--------------- Plane --------------->#
        # create a plane every spawners iteration on right side of screen
        randomizerPlane = random.randrange(1, SPAWNERPLANE, 1)
        if randomizerPlane == 1:
            spritesPlane.append(gameloopList[10].createPlane(
                (1.12*WIDTH), random.uniform((0.1*HEIGHT), (0.6*HEIGHT)), "Left"))

        # create a plane every spawners iteration on right side of screen
        if randomizerPlane == 2:
            spritesPlane.append(gameloopList[10].createPlane(
                (-0.12*WIDTH), random.uniform((0.1*HEIGHT), (0.6*HEIGHT)), "Right"))

        # Update plane
        for spritePlane in spritesPlane:
            spritePlane.updatePlane()

        #<--------------- Chicken --------------->#
        # create a chicken every spawners iteration on right side of screen
        randomizer = random.randrange(1, SPAWNER, 1)
        points = gameloopList[6].renderFont(str(score))
        if randomizer == 1:
            sprites.append(gameloopList[2].createChicken(
                (1.12*WIDTH), random.uniform((0.1*HEIGHT), (0.6*HEIGHT)), "Left", points))

        # create a chicken every spawners iteration on right side of screen
        if randomizer == 2:
            sprites.append(gameloopList[2].createChicken(
                (-0.12*WIDTH), random.uniform((0.1*HEIGHT), (0.6*HEIGHT)), "Right",points))

        # Update chicken sprites
        for sprite in sprites:
            sprite.update()
            # if sprite.isFullDead():
            #    sprites.remove(sprite)

        for ammo in deadAmmos:  # --------------------------------
            ammo.updateAmmo()  # --------------------------------
            if ammo.isFullDead():  # --------------------------------
                try:  # --------------------------------
                    ammos.remove(ammo)  # --------------------------------
                except:  # --------------------------------
                    pass  # --------------------------------

        #<--------------- ChickenForeground --------------->#
        # Append chickenForeground Sprites to the list
        if spritesChickenForegroundAppend:
            SpritesChickenForeground.append(
                gameloopList[4].createChickenForeground(WIDTH * 0.3, HEIGHT - 360))
            spritesChickenForegroundAppend = False

        # Update chickenForeground sprites
        for spriteChickenForeground in SpritesChickenForeground:
            spriteChickenForeground.updateChicken()

        #<--------------- SignPost --------------->#
        # Append SignPost Sprites to the list
        if spritesSignPostAppend:
            spritesSignPost.append(
                gameloopList[3].createSignPost(50, HEIGHT - 310))
            spritesSignPostAppend = False

        # Update signpost
        for spritePost in spritesSignPost:
            spritePost.updateSign(post)

        #<--------------- TrunksBig --------------->#
        # Append Trunks Sprites to the list
        if spritesTrunkAppend:
            spritesTrunk.append(
                gameloopList[8].createTree(WIDTH * 0.8, 0, "trunkBig1"))
            spritesTrunkAppend = False

        # Update Trunk
        for spriteTrunk in spritesTrunk:
            spriteTrunk.updateTrunk()

        #<--------------- TrunksSmall --------------->#
        # Append Trunks Sprites to the list
        if spritesTrunkAppendSmall:
            spritesTrunkSmall.append(
                gameloopList[8].createTree(WIDTH * 0.1, 0, "trunkSmall1"))
            spritesTrunkAppendSmall = False

        # Update Trunk
        for spriteTrunk in spritesTrunkSmall:
            spriteTrunk.updateTrunk()

        #<--------------- Leaves --------------->#
        # Append Leaves Sprites to the list
        randomizerLeaves = random.randrange(1, SPAWNERLEAVES, 1)
        if randomizerLeaves == 1:
            spritesLeaves.append(gameloopList[11].createLeaves(
                (WIDTH * random.uniform(0.4, 0.9)), 0, "Down"))

        # Update Leaves
        if spritesFalling:
            for spriteLeaves in spritesLeaves:
                spriteLeaves.updateLeaves()

        #<--------------- Chickenhole --------------->#
        # Append Leaves Sprites to the list
        if spritesCreated:
            spritesChickenHole.append(gameloopList[12].createChickenHole(
                (WIDTH * 0.9), 200, "Out"))
            spritesCreated = False

        # Update Leaves
        if spritesOut:
            for spriteChickenHole in spritesChickenHole:
                spriteChickenHole.updateChickenHole()

        # #<--------------- Background --------------->#
        # # Render background image and color
        gameloopList[1].fill((SKYBLUE))
        gameloopList[1].blit(backgroundCombined.image, (startX, startY))

        #<--------------- Render Pumpkin --------------->#
        # Render pumpkin to the screen
        for spritePumpkin in spritesPumpkin:
            gameloopList[1].blit(spritePumpkin.getImage(),
                                 spritePumpkin.getRect())

        #<--------------- Render Plane --------------->#
        # Render pumpkin to the screen
        for spritePlane in spritesPlane:
            gameloopList[1].blit(spritePlane.getImage(),
                                 spritePlane.getRect())

        #<--------------- Render Chicken --------------->#
        # Render chickens to the screen
        for sprite in sprites:
            gameloopList[1].blit(sprite.getImage(), sprite.getRect())

        #<--------------- Render TrunkBig --------------->#
        # loops through the signPost list and render it
        for spriteTrunk in spritesTrunk:
            gameloopList[1].blit(spriteTrunk.getImage(),
                                 spriteTrunk.getRect())

        #<--------------- Render TrunkSmall --------------->#
        # loops through the signPost list and render it
        for spriteTrunk in spritesTrunkSmall:
            gameloopList[1].blit(spriteTrunk.getImage(),
                                 spriteTrunk.getRect())

        #<--------------- Render SignPost --------------->#
        # loops through the signPost list and render it
        gameloopList[1].blit(spritePost.getImage(),
                             spritePost.getRect())

        #<--------------- Render ChickenHole --------------->#
        # Render chickens to the screen
        for spriteChickenHole in spritesChickenHole:
            gameloopList[1].blit(spriteChickenHole.getImage(),
                                 spriteChickenHole.getRect())

        #<--------------- Render Leaves --------------->#
        # Render chickens to the screen
        for spriteLeaves in spritesLeaves:
            gameloopList[1].blit(spriteLeaves.getImage(),
                                 spriteLeaves.getRect())

        #<--------------- Render ChickenForeground --------------->#
        for spriteChickenForeground in SpritesChickenForeground:
            gameloopList[1].blit(spriteChickenForeground.getImage(),
                                 spriteChickenForeground.getRect())

        #<--------------- Map scroll --------------->#
        # Move camera
        if gameloopList[13].cursor_rect.center[0] < 50 or left:
            if startX >= backgroundCombined.rect[0]:
                startX += 0
            else:
                startX += 5
        if WIDTH - gameloopList[13].cursor_rect.center[0] < 50 or right:
            if startX - WIDTH <= -backgroundCombined.rect[2] + 50:
                startX -= 0
            else:
                startX -= 5

        #<--------------- Render MenuBar --------------->#
        # render top menu bar
        gameloopList[7].drawRectGame(
            gameloopList[1], 1, BLACK, 0, 0, WIDTH, 30, 0)
        gameloopList[7].drawText(gameloopList[1], gameloopList[6].font_text,
                                 LOCATIONGAME, TEXTGAME, 1, WHITE)

        # initiate the timer
        timerinitialiser = timerinitialiser + 1
        if timerinitialiser == 1:
            before = time.time()

        # get gametime and display in top right corner
        game_timer = round((time.time()-before))
        time_string = (str(120-game_timer)+" time left")
        text = gameloopList[6].renderFont(time_string)
        gameloopList[1].blit(text, (WIDTH * 0.8, 0))
        if game_timer == 20:
            gameloopList[5].background_sound.stop()
            running = False
            return True

        
        # render points
        gameloopList[1].blit(points, (WIDTH * 0.1, 0))

        # render the current ammo
        for ammo in ammos:
            gameloopList[1].blit(ammo.getImage(), ammo.getRect())
        for ammo in deadAmmos:
            gameloopList[1].blit(ammo.getImage(), ammo.getRect())

        #<--------------- Render Cursor --------------->#
        # Blit the image at the rect's topleft coords.
        gameloopList[1].blit(gameloopList[13].CURSOR_IMG,
                             gameloopList[13].cursor_rect)

        # Double Buffering
        pg.display.flip()
