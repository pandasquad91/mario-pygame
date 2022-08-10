"""
Screen for the game over screen
"""

import os
import pygame
from src import settings
from src.screen.screen import Screen

GAME_OVER = pygame.image.load(os.path.join(settings.IMAGE_PATH, "Game Over.png"))


class GameOverScreen(Screen):
    """
    Game Over Screen
    """

    def render(self, surface: pygame.Surface):
        """
        TODO:
        1. Display a black background
        2. Display game over text
        3. Play a game over jingle
        """
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
