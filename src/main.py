"""
Mario Pygame
"""

import pygame
from src import settings
from src.screen.title import TitleScreen
from src.controller.title import TitleController
from src.controllers import Navigator


# Initialize pygame screen
WIN = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
pygame.display.set_caption(settings.TITLE)


def launch():
    """
    main game launching function
    """
    nav = Navigator()

    # Always start at the title screen
    screen = TitleScreen()
    controller = TitleController(screen)

    # Continually navigate between screens until we quit
    while screen:
        # perform the game loop on this screen
        screen.game_loop(WIN)
        # when we exit this loop, use the controller to determine what screen we go to next
        screen = controller.next_screen()
        # get the new screen's controller, if we have one
        controller = nav.get_controller(screen) if screen else None

    pygame.quit()


if __name__ == "__main__":
    launch()
