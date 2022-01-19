import time
import backend
import pygame

newGame = backend.minesweeperGame()
newGame.printGreeting()
newGame.makeMap(2, 2, 1)

pygame.init()
width, height = 900, 400
screen = pygame.display.set_mode((width, height))

mineImage = pygame.image.load("01_01_first_blit/01_image.png")

for i in range(10):
    mineImage.set_alpha(256)
    screen.blit(mineImage, (50 + 5 * i, 50))
    pygame.display.flip()
    time.sleep(0.5)
    screen.fill((0, 0, 0))

# for i in range(10):
#     mineImage.set_alpha(256)
#     pygame.display.flip()
#     time.sleep(0.5)
#     mineImage.set_alpha(128)
#     pygame.display.flip()
#     time.sleep(0.5)

# running = True

# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
