import backend
import pygame
import sys

class minesweeper_game:

    def __init__(self, number_of_rows, number_of_cols, number_of_mines):
        self.number_of_rows      = number_of_rows
        self.number_of_cols      = number_of_cols
        self.number_of_mines     = number_of_mines
        self.pixel_width_of_box  = 50
        self.pixel_height_of_box = 50

        # Initialize the graphical element simulating the minefield
        pygame.init()
        width       = number_of_cols * self.pixel_width_of_box
        height      = number_of_rows * self.pixel_height_of_box
        self.screen = pygame.display.set_mode((width, height))

        # Load images
        self.exploded_box_image = pygame.image \
            .load("images/minesweeper_tiles/exploded_box.jpg") \
            .convert_alpha()

        self.covered_box_image = pygame.image \
            .load("images/minesweeper_tiles/covered_box.jpg") \
            .convert_alpha()

        self.empty_box_image = pygame.image \
            .load("images/minesweeper_tiles/empty_box.jpg") \
            .convert_alpha()

        self.flagged_box_image = pygame.image \
            .load("images/minesweeper_tiles/flagged_box.jpg") \
            .convert_alpha()

        self.one_image = pygame.image \
            .load("images/minesweeper_tiles/one.jpg") \
            .convert_alpha()

        self.two_image = pygame.image \
            .load("images/minesweeper_tiles/two.jpg") \
            .convert_alpha()

        self.three_image = pygame.image \
            .load("images/minesweeper_tiles/three.jpg") \
            .convert_alpha()

        self.four_image = pygame.image \
            .load("images/minesweeper_tiles/four.jpg") \
            .convert_alpha()

        self.five_image = pygame.image \
            .load("images/minesweeper_tiles/five.jpg") \
            .convert_alpha()

        self.six_image = pygame.image \
            .load("images/minesweeper_tiles/six.jpg") \
            .convert_alpha()

        self.seven_image = pygame.image \
            .load("images/minesweeper_tiles/seven.jpg") \
            .convert_alpha()

        self.eight_image = pygame.image \
            .load("images/minesweeper_tiles/eight.jpg") \
            .convert_alpha()

        # Scale images so that they fit into one box on the minefield
        self.exploded_box_image = pygame.transform.scale(self.exploded_box_image,
                (self.pixel_width_of_box, self.pixel_height_of_box))

        self.covered_box_image = pygame.transform.scale(self.covered_box_image,
                (self.pixel_width_of_box, self.pixel_height_of_box))

        self.empty_box_image = pygame.transform.scale(self.empty_box_image,
                (self.pixel_width_of_box, self.pixel_height_of_box))

        self.flagged_box_image = pygame.transform.scale(self.flagged_box_image,
                (self.pixel_width_of_box, self.pixel_height_of_box))

        self.one_image = pygame.transform.scale(self.one_image,
                (self.pixel_width_of_box, self.pixel_height_of_box))

        self.two_image = pygame.transform.scale(self.two_image,
                (self.pixel_width_of_box, self.pixel_height_of_box))

        self.three_image = pygame.transform.scale(self.three_image,
                (self.pixel_width_of_box, self.pixel_height_of_box))

        self.four_image = pygame.transform.scale(self.four_image,
                (self.pixel_width_of_box, self.pixel_height_of_box))

        self.five_image = pygame.transform.scale(self.five_image,
                (self.pixel_width_of_box, self.pixel_height_of_box))

        self.six_image = pygame.transform.scale(self.six_image,
                (self.pixel_width_of_box, self.pixel_height_of_box))

        self.seven_image = pygame.transform.scale(self.seven_image,
                (self.pixel_width_of_box, self.pixel_height_of_box))

        self.eight_image = pygame.transform.scale(self.eight_image,
                (self.pixel_width_of_box, self.pixel_height_of_box))

    def initialize_the_backend(self):

        self.game_backend = backend.minesweeper_backend(self.number_of_rows, self.number_of_cols, self.number_of_mines)

    def initialize_the_frontend(self):

        # fill background with a grey colour
        self.screen.fill((128, 128, 128))

        # draw overlay
        for i in range(number_of_cols - 1):
            pygame.draw.line(self.screen,
                    (0, 0, 0),
                    (self.pixel_width_of_box * (i + 1), 0),
                    (self.pixel_width_of_box * (i + 1), self.pixel_height_of_box *
                        number_of_rows))

        for i in range(number_of_cols - 1):
            pygame.draw.line(self.screen,
                    (0, 0, 0),
                    (0, self.pixel_height_of_box * (i + 1)),
                    (self.pixel_width_of_box * number_of_cols, 
                        self.pixel_height_of_box * (i + 1)))

        # Draw initial box images over the overlay
        for box in self.game_backend.the_map:
            xposition = box['xposition'] * self.pixel_width_of_box
            yposition = box['yposition'] * self.pixel_height_of_box

            rectangle = pygame.Rect(xposition, 
                                    yposition,
                                    self.pixel_width_of_box,
                                    self.pixel_height_of_box)

            self.screen.blit(self.covered_box_image, rectangle)

        # update the display to show overlay
        pygame.display.update()
        pass

    def start_game(self):
        # Start game loop
        running = True

        while running:

            # Get event from peripherals
            for event in pygame.event.get():

                # Click on 'x' to close window
                if event.type == pygame.QUIT:
                    running = False

                # Mouse click
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x_position = event.pos[0]
                    y_position = event.pos[1]

                    # Figure out which box was clicked
                    col_number = x_position // self.pixel_width_of_box
                    row_number = y_position // self.pixel_height_of_box

                    new_game.process_click(col_number, row_number)
                    # box_number = row_number * number_of_cols + col_number

    def initialize(self):
        self.initialize_the_backend()
        self.initialize_the_frontend()

if __name__ == "__main__":

    if len(sys.argv) < 4:
        print ("Too few arguments")
        exit()

    number_of_rows  = int(sys.argv[1])
    number_of_cols  = int(sys.argv[2])
    number_of_mines = int(sys.argv[3])

    new_game = minesweeper_game(number_of_rows, number_of_cols, number_of_mines)
    new_game.initialize_the_backend()
    new_game.initialize_the_frontend()
    # new_game.start_game()
