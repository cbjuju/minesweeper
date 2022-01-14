class minesweeperGame():
    def printGreeting(self):
        print ("Welcome to minesweeper!\n")

    def makeMap(self, xblocks, yblocks, nmines):
        print (f"The map has {xblocks * yblocks} blocks and {nmines} mine(s).")
