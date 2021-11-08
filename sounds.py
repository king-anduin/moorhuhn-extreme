import pygame as pg


class Sounds():
    def __init__(self):
        # Ambient sound
        self.background_sound = pg.mixer.Sound("sounds/ambientloop.ogg")

        # Pumpkin sounds
        self.scarecrowHit = pg.mixer.Sound("sounds/scarecrow-hit.ogg")

        # Leave sounds
        self.leafHit = pg.mixer.Sound("sounds/leaf-hit.ogg")

        # Gun sounds
        self.shot_sound = pg.mixer.Sound("sounds/gunblast.ogg")
        self.empty_sound = pg.mixer.Sound("sounds/empty magazine.ogg")
        self.reload_sound = pg.mixer.Sound("sounds/gun reload.ogg")
        self.treeHit = pg.mixer.Sound("sounds/tree-hit.ogg")

        # Background sounds
        self.start_sound = pg.mixer.Sound("sounds/start.mp3")
        self.bestlist_sound = pg.mixer.Sound("sounds/bestlist.mp3")
        self.ende_sound = pg.mixer.Sound("sounds/ende.mp3")

        # Button sound
        self.button = pg.mixer.Sound("sounds/button1.ogg")

    def planeCrash(self, sound: int):
        self.chick_hit1 = pg.mixer.Sound("sounds/airplane_loop3.ogg")
        self.chick_hit2 = pg.mixer.Sound("sounds/airplanecrash.ogg")
        self.chick_hit3 = pg.mixer.Sound(
            "sounds/airplanemotorfailure.ogg")
        self.list = [self.chick_hit1, self.chick_hit2, self.chick_hit3]
        return self.list[sound]

    def chickenDeadSound(self, sound: int):
        self.chick_hit1 = pg.mixer.Sound("sounds/chick_hit1.ogg")
        self.chick_hit2 = pg.mixer.Sound("sounds/chick_hit2.ogg")
        self.chick_hit3 = pg.mixer.Sound("sounds/chick_hit3.ogg")
        self.list = [self.chick_hit1, self.chick_hit2, self.chick_hit3]
        return self.list[sound]
