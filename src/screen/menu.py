"""
Screen for the main menu
"""

import pygame
from src.screen.screen import Screen
from src.game.menu import Menu, MenuOption
from src.settings import ADVENTURE, LEVEL_SELECT, OPTIONS


class MenuScreen(Screen):
    """
    Main Menu Screen
    """

    def __init__(self):
        super().__init__()

        # Our main menu options
        # TODO: These need images for us to draw
        adventure = MenuOption()
        level_select = MenuOption()
        options = MenuOption()

        menu_options = [None, None, None]
        menu_options[ADVENTURE] = adventure
        menu_options[LEVEL_SELECT] = level_select
        menu_options[OPTIONS] = options

        # Create the main menu to render
        self.main_menu = Menu(menu_options)

    def handle_input(self):
        """
        Handle the user input to move through our menu
        """
        keys_pressed = pygame.key.get_pressed()

        # TODO: If the user presses enter, play a sound effect and load the next screen
        if keys_pressed[pygame.K_RETURN]:
            self.finished = True

        # Pressing back means no menu option selected
        # This should return us to the title screen
        if keys_pressed[pygame.K_ESCAPE]:
            self.main_menu.selected = None
            self.finished = True

        # Pressing up and down should cycle us through the menu options
        if keys_pressed[pygame.K_UP]:
            self.main_menu.select_up()
        if keys_pressed[pygame.K_DOWN]:
            self.main_menu.select_down()

    def render(self, surface: pygame.Surface):
        """
        Draw the menu options to the screen
        TODO:
        1. Display list of menu options
        2. Update the selected option based on key presses
        """
        surface.fill("black")
        # TODO: The menu scrolls through way too fast - add a delay or something
        self.handle_input()
