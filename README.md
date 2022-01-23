Python implementation of the popular game minesweeper.

There is a class called minesweeperGame in the module backend. An instance of
this class is generated every time the user asks to play a game. Mouse button
presses are accepted from the user and the game moves forward based on the
nature of the tile that has been clicked on. The tile can have one of 3
important properties : it is an empty tile, or it is a number showing the
number of mines around the tile or it is empty.

- If the user clicks on a tile that is a number, nothing else happens.
- If the user clicks on a mine, the game ends.
- If the user clicks on an empty tile, all the safe tiles that are adjacent to
  each other are opened.

The file minesweeper.py is the frontend of the program. It is the GUI of the
program and presents an interface to the user. The backend of the program is
the file backend.py which handles all the logic of the program. The file
minesweeper.py lets the user press a button and the file backend.py decides
what happens when the user presses that button.

Future work : implement multithreading in assigning mines initially to the map.
It should be an embarrassingly parallel problem.
