class Cell:

    def __init__(self, val, square, col, row):
        self.cell_val = val
        self.square = square
        self.col = col
        self.row = row
        self.not_possible_vals = {}

    def determine_not_possible_values(self):
        if self.cell_val == 0:
            self.not_possible_vals = self.col.get_existing_values()\
                                     | self.row.get_existing_values()\
                                     | self.square.get_existing_values()
