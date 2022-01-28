import tkinter
import pyautogui
import time
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

    def initialize_the_backend(self):

        # Generate the data structure simulating the minefield
        self.new_game = backend.minesweeper_game(
                self.number_of_rows, 
                self.number_of_cols,
                self.number_of_mines)

    def initialize_the_frontend(self):
        # generate graphical element simulating the minefield
        pygame.init()
        width               = number_of_cols * self.pixel_width_of_box
        height              = number_of_rows * self.pixel_height_of_box
        screen              = pygame.display.set_mode((width, height))

        # fill background with a grey colour
        screen.fill((128, 128, 128))
        # draw overlay
        for i in range(number_of_cols - 1):
            pygame.draw.line(screen,
                    (0, 0, 0),
                    (self.pixel_width_of_box * (i + 1), 0),
                    (self.pixel_width_of_box * (i + 1), self.pixel_height_of_box *
                        number_of_rows))
        for i in range(number_of_cols - 1):
            pygame.draw.line(screen,
                    (0, 0, 0),
                    (0, self.pixel_height_of_box * (i + 1)),
                    (self.pixel_width_of_box * number_of_cols, 
                        self.pixel_height_of_box * (i + 1)))

        flagImage = pygame.image.load("images/Flag.png").convert_alpha()
        flagImage = pygame.transform.scale(flagImage,
                (self.pixel_width_of_box, self.pixel_height_of_box))

        for box in self.new_game.the_map:
            if box['has_mine']:
                xposition = box['xposition'] * self.pixel_width_of_box
                yposition = box['yposition'] * self.pixel_height_of_box
                rectangle = pygame.Rect(xposition, 
                        yposition,
                        self.pixel_width_of_box,
                        self.pixel_height_of_box)

                screen.blit(flagImage, rectangle)
        
        # update the display to show overlay
        pygame.display.update()

        # for box in self.new_game.the_map:
        box = self.new_game.the_map[0]
        xposition = box['xposition'] * self.pixel_width_of_box
        yposition = box['yposition'] * self.pixel_height_of_box
        print(f"x = {xposition} y = {yposition}")
        # pyautogui.moveTo(xposition, yposition)
        time.sleep(1)

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
                    col_number = x_position // self.pixel_width_of_box
                    row_number = y_position // self.pixel_height_of_box

                    print(f"row number = {row_number} col number = {col_number}")
                    box_number = row_number * number_of_cols + col_number
                    has_mine = self.new_game.the_map[box_number]['has_mine']
                    if has_mine: print(f"has mine")

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
