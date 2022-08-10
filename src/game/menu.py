"""
A model for all menus
"""

from typing import List
import pygame


class MenuOption:
    """
    An option in a menu
    """

    # TODO: Decide how to handle a menu option and require it in the future
    def __init__(self, text: str = None, image: pygame.Surface = None):
        self.text = text
        self.image = image


class Menu:
    """
    A menu class
    """

    def __init__(self, options: List[MenuOption]):
        self.selected = 0
        self.options = options

    def get_selected(self) -> MenuOption:
        """
        Return the currently selected menu option
        """
        return self.options[self.selected] if self.selected else self.options[0]

    def select_up(self):
        """
        Move selection to the next menu option
        """
        self.selected = (self.selected + 1) % len(self.options)

    def select_down(self):
        """
        Move selection to the previous menu option
        """
        if self.selected == 0:
            self.selected = len(self.options) - 1
        else:
            self.selected -= 1
