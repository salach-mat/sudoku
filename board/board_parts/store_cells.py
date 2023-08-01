from board.board_parts.cell import Cell


class StoreCells:
    def __init__(self, possible_values):
        self._cells = []
        self.possible_values = possible_values

    def erase(self, val, curr_cell):
        if val is None:
            return
        self.possible_values.remove(val)
        for cell in self._cells:  # przechodzimy po wszystkich cells, czyli usuneicie juz wczesniej z pierwszego wywala blad
            # if curr_cell != cell:
            cell.erase(val)

    def add_back(self, val):
        self.possible_values.add(val)
        for cell in self._cells:
            cell.add_back(val)

    def add_cell(self, cell: Cell):
        self._cells.append(cell)
