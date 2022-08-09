"""
Class to represent a single tile in a level
"""

import pygame


class Tile(pygame.sprite.Sprite):
    """
    A tile is some object within a level
    It should be rendered at a given position and have a size
    TODO: Should we have non-square tiles?
    """

    def __init__(self, pos: tuple, size: int):
        super().__init__()
        # TODO: Customize later, but for now just a grey box
        self.image = pygame.Surface((size, size))
        self.image.fill("grey")
        # Need to define rect to make it drawable, so just use the image rect
        self.rect = self.image.get_rect(topleft=pos)
