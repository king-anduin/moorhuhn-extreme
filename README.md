# Moorhuhn extreme

---

## On this page

1. [What is this all about](#what-is-this-all-about)  
   1.1 [Introduction](#introduction)  
   1.2 [What is needed for playing](#what-is-needed-for-playing)  
   1.3 [How to start the game](#how-to-start-the-game)

2. [Pictures](#pictures)  
   2.1 [That is the start screen](#that-is-the-start-screen)  
   2.2 [That is the highscore screen](#that-is-the-highscore-screen)  
   2.3 [That is the help screen](#that-is-the-help-screen)  
   2.4 [That is the game screen](#that-is-the-game-screen)  
   2.5 [That is the end screen](#that-is-the-end-screen)
3. [What's covered in this repo](#whats-covered-in-this-repo)  
   3.1 [Designpattern](#designpattern)  
   3.2 [Designpattern pygame](#designpattern-pygame)
4. [Ressources](#ressources)  
   4.1 [Sprites](#sprites)  
   4.2 [Sounds](#sounds-pygame)
5. [Further materials](#further-materials)

---

## What is this all about?

### Introduction

- This was a little project in our fifth semester and it was done in 14 days. You can use this code as you like but we're probably not maintaining this repository. It is good for people who starts with pygame.

### What is needed for playing

- Python
- Pygame

### How to start the game

- Just start `start.py`
- If you wanna put your name on the highscore instead of _None_, change `PLAYERNAME` on `settings/settings.py`

---

## Pictures

### That is the start screen

![That is the start screen](/_img/screenshots/start.png "Start Screen")

### That is the highscore screen

![That is the highscore screen](/_img/screenshots/highscore.png "Highscore Screen")

### That is the help screen

![That is the help screen](/_img/screenshots/help.png "Help Screen")

### That is the game screen

That is just part of the map. You can scroll to the left and right side.
![That is the game screen](/_img/screenshots/game.png "Game Screen")

### That is the end screen

![That is the end screen](/_img/screenshots/end.png "End Screen")

---

## What's covered in this repo

### Designpattern

- Dependency Injection
- Strategy --> ./objects/\* & ./statepattern.py
- State --> ./statepattern.py
- MVC --> ./objects/_ & ./highscore/highscore.json & ./loops/_
- Observer --> ./patterns/observer.py
- Factory --> ./objects/\*
- Command --> not implemented

### Designpattern pygame

- Gameloop --> ./loops/\*
- Update --> ./objects/\*
- Movement --> ./objects/\*
- Vektoren --> partly conducted (pixel perfect collision instead of rect)
- Collusion Detection (Seite 246) --> ./objects/\* (pixel perfect collision instead of rect)
- Flyweight --> ./objects/\*
- Camera --> ./patterns/camera.py
- Tilemap --> we don't use tiles

---

## Ressources

### Sprites:

- https://www.spriters-resource.com/pc_computer/moorhuhnremake/

### Sounds:

- https://www.sounds-resource.com/pc_computer/moorremake/sound/334/

---

## Further materials

### Python:

- https://www.w3schools.com/python/

### Pygame Dokumentation:

- https://www.pygame.org/docs/

### Pygame Buch:

- http://programarcadegames.com/index.php?lang=de

### Kenney Assets:

- https://kenney.nl/

### Other Free Assets:

- https://OpenGameArt.org

### Game Programming Patterns (C++):

- https://gameprogrammingpatterns.com/contents.html

### Nature of Code:

- https://natureofcode.com/book/
