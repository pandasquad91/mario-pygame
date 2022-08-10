# Architecture Document

The game files for Mario Pygame are organized with a sort of [Model View Controller](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller) architecture. I don't think I've done this well or used the terms quite right - I don't recommend following my spaghetti as a guideline!


### Assets

Contains the game assets, no code.

* `img` - images
* `lvl` - level maps
* `mus` - music
* `snd` - sound


### Controller

Contains 'controller' classes. The controllers handle which screens can be navigated to from any particular screen. Every screen must have a corresponding controller defined in the main `controllers.py` file.


### Screen

Contains 'view' classes. A Screen handles rendering the view to the pygame window.


### Game

Contains 'model' classes.