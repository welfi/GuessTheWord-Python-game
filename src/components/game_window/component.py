import pygame
from typing import List
import sys
from src.components.start_menu.component import StartMenu


class GameWindow:

    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode([self.width, self.height])
        self.start_menu = StartMenu(self.width, self.height, self)
        pygame.display.set_caption("Guess the word !")

    def show_game_screen(self):
        # Placeholder code to switch to the game screen component
        print("Switching to game screen")

    def run_game(self) -> None:
        pygame.init()
        running = True
        while running:
            for event in pygame.event.get():
                if event == pygame.QUIT:
                    running = False
            # We will be adding code here
            pygame.display.flip()
        pygame.quit()
        sys.exit()

