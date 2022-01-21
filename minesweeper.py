import time
import backend
import pygame

newGame = backend.minesweeperGame()
newGame.printGreeting()
newGame.makeMap(2, 2, 1)

pygame.init()
width, height = 500, 500
screen = pygame.display.set_mode((width, height))

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Shesh")
            running = False
        # The following case is triggered on a left mouse click
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            xposition = event.pos[0]
            yposition = event.pos[1]

            if 0 < xposition and xposition < width and \
               0 < yposition and yposition < height:
                print("valid")
            else:
                print("invalid")
