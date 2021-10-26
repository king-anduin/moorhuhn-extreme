import pygame as pg

pg.init()
screen = pg.display.set_mode((640, 480))
clock = pg.time.Clock()
# pg.mouse.set_visible(False)
BG_COLOR = pg.Color('gray12')

CURSOR_IMG = pg.Surface((40, 40), pg.SRCALPHA)
pg.draw.circle(CURSOR_IMG, pg.Color('white'), (20, 20), 20, 2)
pg.draw.circle(CURSOR_IMG, pg.Color('white'), (20, 20), 2)
# Create a rect which we'll use as the blit position of the cursor.
cursor_rect = CURSOR_IMG.get_rect()

done = False
while not done:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True
        elif event.type == pg.MOUSEMOTION:
            # If the mouse is moved, set the center of the rect
            # to the mouse pos. You can also use pygame.mouse.get_pos()
            # if you're not in the event loop.
            cursor_rect.center = event.pos

    screen.fill(BG_COLOR)
    # Blit the image at the rect's topleft coords.
    screen.blit(CURSOR_IMG, cursor_rect)
    pg.display.flip()
    clock.tick(30)

pg.quit()