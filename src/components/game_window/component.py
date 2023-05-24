import pygame
import sys
from src.components.start_menu.component import StartMenu
from src.components.play_game.component import PlayGame


class GameWindow:

    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode([self.width, self.height])
        self.start_menu = StartMenu(self.width, self.height, self)
        self.game_screen_active = False
        pygame.display.set_caption("Guess the word !")

    def show_game_screen(self):
        self.start_menu.menu.disable()
        self.game_screen_active = True
        play_game = PlayGame(800, 800)

        # Add code to initialize and display the game screen
        while self.game_screen_active:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                    play_game.handle_event(event)

            # Add code for game screen logic and rendering
            play_game.update()
            play_game.render(self.screen)

            pygame.display.flip()

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

