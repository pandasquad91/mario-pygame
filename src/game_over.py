"""
The game over screen
"""

import os
import pygame
from src import settings

GAME_OVER = pygame.image.load(os.path.join("src/assets", "Game Over.png"))


def display(surface: pygame.Surface):
    """
    TODO:
    1. Display a black background
    2. Display game over text
    3. Play a game over jingle
    """
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(settings.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # Make a black screen
        surface.fill("black")

        # Draw game over text
        surface.blit(
            GAME_OVER,
            (
                settings.CENTER_X - GAME_OVER.get_width() / 2,
                settings.CENTER_Y - GAME_OVER.get_height() / 2,
            ),
        )

        # Do the screen update
        pygame.display.update()

    pygame.quit()
