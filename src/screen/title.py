"""
Screen for the Title screen
"""

import os
import pygame

from src.screen.screen import Screen
from src import settings


BACKGROUND = pygame.transform.scale(
    pygame.image.load(os.path.join("src/assets", "Super Mario World Map.png")),
    (settings.WIDTH, settings.HEIGHT),
)


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
        # should clock also be a param?
        # clock = pygame.time.Clock()
        # run = True
        # while run:
        #     clock.tick(settings.FPS)
        #     for event in pygame.event.get():
        #         if event.type == pygame.QUIT:
        #             run = False

        # does doing it this way work??

        # Display a background image
        surface.blit(BACKGROUND, (0, 0))

        # Display Mario in the center

        # Display the title below Mario

        # Display Press Start at the bottom

        # Do the screen update
        pygame.display.update()

        # TODO: If the user presses enter, play a sound effect and load the next screen
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_RETURN]:
            self.finished = True
