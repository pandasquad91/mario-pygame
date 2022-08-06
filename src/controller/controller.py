"""
Defines a controller for moving between screens
"""

from abc import ABC, abstractmethod
from src.screen.screen import Screen


class Controller(ABC):
    """
    Manage movement between screens by defining the conditions given the state
    """

    @abstractmethod
    def __init__(self, screen: Screen):
        """
        Give the controller our state via the Screen
        For subclasses, specify the appropriate subclass of Screen for the parameter
        """
        self.screen = screen

    @abstractmethod
    def next_screen(self) -> Screen:
        """
        Main function of the controller - given the state of our screen,
        determine what is the next screen to go to
        """
