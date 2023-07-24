class Cell:

    def __init__(self, val, square, col, row, possible_vals):
        self.cell_val = val
        self.square = square
        self.col = col
        self.row = row
        self.possible_vals = possible_vals