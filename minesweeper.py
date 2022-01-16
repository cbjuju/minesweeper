import backend
import pygame as pg

newGame = backend.minesweeperGame()
newGame.printGreeting()
newGame.makeMap(2, 2, 1)

pg.init()
width, height = 900, 400
screen = pg.display.set_mode((width, height))
