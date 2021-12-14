# Moorhuhn extreme

## Table of contents

1. Introduction
2. Pictures
3. What's covered in this repo
4. Ressources
5. Further materials

---

## On this page

{:.no_toc}

1. Introduction
   {:Introduction}

---

## Introduction

- This was a little project in our fifth semester and it was done in 14 days. You can use this code as you like but we're probably not maintaining this repository. It is good for people who starts with pygame.

## What's needed for playing

- Python
- Pygame

## How to start the game

- Just start `start.py`

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

## Ressources

### Sprites:

- https://www.spriters-resource.com/pc_computer/moorhuhnremake/

### Sounds:

- https://www.sounds-resource.com/pc_computer/moorremake/sound/334/

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
