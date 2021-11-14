import pygame as pg
import os


class Sounds():
    def __init__(self):
        self.game_folder = os.path.dirname(__file__)
        self.sound_folder = os.path.join(self.game_folder, '../sounds')
        # Ambient sound
        self.background_sound = pg.mixer.Sound(os.path.join(
            self.sound_folder, 'ambientloop.ogg'))

        # Pumpkin sounds
        self.scarecrowHit = pg.mixer.Sound(os.path.join(
            self.sound_folder, 'scarecrow-hit.ogg'))

        # Leave sounds
        self.leafHit = pg.mixer.Sound(os.path.join(
            self.sound_folder, 'leaf-hit.ogg'))

        # Gun sounds
        self.shot_sound = pg.mixer.Sound(os.path.join(
            self.sound_folder, 'gunblast.ogg'))
        self.empty_sound = pg.mixer.Sound(os.path.join(
            self.sound_folder, 'empty magazine.ogg'))
        self.reload_sound = pg.mixer.Sound(os.path.join(
            self.sound_folder, 'gun reload.ogg'))
        self.treeHit = pg.mixer.Sound(os.path.join(
            self.sound_folder, 'tree-hit.ogg'))

        # Background sounds
        self.start_sound = pg.mixer.Sound(os.path.join(
            self.sound_folder, 'start.mp3'))
        self.bestlist_sound = pg.mixer.Sound(os.path.join(
            self.sound_folder, 'bestlist.mp3'))
        self.ende_sound = pg.mixer.Sound(os.path.join(
            self.sound_folder, 'ende.mp3'))

        # Button sound
        self.button = pg.mixer.Sound(os.path.join(
            self.sound_folder, 'button1.ogg'))

        # ChickenForeground sound when comming up
        self.chickenForeground = pg.mixer.Sound(os.path.join(
            self.sound_folder, 'big-chicken-pops-up.ogg'))

    def planeCrash(self, sound: int):
        self.chick_hit1 = pg.mixer.Sound(os.path.join(
            self.sound_folder, 'airplane_loop3.ogg'))
        self.chick_hit2 = pg.mixer.Sound(os.path.join(
            self.sound_folder, 'airplanecrash.ogg'))
        self.chick_hit3 = pg.mixer.Sound(os.path.join(
            self.sound_folder, 'airplanemotorfailure.ogg'))
        self.list = [self.chick_hit1, self.chick_hit2, self.chick_hit3]
        return self.list[sound]

    def chickenDeadSound(self, sound: int):
        self.chick_hit1 = pg.mixer.Sound(os.path.join(
            self.sound_folder, 'chick_hit1.ogg'))
        self.chick_hit2 = pg.mixer.Sound(os.path.join(
            self.sound_folder, 'chick_hit2.ogg'))
        self.chick_hit3 = pg.mixer.Sound(os.path.join(
            self.sound_folder, 'chick_hit3.ogg'))
        self.list = [self.chick_hit1, self.chick_hit2, self.chick_hit3]
        return self.list[sound]
