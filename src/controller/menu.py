"""
Controller for the Menu screen
"""

from src.controller.controller import Controller
from src.screen.game_over import GameOverScreen
from src.screen.menu import MenuScreen


class MenuController(Controller):
    """
    Handle control and navigation away from the Menu screen
    """

    def __init__(self, screen: MenuScreen):
        super().__init__(screen)

    def next_screen(self):
        return GameOverScreen()
