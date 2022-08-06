"""
Mario Pygame
"""

import pygame
from src import settings
from src.screen.title import TitleScreen
from src.controller.title import TitleController
from src.controller.game_over import GameOverController


# Initialize pygame screen
WIN = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
pygame.display.set_caption(settings.TITLE)


def launch():
    """
    main game launching function
    """
    screen = TitleScreen()
    controller = TitleController(screen)

    while screen:
        screen.game_loop(WIN)
        screen = controller.next_screen()
        # TODO: Temp code, need a way to determine controller dynamically in the future
        controller = GameOverController(screen)

    pygame.quit()


if __name__ == "__main__":
    launch()
