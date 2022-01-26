class minesweeperGame():

    def makeMap(self, numberOfRows, numberOfCols, numberOfMines):
        box    = {'hasMine':False,
                'hasBeenClicked':False,
                'hasBeenRightClicked':False}
        row    = [box] * numberOfCols
        theMap = [row] * numberOfRows
