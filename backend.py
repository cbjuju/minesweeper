class minesweeper_backend:

    def __init__(self, number_of_rows, number_of_cols, number_of_mines):

        self.number_of_cols = number_of_cols
        self.number_of_rows = number_of_rows

        # self.state can have one of three string values : running, won, lost
        self.state = "running"

        # For the individual boxes on the screen, xposition and yposition are
        # the x and y coordinates of the top left hand corner of the box.
        box = {'has_mine':False,
                'is_number':False,
                'number':0, # Only accessed if is_number is True
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

        self.boxes_that_have_mines    = []
        self.boxes_that_have_no_mines = []

        # Assign numbers to each box if there are numbers
        for box in self.the_map:

            if box['has_mine']: self.boxes_that_have_mines.append(box)
            else: self.boxes_that_have_no_mines.append(box)

            actual_neighbours_box_numbers = self.find_neighbours(box)

            number_of_mines_around_the_box = 0

            for number in actual_neighbours_box_numbers:
                if self.the_map[number]['has_mine']:
                    number_of_mines_around_the_box += 1

            if number_of_mines_around_the_box > 0 and not box['has_mine']:
                box['is_number'] = True
                box['number']    = number_of_mines_around_the_box

    def find_neighbours(self, box):
            possible_neighbours = [
                    (box['xposition'] - 1 , box['yposition'] - 1),
                    (box['xposition']     , box['yposition'] - 1),
                    (box['xposition'] + 1 , box['yposition'] - 1),
                    (box['xposition'] - 1 , box['yposition']),
                    (box['xposition'] + 1 , box['yposition']),
                    (box['xposition'] - 1 , box['yposition'] + 1),
                    (box['xposition']     , box['yposition'] + 1),
                    (box['xposition'] + 1 , box['yposition'] + 1),
                    ]

            actual_neighbours = [
                    neighbour for neighbour in possible_neighbours if
                    neighbour[0] >= 0 and neighbour[0] < self.number_of_cols and
                    neighbour[1] >= 0 and neighbour[1] < self.number_of_rows
                    ]

            actual_neighbours_box_numbers = [
                    neighbour[1] * self.number_of_cols + neighbour[0] for
                    neighbour in actual_neighbours
                    ]

            return actual_neighbours_box_numbers

    def process_click(self, col_number, row_number, mouse_button):

        box_number = row_number * self.number_of_cols + col_number

        box_clicked = self.the_map[box_number]

        if mouse_button == 1: # left click

            box_clicked['is_covered'] = False

            if box_clicked['has_mine']: self.state = 'lost'

        if mouse_button == 3: # right click
            if box_clicked['is_flagged']: box_clicked['is_flagged'] = False
            else: box_clicked['is_flagged'] = True

    def check_if_player_won(self):
        """ The player wins if every mine if flagged and every other box
        uncovered. """
        pass
#         all_mines_flagged     = True

#         for box in self.boxes_that_have_mines:
#             all_mines_flagged = all_mines_flagged and box['is_flagged']

#         other_boxes_uncovered = True

#         for box in self.boxes_that_have_no_mines:
#             other_boxes_uncovered = other_boxes_uncovered and not box['is_covered']

#         if all_mines_flagged and other_boxes_uncovered:
#             self.state = "won"
