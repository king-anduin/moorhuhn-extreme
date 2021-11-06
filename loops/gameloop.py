import pygame as pg
import random
import time

from settings import *
from predator import *
from background import *
from signpost import *
from fonts import *


def gameLoop(clock, ChickenFactory, screen, SignPostFactory, ChickenForegroundFactory):

    # starting timer
    # starting_timer = 0
    timerinitialiser = 0

    # Choose random map
    int = random.randint(0, 1)
    world = [background1, background2]

    # Cache screen size
    screen_width = screen.get_width()
    screen_height = screen.get_height()

    # Current ammo count
    bullets_count = 10

    # Sprite list for chicken
    sprites = []

    # Sprite List for SignPost
    spritesSignPost = []

    # Sprite List for ChickenForeground
    chickenForeground = []

    # Create Buttons Object
    buttons = MenuButtons()

    # Create SignPost Object
    signPost = SignPost()

    # create font object
    fonts = Fonts(24)

    # Render

    font_text = fonts.font_text

    # Ambient sound
    background_sound = pg.mixer.Sound("sounds/background.mp3")
    background_sound.play(-1)

    # Gun sounds
    shot_sound = pg.mixer.Sound("sounds/schiessen.mp3")
    empty_sound = pg.mixer.Sound("sounds/empty.mp3")
    reload_sound = pg.mixer.Sound("sounds/reload.mp3")

    # Boolean values for stopping appending list objects
    spritesSignPostAppend = True
    spritesChickenForegroundAppend = True

    # GameLoop running?
    running = True

    # check signPost when shooting
    post = True

    # Can predator shoot
    shoot = True

    while running:
        # Delta Time
        dt = clock.tick(FPS)

        # Events
        for event in pg.event.get():
            if event.type == pg.QUIT:
                background_sound.stop()
                running = False

            # Ends the game on ESC
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    background_sound.stop()
                    running = False
                if event.key == pg.K_SPACE:
                    # Reset ammo count and play reload sound
                    bullets_count = 10
                    reload_sound.play()

            elif event.type == pg.MOUSEMOTION:
                # If the mouse is moved, set the center of the rect
                # to the mouse pos. You can also use pg.mouse.get_pos()
                # if you're not in the event loop.
                cursor_rect.center = event.pos

            # Else Check for ending the game
            elif event.type == pg.MOUSEBUTTONDOWN and event.button == RIGHT:
                # Reset ammo count and play reload sound
                bullets_count = 10
                reload_sound.play()

            # If a chicken got hit by mouse it will be removed
            elif event.type == pg.MOUSEBUTTONDOWN and event.button == LEFT:
                # Play shot sound
                if bullets_count >= 1:
                    shot_sound.play()
                    shoot = True
                # Play shot sound if enough ammo or empty sound
                else:
                    empty_sound.play()
                    shoot = False

                # minus one bullet
                bullets_count -= 1

                # Mouse position
                mousex, mousey = event.pos

                # print("Maus-Pos", mousex, mousey)
                for sprite in sprites:
                    if sprite.checkHit(mousex, mousey) and not TrunkBG.rect.collidepoint(event.pos) and not spritePost.rect.collidepoint(event.pos) and shoot:
                        # print(sprite.getPos())
                        sprite.deadchicken()
                        # sprites.remove(sprite)

                # checks for hitting sign post and uses state pattern to change
                for spritePost in spritesSignPost:
                    if spritePost.checkHitSign(mousex, mousey) and shoot:
                        if post:
                            # post = signPost.endState()
                            post = False
                        else:
                            # post = signPost.startState()
                            post = True

                for spriteChickenForeground in chickenForeground:
                    if spriteChickenForeground.checkHitChicken(mousex, mousey) and not TrunkBG.rect.collidepoint(event.pos) and not spritePost.rect.collidepoint(event.pos) and shoot:
                        # print(sprite.getPos())
                        # sprite.deadchicken()
                        # sprites.remove(sprite)
                        pass

        #<--------------- Chicken --------------->#
        # create a chicken every spawners iteration on right side of screen
        randomizer = random.randrange(1, SPAWNER, 1)
        if randomizer == 1:
            sprites.append(ChickenFactory.createCoinAtPosition(
                (1.12*WIDTH), random.uniform((0.1*HEIGHT), (0.6*HEIGHT)), "Left"))

        # create a chicken every spawners iteration on right side of screen
        if randomizer == 2:
            sprites.append(ChickenFactory.createCoinAtPosition(
                (-0.12*WIDTH), random.uniform((0.1*HEIGHT), (0.6*HEIGHT)), "Right"))

        # Update chicken sprites
        for sprite in sprites:
            sprite.update()

        #<--------------- ChickenForeground --------------->#
        # Append SignPost Sprites to the list
        if spritesChickenForegroundAppend:
            chickenForeground.append(
                ChickenForegroundFactory.createChickenForeground(WIDTH * 0.3, HEIGHT - 360))
            spritesChickenForegroundAppend = False

        # Update chickenForeground sprites
        for spriteChickenForeground in chickenForeground:
            spriteChickenForeground.updateChicken()

        #<--------------- SignPost --------------->#
        # Append SignPost Sprites to the list
        if spritesSignPostAppend:
            spritesSignPost.append(
                SignPostFactory.createSignPost(50, HEIGHT - 310))
            spritesSignPostAppend = False

        # # Update signpost
        for spritePost in spritesSignPost:
            spritePost.updateSign(post)

        #<--------------- Background --------------->#
        # Render background image and color
        screen.fill((SKYBLUE))
        screen.blit(world[int].image, world[int].rect)

        #<--------------- Render Chicken --------------->#
        # Render chickens to the screen
        for sprite in sprites:
            screen.blit(sprite.getImage(), sprite.getRect())

        #<--------------- Render ChickenForeground --------------->#
        for spriteChickenForeground in chickenForeground:
            screen.blit(spriteChickenForeground.getImage(),
                        spriteChickenForeground.getRect())

        #<--------------- Render SignPost --------------->#
        # loops through the signPost list and render it
        screen.blit(spritePost.getImage(),
                    spritePost.getRect())

        #<--------------- Render Trunk --------------->#
        screen.blit(TrunkBG.image, TrunkBG.rect)

        #<--------------- Render MenuBar --------------->#
        # render top menu bar
        buttons.drawRect(screen, 1, BLACK, 0, 0, WIDTH, 30, 0)
        buttons.drawText(screen, font_text, LOCATIONGAME, TEXTGAME, 1, WHITE)

        # initiate the timer
        timerinitialiser = timerinitialiser + 1
        if timerinitialiser == 1:
            before = time.time()

        # get gametime and display in top right corner
        game_timer = round((time.time()-before))
        time_string = (str(120-game_timer)+" time left")
        text = fonts.renderFont(time_string)
        screen.blit(text, (WIDTH * 0.8, 0))
        if game_timer == 25:
            background_sound.stop()
            running = False
            return True

        # render the current ammo
        shell_x = screen_width - shell_rect.width * 0.5
        shell_y = screen_height - shell_rect.height * 0.5
        for i in range(bullets_count):
            shell_rect.center = (shell_x - i * shell_rect.width, shell_y)
            screen.blit(SHELL_IMG, shell_rect)

        #<--------------- Render Cursor --------------->#
        # Blit the image at the rect's topleft coords.
        screen.blit(CURSOR_IMG, cursor_rect)

        # Double Buffering
        pg.display.flip()
