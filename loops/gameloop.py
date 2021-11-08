import pygame as pg
import random
import time

from settings import *
from predator import *
from background import *
from signpost import *

# gameloopList = [clock, screen, ChickenFactory, SignPostFactory, ChickenForegroundFactory, Sounds, Fonts, MenuButtons, TreeFactory]


def gameLoop(gameloopList):

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
        ammos.append(gameloopList[10].createAmmo(ammo_x, ammo_y))

    # Sprite list for chicken
    sprites = []

    # Sprite List for SignPost and boolean
    spritesSignPost = []
    post = True

    # Sprite List for ChickenForeground
    SpritesChickenForeground = []

    # Sprite List for Trunks and boolean
    spritesTrunk = []
    spritesTrunkAppend = True

    # Create SignPost Object
    signPost = SignPost()

    # Ambient sound endless loop
    gameloopList[5].background_sound.play(-1)

    # Boolean values for stopping appending list objects
    spritesSignPostAppend = True
    spritesChickenForegroundAppend = True

    # GameLoop running?
    running = True

    # check for pumpkin shoot and sprite list
    pumpkinAppend = True
    spritesPumpkin = []

    # Can predator shoot
    shoot = True

    while running:
        # Delta Time
        dt = gameloopList[0].tick(FPS)

        chickenSound = random.randint(0, 2)

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
                    gameloopList[5].reload_sound.play()
                    if len(ammos) < 10:
                        # Reset ammo count and play reload sound
                        for i in range(len(ammos)+1, ammo_count+1):
                            ammo_x = screen_width - AMMOSIZE[0] * i
                            ammo_y = screen_height - AMMOSIZE[1]
                            ammos.append(
                                gameloopList[10].createAmmo(ammo_x, ammo_y))

            elif event.type == pg.MOUSEMOTION:
                # If the mouse is moved, set the center of the rect
                # to the mouse pos. You can also use pg.mouse.get_pos()
                # if you're not in the event loop.
                cursor_rect.center = event.pos

            # Else Check for ending the game
            elif event.type == pg.MOUSEBUTTONDOWN and event.button == RIGHT:
                gameloopList[5].reload_sound.play()
                if len(ammos) < 10:
                    # Reset ammo count and play reload sound
                    for i in range(len(ammos)+1, ammo_count+1):
                        ammo_x = screen_width - AMMOSIZE[0] * i
                        ammo_y = screen_height - AMMOSIZE[1]
                        ammos.append(
                            gameloopList[10].createAmmo(ammo_x, ammo_y))

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

                # print("Maus-Pos", mousex, mousey)
                for spritePumpkin in spritesPumpkin:
                    if spritePumpkin.checkHitPumpkin(mousex, mousey) and shoot:
                        gameloopList[5].scarecrowHit.play()
                        # print(sprite.getPos())
                        # sprite.deadchicken()
                        # sprites.remove(sprite)

                # print("Maus-Pos", mousex, mousey)
                for sprite in sprites:
                    if sprite.checkHit(mousex, mousey) and not spriteTrunk.rect.collidepoint(event.pos) and not spritePost.rect.collidepoint(event.pos) and shoot:
                        gameloopList[5].chickenDeadSound(chickenSound).play()
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
                        # chickenForeground.remove(spriteChickenForeground)
                        gameloopList[5].chickenDeadSound(chickenSound).play()
                        spriteChickenForeground.deadchicken()

                # Checks for hitting the Trunks
                for spriteTrunk in spritesTrunk:
                    if spriteTrunk.checkHitTrunk(mousex, mousey) and shoot:
                        # chickenForeground.remove(spriteChickenForeground)
                        gameloopList[5].treeHit.play()

        #<--------------- Pumpkin --------------->#
        # Append SignPost Sprites to the list
        if pumpkinAppend:
            spritesPumpkin.append(
                gameloopList[9].createPumpkin(WIDTH * 0.5, HEIGHT * 0.5))
            pumpkinAppend = False

        # Update signpost
        for spritePumpkin in spritesPumpkin:
            spritePumpkin.updatePumpkin()

        #<--------------- Chicken --------------->#
        # create a chicken every spawners iteration on right side of screen
        randomizer = random.randrange(1, SPAWNER, 1)
        if randomizer == 1:
            sprites.append(gameloopList[2].createCoinAtPosition(
                (1.12*WIDTH), random.uniform((0.1*HEIGHT), (0.6*HEIGHT)), "Left"))

        # create a chicken every spawners iteration on right side of screen
        if randomizer == 2:
            sprites.append(gameloopList[2].createCoinAtPosition(
                (-0.12*WIDTH), random.uniform((0.1*HEIGHT), (0.6*HEIGHT)), "Right"))

        # Update chicken sprites
        for sprite in sprites:
            sprite.update()
            # if sprite.isFullDead():
            #    sprites.remove(sprite)

        #   Remove all dead ammo
        for ammo in deadAmmos:
            ammo.updateAmmo()
            if ammo.isFullDead():
                try:
                    ammos.remove(ammo)
                except:
                    pass

        #<--------------- ChickenForeground --------------->#
        # Append SignPost Sprites to the list
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

        #<--------------- Trunks --------------->#
        # Append SignPost Sprites to the list
        if spritesTrunkAppend:
            spritesTrunk.append(
                gameloopList[8].createTree(WIDTH * 0.7, 0))
            spritesTrunkAppend = False

        # Update Trunk
        for spriteTrunk in spritesTrunk:
            spriteTrunk.updateTrunk()

        # #<--------------- Background --------------->#
        # # Render background image and color
        gameloopList[1].fill((SKYBLUE))
        gameloopList[1].blit(backgroundCombined.image, (startX, startY))

        #<--------------- Render Pumpkin --------------->#
        # Render pumpkin to the screen
        for spritePumpkin in spritesPumpkin:
            gameloopList[1].blit(spritePumpkin.getImage(),
                                 spritePumpkin.getRect())

        #<--------------- Render Chicken --------------->#
        # Render chickens to the screen
        for sprite in sprites:
            gameloopList[1].blit(sprite.getImage(), sprite.getRect())

        #<--------------- Render ChickenForeground --------------->#
        for spriteChickenForeground in SpritesChickenForeground:
            gameloopList[1].blit(spriteChickenForeground.getImage(),
                                 spriteChickenForeground.getRect())

        #<--------------- Render SignPost --------------->#
        # loops through the signPost list and render it
        gameloopList[1].blit(spritePost.getImage(),
                             spritePost.getRect())

        #<--------------- Render Trunk --------------->#
        # loops through the signPost list and render it
        gameloopList[1].blit(spriteTrunk.getImage(),
                             spriteTrunk.getRect())

        # Move camera
        if cursor_rect.center[0] < 50 or left == True:
            if startX >= backgroundCombined.rect[0]:
                startX += 0
            else:
                startX += 5
        if WIDTH - cursor_rect.center[0] < 50 or right == True:
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

        # render the current ammo
        for ammo in ammos:
            gameloopList[1].blit(ammo.getImage(), ammo.getRect())

        for ammo in deadAmmos:
            gameloopList[1].blit(ammo.getImage(), ammo.getRect())

        #<--------------- Render Cursor --------------->#
        # Blit the image at the rect's topleft coords.
        gameloopList[1].blit(CURSOR_IMG, cursor_rect)

        # Double Buffering
        pg.display.flip()
