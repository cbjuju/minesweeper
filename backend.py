class minesweeperGame():

    def makeMap(self, numberOfRows, numberOfCols, numberOfMines):
        box    = {'hasMine':False, 'hasBeenClicked':False}
        row    = [box] * numberOfCols
        theMap = [row] * numberOfRows
