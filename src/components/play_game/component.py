import pygame

class PlayGame:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)
        self.word = "WELFI"  # Placeholder word, replace with your actual word
        self.guess = [""] * len(self.word)  # Empty list for user's guesses
        self.current_case = 0
        self.background_image = pygame.image.load("src/assets/background.jpg")  # Replace with your image file
        self.background_image = pygame.transform.scale(self.background_image, (self.width, self.height))

    def update(self):
        # Add game logic here

        # For example, check if the user's guess matches the word
        if "".join(self.guess) == self.word:
            print("Congratulations! You guessed the word correctly.")

    def render(self, screen):
        screen.fill((255, 255, 255))  # Fill the screen with white color
        screen.blit(self.background_image, (0, 0))
        # Display the "Definition" text
        definition_text = self.font.render("Definition", True, (0, 0, 0))
        definition_rect = definition_text.get_rect()
        definition_rect.center = (self.width / 2, 20)
        screen.blit(definition_text, definition_rect)

        # Display the word definition
        definition = self.font.render("He who is smart but sleeps alot", True, (0, 0, 0))
        definition_rect = definition.get_rect()
        definition_rect.center = (self.width / 2, 60)
        screen.blit(definition, definition_rect)  # Adjust the position as needed

        # Display the timer
        timer_text = self.font.render("Timer: 00:00", True, (0, 0, 0))
        screen.blit(timer_text, (self.width // 2 - timer_text.get_width() // 2, self.height // 2 - 20))

        # Display the letter input boxes
        letter_box_width = 40  # Width of each letter input box
        letter_box_height = 40  # Height of each letter input box
        letter_box_margin = 10  # Margin between letter input boxes
        letter_box_x = (self.width - (len(self.word) * (letter_box_width + letter_box_margin))) // 2
        letter_box_y = self.height - letter_box_height - 80 # Adjust the position as needed

        for i, letter in enumerate(self.word):
            # Determine the position of each letter input box
            x = letter_box_x + i * (letter_box_width + letter_box_margin)
            y = letter_box_y

            # Draw the letter input box
            pygame.draw.rect(screen, (0, 0, 0), (x, y, letter_box_width, letter_box_height), 2)

            # Display the user's guess in the letter input box
            guess_text = self.font.render(self.guess[i], True, (0, 0, 0))
            screen.blit(guess_text, (x + letter_box_width // 2 - guess_text.get_width() // 2,
                                     y + letter_box_height // 2 - guess_text.get_height() // 2))

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                # Handle backspace key press to delete the last character in the user's guess
                self.handle_backspace_click()
            elif event.key == pygame.K_RETURN:
                # Handle enter key press to submit the guess and check if it matches the word
                self.update()
            else:
                # Handle other key presses to input characters into the user's guess
                for i, letter in enumerate(self.word):
                    if self.guess[i] == "":
                        self.current_case = i
                        self.guess[i] = event.unicode.upper()
                        break

    def handle_backspace_click(self):
        self.guess[self.current_case] = ""
        if self.current_case == 0:
            pass
        else:
            self.current_case -= 1
