"""
Screen for the Title screen
"""

import os
import pygame

from src.screen.screen import Screen
from src import settings


# loading resources for this screen
BACKGROUND = pygame.transform.scale(
    pygame.image.load(os.path.join(settings.IMAGE_PATH, "Super Mario World Map.png")),
    (settings.WIDTH, settings.HEIGHT),
)
MARIO = pygame.transform.scale(
    pygame.image.load(os.path.join(settings.IMAGE_PATH, "Mario.png")),
    (300, 400),
)
TITLE = pygame.image.load(os.path.join(settings.IMAGE_PATH, "Mario Pygame Title.png"))
PRESS_START = pygame.image.load(os.path.join(settings.IMAGE_PATH, "Press Start.png"))


class TitleScreen(Screen):
    """
    Title Screen
    """

    def render(self, surface: pygame.Surface):
        """
        TODO:
        1. Display a background image
        2. Display Mario, the title, and Press Start text
        3. Play Music
        """
        # Display a background image
        surface.blit(BACKGROUND, (0, 0))

        # Display Mario in the center
        mario_x = settings.CENTER_X - MARIO.get_width() / 2
        mario_y = (
            settings.CENTER_Y
            - MARIO.get_height() / 2
            - TITLE.get_height()
            - PRESS_START.get_height()
        )
        surface.blit(MARIO, (mario_x, mario_y))

        # Display the title below Mario
        title_x = settings.CENTER_X - TITLE.get_width() / 2
        title_y = mario_y + MARIO.get_height() + 30
        surface.blit(TITLE, (title_x, title_y))

        # Display Press Start at the bottom
        press_start_x = settings.CENTER_X - PRESS_START.get_width() / 2
        press_start_y = title_y + TITLE.get_height() + 15
        surface.blit(PRESS_START, (press_start_x, press_start_y))

        # Do the screen update
        pygame.display.update()

        # TODO: If the user presses enter, play a sound effect and load the next screen
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_RETURN]:
            self.finished = True
