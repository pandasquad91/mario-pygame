"""
Mario Pygame
"""

import pygame
from src import settings
from src import title_screen

# Initialize pygame screen
WIN = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
pygame.display.set_caption(settings.TITLE)


def main():
    """
    main game
    """
    title_screen.display(WIN)


if __name__ == "__main__":
    main()
