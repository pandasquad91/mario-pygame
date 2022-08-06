"""
The title screen of the game
"""

import os
import pygame
from src import settings

BACKGROUND = pygame.transform.scale(
    pygame.image.load(os.path.join("src/assets", "Super Mario World Map.png")),
    (settings.WIDTH, settings.HEIGHT),
)


def display(surface: pygame.Surface):
    """
    TODO:
    1. Display a background image
    2. Display Mario, the title, and Press Start text
    3. Play Music
    """
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(settings.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # Display a background image
        # surface.fill(settings.WHITE)
        surface.blit(BACKGROUND, (0, 0))

        # Display Mario in the center

        # Display the title below Mario

        # Display Press Start at the bottom

        # Do the screen update
        pygame.display.update()

        # TODO: If the user presses enter, play a sound effect and load the next screen
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_RETURN]:
            run = False

    pygame.quit()
