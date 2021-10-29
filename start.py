import pygame
import random
from factory import *
from settings import *
from predator import *
from background import *

# Initialization
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.SCALED)
pygame.display.set_caption("Morhuhn Extreme")

# create object
sprites = []
ChickenFactory = ChickenFactory()

# pygame Clock
clock = pygame.time.Clock()


def main():

    # GameLoop running?
    running = True

    while running:
        # Delta Time
        dt = clock.tick(FPS)

        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pg.MOUSEMOTION:
                # If the mouse is moved, set the center of the rect
                # to the mouse pos. You can also use pygame.mouse.get_pos()
                # if you're not in the event loop.
                cursor_rect.center = event.pos

        # If a chicken got hit by mouse it will be removed
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousex, mousey = event.pos
                print("Maus-Pos", mousex, mousey)
                for sprite in sprites:
                    if sprite.checkHit(mousex, mousey):
                        print(sprite.getPos())
                        sprites.remove(sprite)

        # create a chicken every spawners iteration on right side of screen
        randomizer = random.randrange(1, SPAWNER, 1)
        if randomizer == 1:
            sprites.append(ChickenFactory.createCoinAtPosition(
                WIDTH-(0.12*WIDTH), random.uniform((0.1*HEIGHT), (0.9*HEIGHT)), "Left"))

        # Update
        for sprite in sprites:
            sprite.update()

        # Render
        screen.fill((WHITE))
        screen.blit(background.image, background.rect)

        for sprite in sprites:
            screen.blit(sprite.getImage(), sprite.getRect())
        # Blit the image at the rect's topleft coords.
        screen.blit(CURSOR_IMG, cursor_rect)

        # Double Buffering
        pygame.display.flip()


# Start main
main()

# Done! Time to quit.
pygame.quit()
