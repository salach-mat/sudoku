from board.board_parts.cell import Cell


class StoreCells:
    def __init__(self, possible_values):
        self._cells = []
        self.possible_values = possible_values
        self.removed_values = set()

    def get_cell_at(self, ind: int):
        if 0 <= ind < len(self._cells):
            return self._cells[ind]
        else:
            raise IndexError

    def erase(self, val, curr_cell):
        self.possible_values.remove(val)
        for cell in self._cells:  # przechodzimy po wszystkich cells, czyli usuneicie juz wczesniej z pierwszego wywala blad
            if curr_cell != cell:
                cell.erase(val)

    def add_cell(self, cell: Cell):
        if isinstance(cell, Cell) and cell not in self._cells:
            self._cells.append(cell)
            return True
        else:
            return False
