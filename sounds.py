import pygame as pg


class Sounds():
    def __init__(self):
        # Ambient sound
        self.background_sound = pg.mixer.Sound("sounds/background.mp3")
        self.background_sound.play(-1)

        # Gun sounds
        self.shot_sound = pg.mixer.Sound("sounds/schiessen.mp3")
        self.empty_sound = pg.mixer.Sound("sounds/empty.mp3")
        self.reload_sound = pg.mixer.Sound("sounds/reload.mp3")

        # Sounds
        self.start_sound = pg.mixer.Sound("sounds/start.mp3")

        # Sounds
        self.bestlist_sound = pg.mixer.Sound("sounds/bestlist.mp3")

        # Sounds
        self.ende_sound = pg.mixer.Sound("sounds/ende.mp3")
