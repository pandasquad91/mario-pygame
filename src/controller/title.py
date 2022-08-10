"""
Controller for the Title screen
"""

from src.controller.controller import Controller
from src.screen.title import TitleScreen

# from src.screen.game_over import GameOverScreen
# from src.screen.level import LevelScreen
# from src.assets.lvl.test_level import MAP
from src.screen.menu import MenuScreen


class TitleController(Controller):
    """
    Handle control and navigation away from the Title screen
    """

    def __init__(self, screen: TitleScreen):
        super().__init__(screen)

    def next_screen(self):
        return MenuScreen()
        # Test loading a level
        # return LevelScreen(MAP)
        # return GameOverScreen()
