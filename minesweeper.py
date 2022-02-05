import backend
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import sys
import time

class minesweeper_game:

    def __init__(self, number_of_rows, number_of_cols, number_of_mines):
        self.number_of_rows      = number_of_rows
        self.number_of_cols      = number_of_cols
        self.number_of_mines     = number_of_mines
        self.pixel_width_of_box  = 50
        self.pixel_height_of_box = 50

        # Initialize the graphical element simulating the minefield
        pygame.init()
        self.width  = number_of_cols * self.pixel_width_of_box
        self.height = number_of_rows * self.pixel_height_of_box
        self.screen = pygame.display.set_mode((self.width, self.height))

        # Load images
        self.exploded_box_image = pygame.image \
            .load("images/minesweeper_tiles/exploded_box.jpg") \
            .convert()

        self.covered_box_image = pygame.image \
            .load("images/minesweeper_tiles/covered_box.jpg") \
            .convert()

        self.empty_box_image = pygame.image \
            .load("images/minesweeper_tiles/empty_box.jpg") \
            .convert()

        self.flagged_box_image = pygame.image \
            .load("images/minesweeper_tiles/flagged_box.jpg") \
            .convert()

        self.one_image = pygame.image \
            .load("images/minesweeper_tiles/one.jpg") \
            .convert()

        self.two_image = pygame.image \
            .load("images/minesweeper_tiles/two.jpg") \
            .convert()

        self.three_image = pygame.image \
            .load("images/minesweeper_tiles/three.jpg") \
            .convert()

        self.four_image = pygame.image \
            .load("images/minesweeper_tiles/four.jpg") \
            .convert()

        self.five_image = pygame.image \
            .load("images/minesweeper_tiles/five.jpg") \
            .convert()

        self.six_image = pygame.image \
            .load("images/minesweeper_tiles/six.jpg") \
            .convert()

        self.seven_image = pygame.image \
            .load("images/minesweeper_tiles/seven.jpg") \
            .convert()

        self.eight_image = pygame.image \
            .load("images/minesweeper_tiles/eight.jpg") \
            .convert()

        self.dark_overlay = pygame.image \
            .load("images/dark_overlay.png") \
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

        self.number_images = [
                self.one_image, 
                self.two_image, 
                self.three_image, 
                self.four_image, 
                self.five_image, 
                self.six_image, 
                self.seven_image, 
                self.eight_image, 
                ]

    def initialize_the_backend(self):

        self.game_backend = backend.minesweeper_backend(self.number_of_rows,
                                                        self.number_of_cols,
                                                        self.number_of_mines)

    def draw_map(self):
        # fill background with a grey colour
        self.screen.fill((128, 128, 128))

        for box in self.game_backend.the_map:
            xposition = box['xposition'] * self.pixel_width_of_box
            yposition = box['yposition'] * self.pixel_height_of_box

            rectangle = pygame.Rect(xposition, 
                                    yposition,
                                    self.pixel_width_of_box,
                                    self.pixel_height_of_box)

            if box['has_mine']:
                self.screen.blit(self.exploded_box_image, rectangle)
            if box['is_number']:
                number_of_mines = box['number']
                self.screen.blit(self.number_images[number_of_mines - 1], rectangle)
            if box['is_covered']:
                self.screen.blit(self.covered_box_image, rectangle)
            if box['is_flagged']:
                self.screen.blit(self.flagged_box_image, rectangle)

        # draw overlay : vertical lines
        for i in range(number_of_cols - 1):
            pygame.draw.line(self.screen,
                    (0, 0, 0),
                    (self.pixel_width_of_box * (i + 1), 0),
                    (self.pixel_width_of_box * (i + 1), self.pixel_height_of_box *
                        number_of_rows))

        # draw overlay : horizontal lines
        for i in range(number_of_rows - 1):
            pygame.draw.line(self.screen,
                    (0, 0, 0),
                    (0, self.pixel_height_of_box * (i + 1)),
                    (self.pixel_width_of_box * number_of_cols, 
                        self.pixel_height_of_box * (i + 1)))

        # cover screen with a dark overlay on the map to signal end of game
        if self.game_backend.state == "won":
            print ("You won")
            self.screen.blit(self.dark_overlay, 
                                pygame.Rect(0, 0, self.height, self.width))
            self.screen.blit(pygame.font.SysFont("Comic Sans MS",100).render("You win!",1,(0,255,0)),pygame.Rect(200,300,100,50))
            pygame.display.update()
        if self.game_backend.state == "lost":
            print ("You lost")
            self.screen.blit(self.dark_overlay, 
                    pygame.Rect(0, 0, self.height, self.width))
            self.screen.blit(pygame.font.SysFont("Comic Sans MS",100).render("You win!",1,(0,255,0)),pygame.Rect(200,300,100,50))
            pygame.display.update()

        pygame.display.update()

    def start_game(self):

        while self.game_backend.state == "running":

            # Get event from peripherals
            for event in pygame.event.get():

                # Click on 'x' to close window
                if event.type == pygame.QUIT:
                    exit()

                # Mouse click
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x_position = event.pos[0]
                    y_position = event.pos[1]

                    # Figure out which box was clicked
                    col_number = x_position // self.pixel_width_of_box
                    row_number = y_position // self.pixel_height_of_box

                    # Process the click
                    self.game_backend.process_click(
                                            col_number, 
                                            row_number, 
                                            event.button)

                    self.game_backend.check_if_player_won()

                    # Update the screen
                    self.draw_map()

        # Once game loop is broken, decide if player wants to keep playing
        waiting_for_player_decision = True

        while waiting_for_player_decision:

            for event in pygame.event.get():

                if event.type == pygame.KEYDOWN:
                    waiting_for_player_decision = False
                    if event.key == pygame.K_r:
                        return True
                    if not event.key == pygame.K_r:
                        return False

if __name__ == "__main__":

    # if len(sys.argv) < 4:
    #     print ("Too few arguments")
    #     exit()

    # number_of_rows  = int(sys.argv[1])
    # number_of_cols  = int(sys.argv[2])
    # number_of_mines = int(sys.argv[3])

    number_of_rows  = 10
    number_of_cols  = 10
    number_of_mines = 10

    new_game = minesweeper_game(number_of_rows, number_of_cols, number_of_mines)
    new_game.initialize_the_backend()
    new_game.draw_map()

    play_another_game = new_game.start_game()

    while play_another_game:
        number_of_rows  = 10
        number_of_cols  = 10
        number_of_mines = 20

        new_game = minesweeper_game(number_of_rows, number_of_cols, number_of_mines)
        new_game.initialize_the_backend()
        new_game.draw_map()

        play_another_game = new_game.start_game()
