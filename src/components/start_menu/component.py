import pygame_menu
import pygame


class StartMenu:

    def __init__(self, width: int, height: int, game_window) -> None:
        self.menu = None
        self.width = width
        self.height = height
        self.game_window = game_window

    def start_game(self) -> None:
        # Placeholder code, replace with your game logic
        print("Start button clicked")
        self.game_window.show_game_screen()

    def show_leaderboard(self) -> None:
        # Placeholder code, replace with your game logic
        print("Leaderboard button clicked")

    def exit_game(self) -> None:
        pygame.quit()
        quit()

    def show_front_page(self) -> None:
        self.menu = pygame_menu.Menu("Word Learning Game", self.width, self.height,
                                     theme=pygame_menu.themes.THEME_DEFAULT)
        self.menu.add.button("Start", self.start_game)
        self.menu.add.button("Leaderboard", self.show_leaderboard)
        self.menu.add.button("Exit", self.exit_game)

        self.menu.mainloop(self.game_window.screen)  # Use game_window.screen instead of self.screen
        pygame.display.flip()