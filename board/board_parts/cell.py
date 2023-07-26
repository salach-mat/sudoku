class Cell:

    def __init__(self, val, square, col, row):
        self._cell_val = val
        self._square = square
        self._col = col
        self._row = row
        self._not_possible_vals = {}

    def determine_not_possible_values(self):
        if self._cell_val == 0:
            self._not_possible_vals = self._col.get_existing_values() \
                                      | self._row.get_existing_values() \
                                      | self._square.get_existing_values()

    def set_value(self, new_val):
        self._cell_val = new_val

    def get_value(self):
        return self._cell_val

    def get_not_possible_vals(self):
        self.determine_not_possible_values()
        return self._not_possible_vals
