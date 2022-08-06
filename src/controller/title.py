"""
Controller for the Title screen
"""

from src.controller.controller import Controller
from src.screen.title import TitleScreen
from src.screen.game_over import GameOverScreen


class TitleController(Controller):
    """
    Handle control and navigation away from the Title screen
    """

    def __init__(self, screen: TitleScreen):
        super().__init__(screen)

    def next_screen(self):
        return GameOverScreen()
