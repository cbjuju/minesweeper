import backend
import pygame

newGame = backend.minesweeperGame()
newGame.printGreeting()
newGame.makeMap(2, 2, 1)

pygame.init()
width, height = 900, 400
screen = pygame.display.set_mode((width, height))

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
