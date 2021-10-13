import pygame
import random
import os

# Settings
WIDTH = 480
HEIGHT = 360
FPS = 120

# Initialization
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.SCALED)
pygame.display.set_caption("My Game")

#ball in den Speicher 
game_folder = os.path.dirname(__file__)
ballimg = pygame.image.load(os.path.join(game_folder,"handball.png")).convert_alpha()

##abprallen an den rändern

ballRect = ballimg.get_rect()


# pygame Clock
clock = pygame.time.Clock()

# GameLoop running?
running = True

#bewegung 
SPEED = 1000 /FPS

sx = SPEED
sy = SPEED
x = 240
y = 160

while running:
    # Delta Time
    dt = clock.tick(FPS)

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update

    x = x + sx
    y = y + sy

    ballRect.topleft = (x,y)

    if ballRect.bottom >= HEIGHT:
        sy = sy * -1

    if ballRect.right >= WIDTH:
        sx = sx * -1

    if ballRect.left <= 0: 
        sx = sx * -1

    if ballRect.top <= 0:
        sy = sy * -1


    # Render
    screen.fill((255, 255, 255))
    screen.blit(ballimg,ballRect)

    # Double Buffering
    pygame.display.flip()


# Done! Time to quit.
pygame.quit()
