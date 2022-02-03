class minesweeper_backend:

    def __init__(self, number_of_rows, number_of_cols, number_of_mines):

        self.number_of_cols = number_of_cols
        self.number_of_rows = number_of_rows

        # For the individual boxes on the screen, xposition and yposition are
        # the x and y coordinates of the top left hand corner of the box.
        box = {'has_mine':False,
                'is_number':False,
                'is_covered':True,
                'is_exploded':True,
                'is_flagged':False,
                'is_empty':True,
                'xposition':0,
                'yposition':0}

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

        # Assign box positions
        for n, box in enumerate(self.the_map):
            box['xposition'] = n % number_of_cols
            box['yposition'] = n // number_of_cols

    def process_click(self, col_number, row_number):

        box_number = row_number * self.number_of_cols + col_number

        box_clicked = self.the_map[box_number]

        print(box_clicked)

        if box_clicked['is_number']: pass
        if box_clicked['is_covered']: pass
        if box_clicked['is_exploded']: pass
        if box_clicked['is_flagged']: pass
        if box_clicked['is_empty']: pass
