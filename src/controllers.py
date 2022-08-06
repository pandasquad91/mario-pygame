"""
Mapping each Screen to its corresponding Controller

This probably isn't the best way to do things, but I am but a humble noob
"""

# look at all those imports!
from src.screen.screen import Screen
from src.screen.title import TitleScreen
from src.screen.game_over import GameOverScreen

from src.controller.controller import Controller
from src.controller.title import TitleController
from src.controller.game_over import GameOverController


# mapping each Screen class to its corresponding Controller class
CONTROLLERS = {
    TitleScreen: TitleController,
    GameOverScreen: GameOverController,
}


class Navigator:
    """
    Manage navigation between screens by utilizing the mapping
    """

    def get_controller(self, screen: Screen) -> Controller:
        """
        Given a screen object, create a corresponding controller object
        This is kind of a hacky controller factory
        """
        # get the particular class of the passed in Screen object
        # get the corresponding Controller class from the mapping
        # instantiate the Controller object by giving it the Screen object
        return CONTROLLERS.get(type(screen))(screen)
