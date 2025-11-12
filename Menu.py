import pygame
from enum import Enum
from typing import List

class MenuState(Enum):
    MAIN_MENU = 0
    SETTINGS = 1
    CREDITS = 2


class Button:
    def __init__(self):
        pass

    def draw(self):
        pass

class Menu:
    def __init__(self):
        self.buttons: List[Button] = []

    def draw(self):
        for button in self.buttons:
            button.draw()