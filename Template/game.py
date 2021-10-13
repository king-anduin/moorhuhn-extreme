import pygame
import random
import os
from factory import *
from settings import *

# Initialization
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.SCALED)
pygame.display.set_caption("My Game")

# create object
sprites = []
ballFactory = BallFactory()

# pygame Clock
clock = pygame.time.Clock()

# GameLoop running?
running = True

while running:
    # Delta Time
    dt = clock.tick(FPS)

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousex, mousey = event.pos
            sprites.append(ballFactory.createCoinAtPosition(mousex, mousey))

    # Update
    for sprite in sprites:
        sprite.update()

    # Render
    screen.fill((255, 255, 255))
    for sprite in sprites:
        screen.blit(sprite.getImage(), sprite.getRect())

    # Double Buffering
    pygame.display.flip()


# Done! Time to quit.
pygame.quit()
