Semester project:
Mindestanforderungen:

    Programmierung eines lauffähigen Spiels

    Teambildung (2 - 4 Personen)

    Ausschließlich Python mit Modul pg

    mind. 3 Szenen: Startbildschirm, Game Over, Spiel

    mind. 5 unterschiedlich agierende Objekte (Spieler, Gegner, Hindernisse)

    Einbindung objektorientierter Konzepte (siehe Vorlesung)

    Einbindung von Entwurfsmustern (siehe Vorlesung)

    Sauberer Code (siehe Vorlesung)

Keine Wertung für:

    supertolle Grafik

    mega Sound

Pluspunkte für:

    Einsatz von Design Patterns (siehe Vorlesung)

    Übersichtlicher und strukturierter Code

    Kreativität

Abgabe der Arbeit (am Ende des Semesters):

    Source Code + Bericht (ZIP-Datei) im Moodle-System

    Arbeitsmatrix (wer hat was gemacht)

Bewertungsmatrix:

    Fehlerfreiheit (30%)

    Vollständigkeit und Features (30%)

    Codestärke (Lesbarkeit und Patterns) (30%)

    Sichere Präsentation des Projektes (10%)

-------------------------------------------------------------------------------------
Mindestanforderungen:

- Mind. 3 Szenen: Startbildschirm, Game Over, Spiel, Bestenliste
- Mind. 5 unterschiedliche agierende Objekte (Spieler, Gegner(drei verschiedene Hühnergrößen), Hindernisse, Map?) 
- Einbindung objektorientierter Konzepte
- Einbindung von Entwurfsmustern

Pluspunkte für:

- Designpatterns
- Übersichtlicher und strukturierter Code
- Kreativität

Bewertungsmatrix:

- Fehlerfreiheit (30%)
- Vollständigkeit und Features (30%)
- Codestärke (Lesbarkeit und Patterns) (30%)
- Sichere Präsentation des Projektes (10%)

-------------------------------------------------------------------------------------
Designpattern

- Dependency Injection (Seite 93)
- Strategy (Seite 103)    --> ./objects/* & ./statepattern.py
- State (Seite 112)       --> ./statepattern.py
- MVC (Seite 124)         --> ./objects/* & ./highscore/highscore.json & ./loops/*
- Observer (Seite 133)    --> ./patterns/observer.py
- Factory (Seite 142)     --> ./objects/*
- Command (Seite 152)     --> not implemented

Designpattern pygame

- Gameloop (Seite 194)    --> ./loops/*
- Update (Seite 206)      --> ./objects/*
- Movement (Seite 219)    --> ./objects/*
- Vektoren (Seite 237)    --> partly conducted (pixel perfect collision instead of rect)
- Collusion Detection (Seite 246) --> ./objects/* (pixel perfect collision instead of rect)
- Flyweight (Seite 300)   --> ./objects/*
- Camera (Seite 310)      --> ./patterns/camera.py
- Tilemap (Seite 282)     --> we don't use tiles

-------------------------------------------------------------------------------------
Task which were implemented by the following team member
Peter:
- root folder
  - statepattern.py
  - importmodules.py
  - start.py
- objects
  - chicken.py
  - chickenforeground.py
  - chickenhole.py
  - chickenwindmil.py
  - leaves.py
  - plane.py
  - predator.py
  - pumpkin.py
  - signpost.py
  - trunk.py
- settings 
  - background.py
  - menus.py
  - sounds.py (original sounds)
- loops
  - bestlistloop.py
  - endloop.py
  - gameloop.py
  - helploop.py
  - startloop.py
- _img
- refactoring

MoH:
- _img
- highscore (still in progress)
  - highscore.py
- objects
  - ammo.py
- settings
  - sounds.py (old sounds were replaced by original sounds)
- uml
  - UML.uxf
- removed sprites from lists in objects (chicken, chickenforeground, ammo, leaves)
- loops
  - gameloop.py
  - bestlistloop.py

Sebastian:
- _img
- objects
  - chicken
- patterns
  - camera.py (Updated Update function in all objects)
- loops
  - gameloop.py

Richard:
- _img
- fonts
- objects
  - chicken.py
- patterns
  - observer.py (added getPoints() in sprites which give points)
- settings
  - fonts.py
- start template from lecture
- loops
  - gameloop.py (Game timer)

Ressources:
Sprites:
  - https://www.spriters-resource.com/pc_computer/moorhuhnremake/
Sounds:
  - https://www.sounds-resource.com/pc_computer/moorremake/sound/334/

-------------------------------------------------------------------------------------
Vorgehensmodell:

SCRUM (start 01.11 - 14.11)

Rolls

- Scrum Master: Moh
- Product Owner: Peter
- Team: Richard, Sebastian

Dailys at 11 am:

- Wednesday, Friday

Weekly 12 pm:

- Sunday (Fertiges Produkt)

Nice to have:
- Mute Button
