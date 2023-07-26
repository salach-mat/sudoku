class StoreCells:
    def __init__(self, num):
        self._num = num
        self._cells = []

    def get_existing_values(self):
        return {cell.get_value() for cell in self._cells}

    def get_cell_at(self, ind):
        if 0 <= ind < len(self._cells):
            return self._cells[ind]
        else:
            raise IndexError

    def add_cell(self, cell):
        self._cells.append(cell)
