import backend
import pygame

newGame = backend.minesweeperGame()
newGame.printGreeting()
newGame.makeMap(2, 2, 1)

pygame.init()
width, height = 900, 400
screen = pygame.display.set_mode((width, height))

mineImage = pygame.image.load("images/Mine.png")
screen.blit(mineImage, (100, 100))
pygame.display.flip()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
