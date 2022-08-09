"""
Screen for a Level
"""

from typing import List
import pygame
from src.screen.screen import Screen
from src.game.tile import Tile
from src.settings import TILE_SIZE


class LevelScreen(Screen):
    """
    Level Screen
    """

    def __init__(self, level_data: List[str]):
        super().__init__()
        self.setup(level_data)

    def setup(self, level_data: List[str]):
        """
        Given a list of strings representing a level,
        generate the tiles corresponding to this level
        """
        self.tiles = pygame.sprite.Group()
        for row_index, row in enumerate(level_data):
            for col_index, col in enumerate(row):
                # TODO: Make a list of symbols to check for later
                if col == "X":
                    # position of the tile is equivalent to
                    # the row and col index * size of the tile
                    x_pos = col_index * TILE_SIZE
                    y_pos = row_index * TILE_SIZE
                    tile = Tile((x_pos, y_pos), TILE_SIZE)
                    self.tiles.add(tile)

    def render(self, surface: pygame.Surface):
        """
        Render the tiles in this level on the given surface
        """
        surface.fill("black")
        self.tiles.draw(surface)
        pygame.display.update()
