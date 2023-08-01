import random


class Cell:

    def __init__(self, possible_values):
        self._cell_val = None
        self.square = None
        self.col = None
        self.row = None
        self.possible_values = possible_values
        self._removed_values = set()

    def set_value(self, new_val):
        self._cell_val = new_val
        self.col.erase(new_val, self)  # wywala sie na rekurencji przy powrocie do poprzedniego indeksu
        self.row.erase(new_val, self)
        self.square.erase(new_val, self)

    def choose_value(self):
        self.remove_actual_value()
        value = random.choice(list(self.possible_values))
        self.set_value(value)
        # self.erase(value)

    def erase(self, val):
        if val not in self._removed_values:
            self.possible_values.remove(val)
            self._removed_values.add(val)

    def get_value(self):
        return self._cell_val

    def get_possible_values(self):
        return self.possible_values

    def add_back(self, val):
        if val in self._removed_values:
            self.possible_values.add(val)
            self._removed_values.remove(val)

    def remove_actual_value(self):
        if self._cell_val is not None:
            self.col.add_back(self._cell_val)
            self.row.add_back(self._cell_val)
            self.square.add_back(self._cell_val)
            self._cell_val = None
