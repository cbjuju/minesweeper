import time
import backend
import pygame
import sys

# Input from command line
numberOfRows  = int(sys.argv[1])
numberOfCols  = int(sys.argv[2])
numberOfMines = int(sys.argv[3])

# Generate the data structure simulating the minefield
newGame = backend.minesweeperGame()
newGame.makeMap(numberOfRows, numberOfCols, numberOfMines)

# Generate graphical element simulating the minefield
pygame.init()
pixelWidthOfBox  = 50
pixelHeightOfBox = 50
width            = numberOfCols * pixelWidthOfBox
height           = numberOfRows * pixelHeightOfBox
screen           = pygame.display.set_mode((width, height))

running = True

# Fill background with a grey colour
screen.fill((128, 128, 128))
# Draw overlay
for i in range(numberOfCols - 1):
    pygame.draw.line(screen,
            (0, 0, 0),
            (pixelWidthOfBox * (i + 1), 0),
            (pixelWidthOfBox * (i + 1), pixelHeightOfBox * numberOfRows))
for i in range(numberOfCols - 1):
    pygame.draw.line(screen,
            (0, 0, 0),
            (0, pixelHeightOfBox * (i + 1)),
            (pixelWidthOfBox * numberOfCols, pixelHeightOfBox * (i + 1)))
# Update the display to show background and overlay
pygame.display.update()

# Start game loop
while running:

    # Get event from peripherals
    for event in pygame.event.get():

        # Click on 'x' to close window
        if event.type == pygame.QUIT:
            running = False

        # Left mouse click
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            xPosition = event.pos[0]
            yPosition = event.pos[1]

            # Figure out which box was clicked
            colNumber = xPosition // pixelWidthOfBox
            rowNumber = yPosition // pixelHeightOfBox

            print(f"row number = {rowNumber} col number = {colNumber}")
