from src.components.game_window.component import GameWindow
import pygame

if __name__ == '__main__':
    pygame.init()
    game_window = GameWindow(800, 800)
    game_window.start_menu.show_front_page()
    game_window.run_game()