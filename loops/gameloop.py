import pygame as pg
import random
import time
import json

from settings.settings import *
from settings.background import *

# gameloopList = [clock, screen, ChickenFactory, SignPostFactory, ChickenForegroundFactory,
#                  Sounds, Fonts, MenuButtons, TreeFactory, PumpkinFactory, PlaneFactory,
#                   LeavesFactory, ChickenHoleFactory, Predator, ammoFactory ,ObserverSubject,
#                   ChickenWindmilFactory]


def gameLoop(gameloopList):

    # def show_go_screen():
    #     draw_text (screen, "GAME OVER", 64, screen_width * 0.5, screen-height * 0.25 )
    #

    #     pg.display.flip()
    #     waiting = True
    #     while waiting:
    #         clock.tick(FPS)
    #         for event in pg.event.get():
    #             if event.type ==  pg.QUIT:
    #                 pg.quit()

    #             if event.type == pg.KEYUP:
    #                 waiting = False

    # set score to 0
    score = 0

    # Starting coordinates for map
    startX, startY = 0, 100

    # Starting movement of map
    move = 0
    left = False
    right = False

    # Mouseposition
    mouseposition = gameloopList[13].cursor_rect.center

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
        ammos.append(gameloopList[14].createAmmo((ammo_x, ammo_y), "Ammo1"))

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

    # Sprite List for planes and banners and boolean
    spritesPlane = []
    spritesBanner = []

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

    # check for chickenwindmil shoot and sprite list
    spritesWindmilAlive = True
    spritesWindmilCreate = True
    spritesWindmil = []
    windmilList = ["chickenwindmil1", "chickenwindmil10",
                   "chickenwindmil19", "chickenwindmil28"]
    index = [1, 10, 19, 28]

    # check for chickenhole shoot and sprite list
    spritesChickenHoleBooelanList = []
    spritesOut = False
    spritesEnd = False
    spritesChickenHoleOut = False
    spritesChickenHoleEnd = False
    spritesChickenHole = []
    spritesCreated = True
    spritesChickenholeCreated = True

    # Can predator shoot
    shoot = True
    normaleCursor = gameloopList[13].CURSOR_IMG
    redCursor = gameloopList[13].CURSOR_IMG_RED
    cursorColor = normaleCursor
    result = False

    # Game Over variables
    game_over = False
    game_over_text = gameloopList[6].renderFont("GAME OVER", BLACK)

    # Window should exit?
    exited = False

    while running or game_over:
        # Delta Time
        dt = gameloopList[0].tick(FPS)
        if game_over:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    gameloopList[5].background_sound.stop()
                    game_over = False
                    exited = True
                if event.type == pg.KEYDOWN:
                    # Ends the game on ESC
                    if event.key == pg.K_RETURN:
                        gameloopList[5].background_sound.stop()
                        game_over = False
                if event.type == pg.MOUSEMOTION:
                    gameloopList[13].cursor_rect.center = event.pos
                    mouseposition = gameloopList[13].cursor_rect.center
            # Render background
            gameloopList[1].fill((SKYBLUE))

            # Render Game Over label and final score
            gameloopList[1].blit(
                game_over_text, (WIDTH * 0.5 - game_over_text.get_rect().width/2, HEIGHT * 0.5 - 50))
            gameloopList[1].blit(
                points, (WIDTH * 0.5 - points.get_rect().width/2, HEIGHT * 0.5))

            # Render mouse
            if result:
                cursorColor = redCursor
            else:
                cursorColor = normaleCursor
            gameloopList[1].blit(cursorColor,
                                 gameloopList[13].cursor_rect)

            pg.display.flip()
            continue

        chickenSound = random.randint(0, 2)
        planeSound = random.randint(1, 2)

        # Events
        for event in pg.event.get():
            if event.type == pg.QUIT:
                gameloopList[5].background_sound.stop()
                running = False
                return False

            # Keys pressed
            if event.type == pg.KEYDOWN:
                # Ends the game on ESC
                if event.key == pg.K_ESCAPE:
                    # gameloopList[5].background_sound.stop()
                    running = False
                    game_over = True
                # Reload on space
                if event.key == pg.K_SPACE:
                    if len(ammos) < 10:
                        gameloopList[5].reload_sound.play()
                        # Reset ammo count and play reload sound
                        for i in range(len(ammos)+1, ammo_count+1):
                            ammo_x = screen_width - AMMOSIZE[0] * i
                            ammo_y = screen_height - AMMOSIZE[1]
                            ammos.append(
                                gameloopList[14].createAmmo((ammo_x, ammo_y), "Ammo1"))
            # move camera with arrows
                if event.key == pg.K_LEFT:
                    left = True
                if event.key == pg.K_RIGHT:
                    right = True
            elif event.type == pg.KEYUP:
                if event.key == pg.K_LEFT:
                    left = False
                if event.key == pg.K_RIGHT:
                    right = False

            elif event.type == pg.MOUSEMOTION:
                # If the mouse is moved, set the center of the rect
                # to the mouse pos. You can also use pg.mouse.get_pos()
                # if you're not in the event loop.
                gameloopList[13].cursor_rect.center = event.pos
                mouseposition = gameloopList[13].cursor_rect.center

            # Else Check for ending the game
            elif event.type == pg.MOUSEBUTTONDOWN and event.button == RIGHT:
                if len(ammos) < 10:
                    gameloopList[5].reload_sound.play()
                    for i in range(len(ammos)+1, ammo_count+1):
                        ammo_x = screen_width - AMMOSIZE[0] * i
                        ammo_y = screen_height - AMMOSIZE[1]
                        ammos.append(
                            gameloopList[14].createAmmo((ammo_x, ammo_y), "Ammo1"))

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

        #<------------------------------------------- WINDMIL ----------------------------------------------->#
                # checks for hitting chickenwindmil
                for spriteWindmil in spritesWindmil:
                    if spriteWindmil.checkHitWindmil(gameloopList[13].CURSOR_IMG_MASK, mousex, mousey) and not spritePlane.rect.collidepoint(event.pos) and not sprite.rect.collidepoint(event.pos) and shoot:
                        gameloopList[5].chickenDeadSound(chickenSound).play()
                        # spritesWindmilAlive = False

        #<---------------------------------------- CHICKENHOLE ----------------------------------------------->#
                # checks for hitting chickenhole
                for spriteChickenHole in spritesChickenHole:
                    if spriteChickenHole.checkHitChickenHole(gameloopList[13].CURSOR_IMG_MASK, mousex, mousey) and shoot and spritesOut:
                        gameloopList[5].chickenDeadSound(chickenSound).play()
                        if spritesOut:
                            spritesEnd = True
                        if spritesChickenHoleOut:
                            spritesChickenHoleEnd = True

        #<------------------------------------------- PUMPKIN ----------------------------------------------->#
                # checks for hitting pumpkin
                for spritePumpkin in spritesPumpkin:
                    if spritePumpkin.checkHitPumpkin(mousex, mousey) and not sprite.rect.collidepoint(event.pos) and not spritePlane.rect.collidepoint(event.pos) and shoot:
                        gameloopList[5].scarecrowHit.play()
                        pumpkinMove = True

        #<------------------------------------------- PLANES ----------------------------------------------->#
                # checks for hitting planes
                for spritePlane in spritesPlane:
                    if spritePlane.checkHitPlane(mousex, mousey) and not spriteTrunk.rect.collidepoint(event.pos) and not spritePost.rect.collidepoint(event.pos) and shoot:
                        gameloopList[5].planeCrash(planeSound).play()

        #<------------------------------------------ BANNERS ----------------------------------------------->#
                # checks for hitting banners
                for spriteBanner in spritesBanner:
                    if spriteBanner.checkHitPlane(mousex, mousey) and not spriteTrunk.rect.collidepoint(event.pos) and not spritePost.rect.collidepoint(event.pos) and shoot:
                        spritesBanner.remove(spriteBanner)

        #<------------------------------------------ CHICKENS ----------------------------------------------->#
                # checks for hitting chickens
                for sprite in sprites:
                    if sprite.checkHit(mousex, mousey) and not spriteTrunk.rect.collidepoint(event.pos) and not spritePost.rect.collidepoint(event.pos) and not spriteLeaves.rect.collidepoint(event.pos) and shoot:
                        gameloopList[5].chickenDeadSound(chickenSound).play()
                        score = gameloopList[15].erhoehePunkte(sprite.points)
                        sprite.deadchicken()

        #<------------------------------------------- SIGNPOST ----------------------------------------------->#
                # checks for hitting sign post and uses state pattern to change
                for spritePost in spritesSignPost:
                    if spritePost.checkHitSign(gameloopList[13].CURSOR_IMG_MASK, mousex, mousey) and shoot:
                        gameloopList[5].treeHit.play()
                        if post:
                            # post = signPost.endState()
                            post = False
                        else:
                            # post = signPost.startState()
                            post = True

        #<--------------------------------------- CHICKENFOREGROUND -------------------------------------->#
                # Checks for hitting the ChickenForeground
                for spriteChickenForeground in SpritesChickenForeground:
                    if spriteChickenForeground.checkHitChicken(mousex, mousey) and not spriteTrunk.rect.collidepoint(event.pos) and not spritePost.rect.collidepoint(event.pos) and shoot:
                        # score = gameloopList[15].erhoehePunkte(sprite.points)
                        gameloopList[5].chickenDeadSound(chickenSound).play()
                        spriteChickenForeground.deadchicken()

        #<------------------------------------------ TRUNK BIG ------------------------------------------->#
                # Checks for hitting the TrunkBig
                for spriteTrunk in spritesTrunk:
                    if spriteTrunk.checkHitTrunk(mousex, mousey) and shoot:
                        gameloopList[5].treeHit.play()
                        spritesFalling = True
                        spritesOut = True

        #<---------------------------------------- TRUNK SMALL ------------------------------------------->#
                # Checks for hitting the TrunkSmall
                for spriteTrunk in spritesTrunkSmall:
                    if spriteTrunk.checkHitTrunk(mousex, mousey) and shoot:
                        gameloopList[5].treeHit.play()
                        spritesFalling = True
                        spritesChickenHoleOut = True

                # Checks for hitting the leaves
                for spriteLeaves in spritesLeaves:
                    if spriteLeaves.checkHitLeaves(mousex, mousey) and shoot:
                        gameloopList[5].leafHit.play()
                        spriteLeaves.fallingShot()

        #<------------------------------------------- Pumpkin ------------------------------------------->#
        # Append Pumpkin Sprites to the list
        if pumpkinAppend:
            spritesPumpkin.append(
                gameloopList[9].createPumpkin(2060, HEIGHT * 0.6))
            pumpkinAppend = False

        # Update Pumpkin
        for spritePumpkin in spritesPumpkin:
            spritePumpkin.updatePumpkin(move, pumpkinMove)

        #<------------------------------------------- Plane ------------------------------------------->#
        # create a plane every spawners iteration on right side of screen
        randomizerPlane = random.randrange(1, SPAWNERPLANE, 1)
        if randomizerPlane == 1:
            height1 = random.uniform((0.1*HEIGHT), (0.6*HEIGHT))
            speed = SPEED * random.choice([-1, -1, -0.5, -0.5])
            spritesPlane.append(gameloopList[10].createPlane(
                (1.12*WIDTH), height1, "Left", "plane0", speed))
            spritesBanner.append(gameloopList[10].createPlane(
                (1.18*WIDTH), height1, "Left", "planebanner0", speed))

        # create a plane every spawners iteration on left side of screen
        if randomizerPlane == 2:
            height2 = random.uniform((0.1*HEIGHT), (0.6*HEIGHT))
            speed = SPEED * random.choice([1, 1, 0.5, 0.5])
            spritesPlane.append(gameloopList[10].createPlane(
                (-0.12*WIDTH), height2, "Right", "plane0", speed))
            spritesBanner.append(gameloopList[10].createPlane(
                (-0.18*WIDTH), height2, "Right", "planebanner0", speed))

        # Update plane
        for spritePlane in spritesPlane:
            spritePlane.updatePlane(move)

        # Update banners
        for spriteBanner in spritesBanner:
            spriteBanner.updateBanner(move)

        #<------------------------------------------- Chicken ------------------------------------------->#
        # create a chicken every spawners iteration on right side of screen
        randomizer = random.randrange(1, SPAWNER, 1)
        points = gameloopList[6].renderFont(str(score))
        if randomizer == 1:
            sprites.append(gameloopList[2].createChickenRight(
                (1.12*WIDTH), random.uniform((0.1*HEIGHT), (0.6*HEIGHT)), "Left", points))

        # create a chicken every spawners iteration on right side of screen
        if randomizer == 2:
            sprites.append(gameloopList[2].createChickenLeft(
                (-0.12*WIDTH), random.uniform((0.1*HEIGHT), (0.6*HEIGHT)), "Right", points))

        # Update chicken sprites
        for sprite in sprites:
            sprite.update(move)
            if sprite.isFullDead():
                sprites.remove(sprite)

        #<------------------------------------------- AMMO ----------------------------------------------->#
        # Update ammo list
        for ammo in deadAmmos:
            ammo.updateAmmo()
            if ammo.isFullDead():
                try:
                    ammos.remove(ammo)
                except:
                    pass

        #<------------------------------------ ChickenForeground ------------------------------------------>#
        # Append chickenForeground Sprites to the list
        if spritesChickenForegroundAppend:
            SpritesChickenForeground.append(
                gameloopList[4].createChickenForeground(random.randrange(100, 2700), HEIGHT - 300))
            spritesChickenForegroundAppend = False

        # Update chickenForeground sprites
        for spriteChickenForeground in SpritesChickenForeground:
            spriteChickenForeground.updateChicken(move)
            if spriteChickenForeground.isFullDead():
                SpritesChickenForeground.remove(spriteChickenForeground)

        #<------------------------------------------- SignPost -------------------------------------------->#
        # Append SignPost Sprites to the list
        if spritesSignPostAppend:
            spritesSignPost.append(
                gameloopList[3].createSignPost(50, HEIGHT - 310))
            spritesSignPostAppend = False

        # Update signpost
        for spritePost in spritesSignPost:
            spritePost.updateSign(post, move)

        #<------------------------------------------- TrunksBig -------------------------------------------->#
        # Append Trunks Sprites to the list
        if spritesTrunkAppend:
            spritesTrunk.append(
                gameloopList[8].createTree(WIDTH * 0.8, 0, "trunkBig1"))
            spritesTrunkAppend = False

        # Update Trunk
        for spriteTrunk in spritesTrunk:
            spriteTrunk.updateTrunk(move)

        #<------------------------------------------- TrunksSmall ------------------------------------------->#
        # Append Trunks Sprites to the list
        if spritesTrunkAppendSmall:
            spritesTrunkSmall.append(
                gameloopList[8].createTree(1500, 0, "trunkSmall1"))
            spritesTrunkAppendSmall = False

        # Update Trunk
        for spriteTrunk in spritesTrunkSmall:
            spriteTrunk.updateTrunk(move)

        #<------------------------------------------- Leaves ------------------------------------------------>#
        # Append Leaves Sprites to the list
        randomizerLeaves = random.randrange(1, SPAWNERLEAVES, 1)
        if randomizerLeaves == 1:
            spritesLeaves.append(gameloopList[11].createLeaves(
                (random.uniform(384, 864)), 0, "Down"))

        if randomizerLeaves == 2:
            spritesLeaves.append(gameloopList[11].createLeaves(
                (random.uniform(1300, 1700)), 0, "Down"))

        # Update Leaves
        for spriteLeaves in spritesLeaves:
            spriteLeaves.updateLeaves(move, spritesFalling)
            if spriteLeaves.isFullDead():
                spritesLeaves.remove(spriteLeaves)

        #<------------------------------------------- Chickenhole ------------------------------------------->#
        # Append Chickenhole Sprites to the list
        if spritesCreated:
            spritesChickenHole.append(gameloopList[12].createChickenHole(
                (WIDTH * 0.87), 270, "Out", move))
            spritesCreated = False

        if spritesChickenholeCreated:
            spritesChickenHole.append(gameloopList[12].createChickenHole(
                1515, 150, "Out2", move))
            spritesChickenholeCreated = False

        # Update Chickenhole
        for spriteChickenHole in spritesChickenHole:
            spriteChickenHole.updateChickenHole(
                move, spritesOut, spritesChickenHoleOut, spritesEnd, spritesChickenHoleEnd)

        #<------------------------------------------- chickenWindmil ---------------------------------------->#
        # Append Windmil Sprites to the list
        if spritesWindmilCreate:
            for i in range(0, 4):
                spritesWindmil.append(gameloopList[16].createChickenWindmil(
                    2380, 90, windmilList[i], index[i]))
            spritesWindmilCreate = False

        # Update Leaves
        for spriteWindmil in spritesWindmil:
            spriteWindmil.updateWindmil(spritesWindmilAlive, move)

        #<------------------------------------------- Camera ------------------------------------------------>#
        # Camera Variables
        camera = gameloopList[17](mouseposition)
        scrolling = gameloopList[18]((startX, startY), mouseposition)
        move = 0

        # #<------------------------------------------- Background ------------------------------------------->#
        # # Render background image and color

        gameloopList[1].fill((SKYBLUE))
        gameloopList[1].blit(backgroundCombined.image,
                             (scrolling.offset[0], scrolling.offset[1]))

        #<------------------------------------------- Render chickenWindmil ----------------------------------->#
        # Render chickens to the screen
        for spriteWindmil in spritesWindmil:
            gameloopList[1].blit(spriteWindmil.getImage(),
                                 spriteWindmil.getRect())

        #<------------------------------------------- Render Pumpkin ------------------------------------------>#
        # Render pumpkin to the screen
        for spritePumpkin in spritesPumpkin:
            gameloopList[1].blit(spritePumpkin.getImage(),
                                 spritePumpkin.getRect())

        #<------------------------------------------- Render Plane -------------------------------------------->#
        # Render pumpkin to the screen
        for spritePlane in spritesPlane:
            gameloopList[1].blit(spritePlane.getImage(),
                                 spritePlane.getRect())

        #<------------------------------------------- Render Banner -------------------------------------------->#
        # Render pumpkin to the screen
        for spriteBanner in spritesBanner:
            gameloopList[1].blit(spriteBanner.getImage(),
                                 spriteBanner.getRect())

        #<------------------------------------------- Render Chicken ------------------------------------------->#
        # Render chickens to the screen
        for sprite in sprites:
            gameloopList[1].blit(sprite.getImage(), sprite.getRect())

        #<------------------------------------------- Render TrunkBig ------------------------------------------->#
        # loops through the signPost list and render it
        for spriteTrunk in spritesTrunk:
            gameloopList[1].blit(spriteTrunk.getImage(),
                                 spriteTrunk.getRect())

        #<------------------------------------------- Render TrunkSmall ----------------------------------------->#
        # loops through the signPost list and render it
        for spriteTrunk in spritesTrunkSmall:
            gameloopList[1].blit(spriteTrunk.getImage(),
                                 spriteTrunk.getRect())

        #<------------------------------------------- Render SignPost ------------------------------------------->#
        # loops through the signPost list and render it
        gameloopList[1].blit(spritePost.getImage(),
                             spritePost.getRect())

        #<------------------------------------------- Render ChickenHole ---------------------------------------->#
        # Render chickens to the screen
        for spriteChickenHole in spritesChickenHole:
            gameloopList[1].blit(spriteChickenHole.getImage(),
                                 spriteChickenHole.getRect())

        #<------------------------------------------- Render Leaves --------------------------------------------->#
        # Render chickens to the screen
        for spriteLeaves in spritesLeaves:
            gameloopList[1].blit(spriteLeaves.getImage(),
                                 spriteLeaves.getRect())

        #<------------------------------------------- Render ChickenForeground ---------------------------------->#
        for spriteChickenForeground in SpritesChickenForeground:
            gameloopList[1].blit(spriteChickenForeground.getImage(),
                                 spriteChickenForeground.getRect())

        #<------------------------------------------- Map scroll ------------------------------------------------>#
        # Move camera
        if gameloopList[13].cursor_rect.center[0] < 50 or left:
            if startX >= backgroundCombined.rect[0]:
                startX += 0
            else:
                move = 5
                startX += move
        if WIDTH - gameloopList[13].cursor_rect.center[0] < 50 or right:
            if startX - WIDTH <= -backgroundCombined.rect[2] + 50:
                startX -= 0
            else:
                move = -5
                startX += move
        scrolling = gameloopList[18]((startX, startY), mouseposition)
        camera.setmethod(scrolling)
        camera.scroll()
        #<------------------------------------------- Render MenuBar ------------------------------------------->#
        # render top menu bar
        gameloopList[7].drawRectGame(
            gameloopList[1], 1, BLACK, 0, 0, WIDTH, 30, 0)
        gameloopList[7].drawText(gameloopList[1], gameloopList[6].font_text,
                                 LOCATIONGAME, TEXTGAME, 1, WHITE)

        #<------------------------------------------- TIMER ----------------------------------------------->#
        # initiate the timer
        timerinitialiser = timerinitialiser + 1
        if timerinitialiser == 1:
            before = time.time()

        # get gametime and display in top right corner
        game_timer = round((time.time()-before))
        time_string = (str(120-game_timer)+" time left")
        text = gameloopList[6].renderFont(time_string)
        gameloopList[1].blit(text, (WIDTH * 0.8, 0))
        if game_timer == 120:
            # gameloopList[5].background_sound.stop()
            running = False
            game_over = True
            # return True

        # render points
        gameloopList[1].blit(points, (WIDTH * 0.1, 0))

        #<------------------------------------------- RENDER AMMO ----------------------------------------------->#
        # render the current ammo
        for ammo in ammos:
            gameloopList[1].blit(ammo.getImage(), ammo.getRect())
        for ammo in deadAmmos:
            gameloopList[1].blit(ammo.getImage(), ammo.getRect())

        #<------------------------------------------- Render Cursor ------------------------------------------->#
        # Blit the image at the rect's topleft coords.
        if result:
            cursorColor = redCursor
        else:
            cursorColor = normaleCursor
        gameloopList[1].blit(cursorColor,
                             gameloopList[13].cursor_rect)

        # Double Buffering
        pg.display.flip()

    # Save Score
    data = {"highscores": []}
    try:
        with open("highscore\highscore.json", "r+") as f:
            data = json.load(f)
    except Exception as e:
        pass
    try:
        with open("highscore\highscore.json", "w+") as f:
            data["highscores"].append({"value": score})
            data["highscores"] = sorted(
                data["highscores"], key=lambda score: score["value"], reverse=True)[:6]
            json.dump(data, f, indent=4)
    except Exception as e:
        pass


# Game Over

    return not exited
