import random


class Cell:

    def __init__(self, possible_values):
        self._cell_val = None
        self._square = None
        self._col = None
        self._row = None
        self._possible_values = possible_values

    def set_value(self, new_val):
        self._cell_val = new_val
        self._col.erase(new_val, self)  # w tym momencie to dziala git
        self._row.erase(new_val, self)  # to w sumie tez
        self._square.erase(new_val, self)  # tutaj sie wywala na erase, bo czesc elementow square jest juz w col i row

    def choose_value(self):
        value = random.choice(list(self._possible_values))
        self.set_value(value)
        self.erase(value)

    def erase(self, val):
        self._possible_values.remove(val)

    def get_value(self):
        return self._cell_val
