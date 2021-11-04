import pygame as pg
import random
from factory import *
from settings import *
from predator import *
from background import *
from mapcamera import *


def gameLoop(clock, ChickenFactory, screen, SignPostFactory):

    # Choose random map
    int = random.randint(0, 1)
    world = [background1, background2]

    # Cache screen size
    screen_width = screen.get_width()
    screen_height = screen.get_height()

    count = 0
    # Current ammo count
    bullets_count = 10

    # Sprite list for chicken
    sprites = []

    # Sprite SignPost
    spritesSignPost = []

    # Create Buttons Object
    buttons = MenuButtons()

    # Render
    font_text = pg.font.Font("freesansbold.ttf", 24)

    # Ambient sound
    background_sound = pg.mixer.Sound("sounds/background.mp3")
    background_sound.play(-1)

    # Gun sounds
    shot_sound = pg.mixer.Sound("sounds/schiessen.mp3")
    empty_sound = pg.mixer.Sound("sounds/empty.mp3")
    reload_sound = pg.mixer.Sound("sounds/reload.mp3")

    # GameLoop running?
    running = True

    while running:
        # Delta Time
        dt = clock.tick(FPS)

        # Events
        for event in pg.event.get():
            if event.type == pg.QUIT:
                background_sound.stop()
                running = False

            elif event.type == pg.MOUSEMOTION:
                # If the mouse is moved, set the center of the rect
                # to the mouse pos. You can also use pg.mouse.get_pos()
                # if you're not in the event loop.
                cursor_rect.center = event.pos

        # If a chicken got hit by mouse it will be removed
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == pg.BUTTON_RIGHT:
                    # Reset ammo count and play reload sound
                    bullets_count = 10
                    reload_sound.play()
                else:
                    # Play shot sound if enough ammo or empty sound
                    if bullets_count <= 0:
                        empty_sound.play()
                    else:
                        shot_sound.play()
                        bullets_count = bullets_count - 1
                        # Checks for ending the game
                        if count < 5:
                            mousex, mousey = event.pos
                            # print("Maus-Pos", mousex, mousey)
                            for sprite in sprites:
                                if sprite.checkHit(mousex, mousey):
                                    count += 1
                                    # print(sprite.getPos())
                                    sprite.deadchicken()
                                    # sprites.remove(sprite)
                        # Else Check for ending the game
                        else:
                            background_sound.stop()
                            running = False
                            return True

            # Ends the game on ESC
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    background_sound.stop()
                    running = False
                if event.key == pg.K_SPACE:
                    # Reset ammo count and play reload sound
                    bullets_count = 10
                    reload_sound.play()

        # create a chicken every spawners iteration on right side of screen
        randomizer = random.randrange(1, SPAWNER, 1)
        if randomizer == 1:
            sprites.append(ChickenFactory.createCoinAtPosition(
                (1.12*WIDTH), random.uniform((0.1*HEIGHT), (0.9*HEIGHT)), "Left"))

        if randomizer == 2:
            sprites.append(ChickenFactory.createCoinAtPosition(
                (-0.12*WIDTH), random.uniform((0.1*HEIGHT), (0.9*HEIGHT)), "Right"))

        # Update chicken sprites
        for sprite in sprites:
            sprite.update()

        spritesSignPost.append(
            SignPostFactory.createSignPost(50, 50, 100, 50))

        # Update signpost
        for spritePost in spritesSignPost:
            spritePost.update()

        # Render background image and color
        screen.fill((SKYBLUE))
        screen.blit(world[int].image, world[int].rect)

        # Render chickens to the screen
        for sprite in sprites:
            screen.blit(sprite.getImage(), sprite.getRect())

        # loops through the list
        screen.blit(spritePost.getImage(),
                    spritePost.getRect())

        screen.blit(TrunkBG.image, TrunkBG.rect)

        # render top menu bar
        buttons.drawRect(screen, 1, BLACK, 0, 0, WIDTH, 30, 0)
        buttons.drawText(screen, font_text, LOCATIONGAME, TEXTGAME, 1, WHITE)

        # render the current ammo
        shell_x = screen_width - shell_rect.width / 2
        shell_y = screen_height - shell_rect.height / 2
        for i in range(bullets_count):
            shell_rect.center = (shell_x - i * shell_rect.width, shell_y)
            screen.blit(SHELL_IMG, shell_rect)

        # Blit the image at the rect's topleft coords.
        screen.blit(CURSOR_IMG, cursor_rect)

        # Double Buffering
        pg.display.flip()
