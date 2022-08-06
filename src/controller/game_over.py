"""
Controller for the Game Over screen
"""

from src.controller.controller import Controller
from src.screen.game_over import GameOverScreen


class GameOverController(Controller):
    """
    Handle control and navigation away from the Game Over screen
    """

    def __init__(self, screen: GameOverScreen):
        super().__init__(screen)

    def next_screen(self):
        return None
