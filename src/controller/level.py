"""
Controller for a Level
"""

from src.controller.controller import Controller
from src.screen.game_over import GameOverScreen


class LevelController(Controller):
    """
    Handle control and navigation away from a level
    """

    def __init__(self, screen: GameOverScreen):
        super().__init__(screen)

    def next_screen(self):
        return GameOverScreen()
