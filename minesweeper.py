import time
import backend
import pygame
import sys

class minesweeper_game:

    def __init__(self, number_of_rows, number_of_cols, number_of_mines):
        self.number_of_rows  = number_of_rows
        self.number_of_cols  = number_of_cols
        self.number_of_mines = number_of_mines

    def initialize_the_backend(self):

        # Generate the data structure simulating the minefield
        new_game = backend.minesweeper_game(
                self.number_of_rows, 
                self.number_of_cols,
                self.number_of_mines)

    def initialize_the_frontend(self):
        # generate graphical element simulating the minefield
        pygame.init()
        pixel_width_of_box  = 50
        pixel_height_of_box = 50
        width               = number_of_cols * pixel_width_of_box
        height              = number_of_rows * pixel_height_of_box
        screen              = pygame.display.set_mode((width, height))

        # fill background with a grey colour
        screen.fill((128, 128, 128))
        # draw overlay
        for i in range(number_of_cols - 1):
            pygame.draw.line(screen,
                    (0, 0, 0),
                    (pixel_width_of_box * (i + 1), 0),
                    (pixel_width_of_box * (i + 1), pixel_height_of_box *
                        number_of_rows))
        for i in range(number_of_cols - 1):
            pygame.draw.line(screen,
                    (0, 0, 0),
                    (0, pixel_height_of_box * (i + 1)),
                    (pixel_width_of_box * number_of_cols, 
                        pixel_height_of_box * (i + 1)))

        flagImage = pygame.image.load("images/Flag.png").convert_alpha()
        flagImage = pygame.transform.scale(flagImage,(50, 50))
        screen.blit(flagImage, pygame.Rect(0, 0, 50, 50))

        # update the display to show background and overlay
        pygame.display.update()

    def start_game(self):
        # Start game loop
        running = True

        while running:

            # Get event from peripherals
            for event in pygame.event.get():

                # Click on 'x' to close window
                if event.type == pygame.QUIT:
                    running = False

                # Left mouse click
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    x_position = event.pos[0]
                    y_position = event.pos[1]

                    # Figure out which box was clicked
                    col_number = x_position // pixel_width_of_box
                    row_number = y_position // pixel_height_of_box

                    print(f"row number = {row_number} col number = {col_number}")

    def initialize(self):
        self.initialize_the_backend()
        self.initialize_the_frontend()

if __name__ == "__main__":

    number_of_rows  = int(sys.argv[1])
    number_of_cols  = int(sys.argv[2])
    number_of_mines = int(sys.argv[3])

    new_game = minesweeper_game(number_of_rows, number_of_cols, number_of_mines)
    new_game.initialize_the_backend()
    new_game.initialize_the_frontend()
    new_game.start_game()
