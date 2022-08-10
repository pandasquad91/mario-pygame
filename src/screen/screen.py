"""
Defines a screen for the game
"""

from abc import ABC, abstractmethod
import pygame

from src import settings


class Screen(ABC):
    """
    A screen should hold state for the game during this game loop
    It is also responsible for rendering the relevant images and data to the pygame window
    """

    finished: bool = False

    def game_loop(self, surface: pygame.Surface) -> int:
        """
        Main game loop for every screen
        """
        clock = pygame.time.Clock()
        while not self.finished:
            clock.tick(settings.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # return an intention to quit the game entirely
                    return pygame.QUIT

            self.render(surface)
            pygame.display.update()

    @abstractmethod
    def render(self, surface: pygame.Surface):
        """
        Render to the pygame window
        """
