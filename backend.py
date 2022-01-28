class minesweeper_game():

    def __init__(self, number_of_rows, number_of_cols, number_of_mines):

        box = {'has_mine':False,
                'has_been_clicked':False,
                'has_been_right_clicked':False}

        number_of_boxes = number_of_rows * number_of_cols

        # Generate the empty map. It is represented here simply by a list of
        # dictionaries.
        self.the_map = [box.copy() for i in range(number_of_boxes)]

        # Place mines in the first number_of_mines number of boxes.
        for i in range(number_of_mines):
            self.the_map[i]['has_mine'] = True

        # Shuffle the map to randomize the placement of mines.
        from random import shuffle
        shuffle(self.the_map)
