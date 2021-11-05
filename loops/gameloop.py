import pygame as pg
import random
from pygame import font

from pygame.font import Font
from loops.endloop import endloop
from settings import *
from predator import *
from background import *
from signpost import *
import time
from fonts import *



def gameLoop(clock, ChickenFactory, screen, SignPostFactory):


    #starting timer
    starting_timer = 0
    timerinitialiser = 0

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

    # Sprite List for SignPost
    spritesSignPost = []

    # Create Buttons Object
    buttons = MenuButtons()

    # Create SignPost Object
    signPost = SignPost()

    #create font object
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

            if event.type == pg.MOUSEMOTION:
                # If the mouse is moved, set the center of the rect
                # to the mouse pos. You can also use pg.mouse.get_pos()
                # if you're not in the event loop.
                cursor_rect.center = event.pos

            # If a chicken got hit by mouse it will be removed
            if event.type == pg.MOUSEBUTTONDOWN:

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

                # Checks for ending the game
                if count < 5:
                    mousex, mousey = event.pos
                    # print("Maus-Pos", mousex, mousey)
                    for sprite in sprites:
                        if sprite.checkHit(mousex, mousey) and not TrunkBG.rect.collidepoint(event.pos) and not spritePost.rect.collidepoint(event.pos) and shoot:
                            count += 1
                            # print(sprite.getPos())
                            sprite.deadchicken()
                            # sprites.remove(sprite)
                # Else Check for ending the game
                else:
                    background_sound.stop()
                    running = False
                    return True

                # checks for hitting sign post and uses state pattern to change
                for spritePost in spritesSignPost:
                    if spritePost.checkHitSign(mousex, mousey):
                        if post == True:
                            post = False
                            signPost.endState()
                        else:
                            post = True
                            signPost.startState()

                # Else Check for ending the game
                if event.button == pg.BUTTON_RIGHT:
                    # Reset ammo count and play reload sound
                    bullets_count = 10
                    reload_sound.play()

            # Ends the game on ESC
            if event.type == pg.KEYDOWN:
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
                (1.12*WIDTH), random.uniform((0.1*HEIGHT), (0.6*HEIGHT)), "Left"))

        # create a chicken every spawners iteration on right side of screen
        if randomizer == 2:
            sprites.append(ChickenFactory.createCoinAtPosition(
                (-0.12*WIDTH), random.uniform((0.1*HEIGHT), (0.6*HEIGHT)), "Right"))


        # Update chicken sprites
        for sprite in sprites:
            sprite.update()

        spritesSignPost.append(
            SignPostFactory.createSignPost(50, HEIGHT - 360, 50, 50))

        # Update signpost
        for spritePost in spritesSignPost:
            spritePost.updateSign(post)

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

        # initiate the timer 
        timerinitialiser = timerinitialiser + 1 
        if timerinitialiser == 1:
            before = time.time()

        # get gametime and display in top right corner
        game_timer = round((time.time()-before))
        time_string = (str(120-game_timer)+" time left")
        text = fonts.renderFont(time_string)
        screen.blit(text, (WIDTH * 0.8, 0))
        if game_timer == 5:
            background_sound.stop()
            running = False
            return True


        # render the current ammo
        shell_x = screen_width - shell_rect.width * 0.5
        shell_y = screen_height - shell_rect.height * 0.5
        for i in range(bullets_count):
            shell_rect.center = (shell_x - i * shell_rect.width, shell_y)
            screen.blit(SHELL_IMG, shell_rect)

        # Blit the image at the rect's topleft coords.
        screen.blit(CURSOR_IMG, cursor_rect)




        # Double Buffering
        pg.display.flip()
