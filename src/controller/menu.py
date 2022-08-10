"""
Controller for the Menu screen
"""

from src.controller.controller import Controller
from src.screen.game_over import GameOverScreen
from src.screen.title import TitleScreen
from src.screen.menu import MenuScreen
from src.screen.level import LevelScreen
from src.settings import ADVENTURE, LEVEL_SELECT, OPTIONS
from src.assets.lvl.test_level import MAP


class MenuController(Controller):
    """
    Handle control and navigation away from the Menu screen
    """

    def __init__(self, screen: MenuScreen):
        super().__init__(screen)

    def next_screen(self):
        menu_selection = self.screen.main_menu.selected

        # TODO: Navigate to the appropriate screen based on the menu selection
        if menu_selection == ADVENTURE:
            return LevelScreen(MAP)
        elif menu_selection == LEVEL_SELECT:
            return GameOverScreen()
        elif menu_selection == OPTIONS:
            return GameOverScreen()

        # Go back to the Title screen otherwise
        return TitleScreen()
